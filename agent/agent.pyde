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

    global grid

    if frontier:

        u = frontier.pop(0)
        i, j = u
        grid[i][j].visited = True

        if (i, j) != s and (i, j) != e:
            grid[i][j].setColor("#f757f7") #set color pink to show the elements that were visited 

        if u == e: #if we found the food

            time.sleep(2) #delay to show we found the path
            reset() #reseting the actual colors of all the elements
            time.sleep(1) #delay before coloring the path

            path = backtrace(parent, s, e)
            for i, j in path:
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#850000") #set the path color
        
            return True, path
                
        y, x = u
        for v in neighbors(y, x): #access the neighbors of the current element
            i, j = v
            if v not in frontier and not grid[i][j].visited: #if the neighbor is not already in the frontier and it wasnt visited, add it to the list
                parent[v] = u
                frontier.append(v)
                i, j = v
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#000057") #set color dark blue to show the neighbors elements
    
    return False, []
                
                
def heuristic(a, b):
   #Manhattan distance on a square grid
   return abs(a[1] - b[1]) + abs(a[0] - b[0])


def custoso(s, e):

    global grid

    if frontier_cost:

        cost, p = heapq.heappop(frontier_cost)
        i, j = p
        grid[i][j].visited = True

        if (i, j) != s and (i, j) != e:
            grid[i][j].setColor("#f757f7") #set color pink to show the elements that were visited 

        if p == e: #if we found the food

            time.sleep(2) #delay to show we found the path
            reset() #reseting the actual colors of all the elements
            time.sleep(1) #delay before coloring the path

            path = backtrace(parent, s, e)
            for i, j in path:
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#850000") #set the path color
           
            return True, path

        y, x = p
        for next in neighbors(y, x): #access the neighbors of the current element
            a, b = next
            new_cost = cost_so_far[p] + grid[a][b].cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                prioridade = new_cost
                heapq.heappush(frontier_cost,(prioridade, next))
                parent[next] = p
                if (i, j) != s and (i, j) != e:
                    grid[a][b].setColor("#000057") #set color dark blue to show the neighbors elements
    
    return False, []


def aStar(s,e):

    global grid
    
    if frontier_cost:

        cost, p = heapq.heappop(frontier_cost)
        i, j = p
        grid[i][j].visited = True

        if (i, j) != s and (i, j) != e:
            grid[i][j].setColor("#f757f7") #set color pink to show the elements that were visited
        
        if p == e: #if we found the food

            time.sleep(2) #delay to show we found the path
            reset() #reseting the actual colors of all the elements
            time.sleep(1) #delay before coloring the path

            path = backtrace(parent, s, e)
            for i, j in path:
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#850000") #set the path color
            
            return True, path
        
        y, x = p
        for next in neighbors(y, x): #access the neighbors of the current element
            a, b = next
            new_cost = cost_so_far[p] + grid[a][b].cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                prioridade = new_cost + heuristic(e, next)
                heapq.heappush(frontier_cost,(prioridade, next))
                parent[next] = p
                if (i, j) != s and (i, j) != e:
                    grid[a][b].setColor("#000057") #set color dark blue to show the neighbors elements
    
    return False, []


def greedy(s, e):

    global grid

    if frontier_cost:

        c, u = frontier_cost.pop(0)
        i, j = u
        grid[i][j].visited = True

        if (i, j) != s and (i, j) != e:
            grid[i][j].setColor("#f757f7") #set color pink to show the elements that were visited 

        if u == e: #if we found the food

            time.sleep(2) #delay to show we found the path
            reset() #reseting the actual colors of all the elements
            time.sleep(1) #delay before coloring the path
                
            path = backtrace(parent, s, e)
            for i, j in path:
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#850000") #set the path color
                
            return True, path
                
        y, x = u
        for v in neighbors(y, x): #access the neighbors of the current element
            i, j = v
            if v not in came_from and not grid[i][j].visited:
                priority = heuristic(e, v)
                parent[v] = u
                heapq.heappush(frontier_cost, (priority, v))
                came_from[v] = u
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#000057") #set color dark blue to show the neighbors elements
    
    return False, []


