from matrix_element import MatrixElement

from random import randint
import heapq
import time


def backtrace(parent, start, e):

    path = [e]

    while path[-1] != start:
        path.append(parent[path[-1]])

    path.reverse()
    return path   


def neighbors(i, j):

    r = [-1,-1,-1, 0, 0, +1, +1, +1]
    c = [-1, 0, +1, -1, +1, -1, 0,  +1]
    ret = []

    for k in range(8):
        y, x = i + r[k], j + c[k]
        if (0 <= y < rows) and (0 <= x < cols) and not grid[y][x].obstacle:
            ret.append((y, x))

    return ret

                 
def bfs(s, e):

    global life

    if frontier:
        u = frontier.pop(0)
        i,j = u
        grid[i][j].visited = True
        if (i, j) != s and (i, j) != e:
            grid[i][j].setColor("#f757f7")   
        if u == e:
            i, j = u
            path = backtrace(parent, s, e)
            for i, j in path:
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#850000")
            
            if (i, j) != s and (i, j) != e:
                grid[i][j].setColor("#55ff55")
            return True, path
                
        y, x = u
        for v in neighbors(y, x):
            i,j = v
            if v not in frontier and not grid[i][j].visited:
                parent[v] = u
                frontier.append(v)
                i,j = v
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#000057")
    
    return False, []
                
                
def heuristic(a, b):
   #Manhattan distance on a square grid
   return abs(a[1] - b[1]) + abs(a[0] - b[0])


def custoso(s, e):

    if frontier_cost:
        cost, p = heapq.heappop(frontier_cost)
        i, j = p
        grid[i][j].visited = True
        if (i, j) != s and (i, j) != e:
            grid[i][j].setColor("#f757f7")   

        if p == e:
            path = backtrace(parent, s, e)
            for i, j in path:
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#850000")
            i, j = e
            grid[i][j].setColor("#55ff55")
            return True, path

        y, x = p
        for next in neighbors(y, x):
            a, b = next
            new_cost = cost_so_far[p] + grid[a][b].cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                prioridade = new_cost
                heapq.heappush(frontier_cost,(prioridade, next))
                parent[next] = p
                if (i, j) != s and (i, j) != e:
                    grid[a][b].setColor("#000057")
    
    return False, []


def aStar(s,e):
    
    if frontier_cost:
        cost, p = heapq.heappop(frontier_cost)
        i, j = p
        grid[i][j].visited = True
        if (i, j) != s and (i, j) != e:
            grid[i][j].setColor("#f757f7")   
        if p == e:
            path = backtrace(parent, s, e)
            for i,j in path:
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#850000")
            i, j = e
            grid[i][j].setColor("#55ff55")
            return True, path
        
        y, x = p
        for next in neighbors(y, x):
            a, b = next
            new_cost = cost_so_far[p] + grid[a][b].cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                prioridade = new_cost + heuristic(e, next)
                heapq.heappush(frontier_cost,(prioridade, next))
                parent[next] = p
                if (i, j) != s and (i, j) != e:
                    grid[a][b].setColor("#000057")
    
    return False, []


def greedy(s, e):

    if frontier_cost:
        c, u = frontier_cost.pop(0)
        i, j = u
        grid[i][j].visited = True
        if (i, j) != s and (i, j) != e:
            grid[i][j].setColor("#f757f7")   

        if u == e:
            i, j = u
                
            path = backtrace(parent, s, e)
            for i, j in path:
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#850000")
                
            if (i, j) != s and (i, j) != e:
                grid[i][j].setColor("#55ff55")
            return True, path
                
        y, x = u
        for v in neighbors(y, x):
            i, j = v
            if v not in came_from and not grid[i][j].visited:
                priority = heuristic(e, v)
                parent[v] = u
                heapq.heappush(frontier_cost, (priority, v))
                came_from[v] = u
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#000057")
    
    return False, []


def dfs(s, e):

    if frontier:
        u = frontier.pop(-1)
        i, j = u
        grid[i][j].visited = True
        if (i, j) != s and (i, j) != e:
            grid[i][j].setColor("#f757f7")    

        if u == e:
            i, j = u
                
            path = backtrace(parent, s, e)
            for i,j in path:
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#850000")
                
            if (i, j) != s and (i, j) != e:
                grid[i][j].setColor("#55ff55")
            return True, path
                
        y, x = u
        for v in neighbors(y, x):
            i, j = v
            if v not in frontier and not grid[i][j].visited:
                parent[v] = u
                frontier.append(v)
                i, j = v
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#000057")
    
    return False, []


def reset():

    for spots in grid:
        for spot in spots:
            spot.setColor()
            spot.visited = False


def printGrid(grid):

    global scaleX, scaleY

    for spots in grid:
        for spot in spots:
            spot.show(scaleX, scaleY)    


def init(f):

    global s, e, finish
    global frontier, parent
    global came_from, frontier_cost, cost_so_far, grid
    global old

    s = f
    old = f
        
    i, j = s
    grid[i][j].setColor("#9f1cfc")
    
    i, j = e
    grid[i][j].setColor("#55ff55")

    grid[i][j].updateElementType(element_type = None)
    e = randint(0, rows - 1), randint(0, cols - 1)
    i, j = e

    while f == e or grid[i][j].obstacle:
        e = randint(0, rows - 1), randint(0, cols - 1)
        i, j = e
    
    grid[i][j].updateElementType(element_type = 'food')
        
    grid[i][j].setColor()
    parent = {}
    frontier = []
    frontier.append(s)
    finish = False
    
    frontier_cost = []
    heapq.heappush(frontier_cost, (0, s))
    came_from = {}
    came_from[s] = None
    cost_so_far = {}
    cost_so_far[s] = 0
    
    
def setup():

    global font, cnt
    global grid
    global rows, cols
    global scaleX, scaleY
    global frontier, frontier_cost, parent, finish, came_from, cost_so_far, walk
    global s, e
    global old
    global life

    life = 100

    size(600, 600)
    font = createFont("Arial", 16)
    cnt = 0
    rows,cols = 40, 40
    scaleX = width/cols 
    scaleY = height/rows -2
    s = (0, 0)
    e = (rows - 1, cols - 1)
    old = s
    grid = [[MatrixElement(i, j) for j in range(cols)] for i in range(rows)]
    init(s)
    walk = False


def goto(old, next):

    global life

    iOld, jOld = old
    iNext, jNext = next
    
    grid[iNext][jNext].setColor("#9f1cfc")
    grid[iOld][jOld].setColor("#850000")
    

def draw():

    global frontier, parent, s, path
    global finish
    global last
    global walk
    global old
    global font, cnt
    global life

    if not finish:

        i, j = s
        grid[i][j].setColor("#9f1cfc")
        i, j = e
        grid[i][j].setColor("#55ff55")
        finish, path = custoso(s, e)
        if finish:
            walk = finish
            s = e

    elif walk and finish:

        next = path.pop(0)
        goto(old, next)
        life -= grid[next[0]][next[1]].cost #subtracting life from agent based on path element
        if life <= 0:
            #agent died before getting to the food so DO SOMETHING
            pass
        old = next
        time.sleep(0.2)
        if len(path) == 0:
            walk = False
            life += 20 #life from food
            cnt += 1

    else:

        time.sleep(1)
        reset()
        init(e)
                
    background(0)
    printGrid(grid)
    fill("#f3f6f4")
    textFont(font, 32)
    text("Food Collected: {}".format(cnt), 5, height - 10)
    text("Agents Life: {}".format(life), 5, height - 45)