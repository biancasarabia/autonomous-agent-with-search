from random import randint

class MatrixElement:

    #POSSIBLE ELEMENT TYPES -> food, obstacle, sand, watter, mud or None
    
    def __init__(self, x, y, element_type = None) :
        
        self.x = x
        self.y = y
        self.element_type = element_type

        self.sand, self.mud, self.watter, self.obstacle, self.food = False, False, False, False, False

        #fazer código para geração aleatória de elementos

        self.cost = 0
       
        if self.element_type == "sand":
            self.sand = True
            self.cost = 1
        elif self.element_type == "mud":
            self.mud = True
            self.cost = 2
        elif self.element_type == "watter":
            self.watter = True
            self.cost = 3
        elif self.element_type == "obstacle":
            self.obstacle = True
        elif self.element_type == "food":
            self.food = True
            
        self.color = "#f3f6f4" #the matrix empty spots will be a gray-ish white
        self.visited = False #flag to indicate if the element was visited
        self.setColor(0) #set differend color to different type of elements
        

    def setColor(self, stage, reset = None):
        
        if self.food:
            self.color = "#e43b3b" #red
        elif self.obstacle:
            self.color = "#444444" #dark gray
        elif self.sand:
            self.color = "#ebc633" #golden yellow (sand)
        elif self.mud:
            self.color = "#834300" #brown (mud)
        elif self.watter:
            self.color = "#834300" #blue (watter)
             
        if reset:
            self.color = "#f3f6f4" #gray-ish white
        

    def show(self, element_width, element_height):
        
        fill(self.color)
        stroke(0)
        rect(self.x * element_width, self.y * element_height, element_width, element_height)