def dfs(s, e):

    global grid

    if frontier:

        u = frontier.pop(-1)
        i, j = u
        grid[i][j].visited = True

        if (i, j) != s and (i, j) != e:
            grid[i][j].setColor("#f757f7") #set color pink to show the elements that were visited 

        if u == e: #if we found the food

            time.sleep(2) #delay to show we found the path
            reset() #reseting the actual colors of all the elements
            time.sleep(1) #delay before coloring the path
                
            path = backtrace(parent, s, e)
            for i, j in path:
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#850000") #set the path color
                
            return True, path
                
        y, x = u
        for v in neighbors(y, x): #access the neighbors of the current element
            i, j = v
            if v not in frontier and not grid[i][j].visited:
                parent[v] = u
                frontier.append(v)
                i, j = v
                if (i, j) != s and (i, j) != e:
                    grid[i][j].setColor("#000057") #set color dark blue to show the neighbors elements
    
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
    global old_element_type
    
    s = f
    old = f
        
    i, j = s
    grid[i][j].updateElementType(element_type = "agent") #agent

    if old_element_type:
        grid[i][j].updateElementType(element_type = old_element_type)

    #reset()

    e = randint(0, rows - 1), randint(0, cols - 1)
    i, j = e

    while f == e or grid[i][j].obstacle:
        e = randint(0, rows - 1), randint(0, cols - 1)
        i, j = e

    old_element_type = grid[i][j].element_type
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
    global old_element_type


    size(600, 600)
    font = createFont("Arial", 16)
    cnt = 0
    rows,cols = 40, 40
    scaleX = width/cols 
    scaleY = height/rows -2
    s = (0, 0) #start position of agent
    e = (rows - 1, cols - 1)
    old = s

    #creation of random map
    less_cols = int(cols/5)
    less_rows = int(rows/5)
    grid = [["" for j in range(cols)] for i in range(rows)]
    for x in range(less_rows):
        for y in range(less_cols):
            
            if x != 0 and y != 0:
                #sand 30%, mud 30%, watter 30%, obstacle 10%
                random = randint(1, 10)
                if random < 2:
                    element_type = "obstacle"
                elif random < 5:
                    element_type = "sand"
                elif random < 8:
                    element_type = "mud"
                else:
                    element_type = "watter"
            else: #no obstacle in 0, 0 possition
                #sand 33.33...%, mud 33.33...%, watter 33.33...%
                random = randint(1, 9)
                if random < 4:
                    element_type = "sand"
                elif random < 7:
                    element_type = "mud"
                else:
                    element_type = "watter"
            
            for i in range(x*5, x*5 + 5):
                for j in range(y*5, y*5 + 5):
                    grid[i][j] = MatrixElement(i, j, element_type = element_type)

    old_element_type = grid[0][0].element_type
    init(s)
    walk = False


def goto(old, next):

    iOld, jOld = old
    iNext, jNext = next
    
    grid[iNext][jNext].setColor("#9f1cfc") #agent
    grid[iOld][jOld].setColor("#850000") #path
    

def draw():

    global frontier, parent, s, path
    global finish
    global last
    global walk
    global old
    global font, cnt
    global grid

    if not finish:

        i, j = s
        grid[i][j].setColor("#9f1cfc") #agent
        i, j = e
        grid[i][j].setColor("#55ff55") #food

        finish, path = greedy(s, e)
        if finish:
            walk = finish
            s = e

    elif walk and finish:

        next = path.pop(0)
        i, j = next
        if grid[i][j].element_type == "sand":
            time.sleep(0.1)
        elif grid[i][j].element_type == "mud":
            time.sleep(0.5)
        elif grid[i][j].element_type == "watter":
            time.sleep(1.0)

        goto(old, next)
        old = next
        time.sleep(0.2)
        if len(path) == 0:
            walk = False
            cnt += 1

    else:

        time.sleep(1)
        reset()
        time.sleep(1)
        init(e)
                
    background(0)
    printGrid(grid)
    fill("#f3f6f4")
    textFont(font, 32)
    text("Food Collected: {}".format(cnt), 5, height - 10)
