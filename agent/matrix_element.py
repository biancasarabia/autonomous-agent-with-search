from random import randint

class MatrixElement:

    #POSSIBLE ELEMENT TYPES -> food, obstacle, sand, watter, mud or None
    
    def __init__(self, x, y, element_type = None) :
        
        self.x = x
        self.y = y
        self.element_type = element_type

        self.sand, self.mud, self.watter, self.obstacle, self.food = False, False, False, False, False
        self.cost = 0

        #code snippet for random generation of elements
        if not self.element_type:

            self.cost = 1 if randint(0, 10) > 4 else randint(2, 3)
            self.obstacle = True if randint(0, 10) < 1 else False

            if self.cost == 1:
                self.element_type = "sand"
            elif self.cost == 2:
                self.element_type = "mud"
            elif self.cost == 3:
                self.element_type = "watter"
 
        if self.element_type == "obstacle":
            self.obstacle = True
        elif self.element_type == "food":
            self.food = True
        elif self.element_type == "sand":
            self.sand = True
        elif self.element_type == "mud":
            self.mud = True
        elif self.element_type == "watter":
            self.watter = True
            
        self.visited = False #flag to indicate if the element was visited
        self.setColor() #set differend color to different type of elements

    def updateElementType(self, element_type = None):

        self.element_type = element_type
        self.sand, self.mud, self.watter, self.obstacle, self.food = False, False, False, False, False
        self.cost = 0

        if not self.element_type:

            self.cost = 1 if randint(0, 10) > 4 else randint(2, 3)
            self.obstacle = True if randint(0, 10) < 1 else False

            if self.cost == 1:
                self.element_type = "sand"
            elif self.cost == 2:
                self.element_type = "mud"
            elif self.cost == 3:
                self.element_type = "watter"
       
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
        
        self.visited = False #flag to indicate if the element was visited
        self.setColor() #set differend color to different type of elements


    def setColor(self, color = None, reset = None):

        if not color:

            if reset:

                self.color = "#f3f6f4" #gray-ish white
                self.sand, self.mud, self.watter, self.obstacle, self.food = False, False, False, False, False

            else:

                if self.food:
                    self.color = "#55ff55" #green
                elif self.obstacle:
                    self.color = "#000000" #black
                elif self.sand:
                    self.color = "#ebc633" #golden yellow (sand)
                elif self.mud:
                    self.color = "#834300" #brown (mud)
                elif self.watter:
                    self.color = "#89cff0" #blue (watter)

        else:

            self.color = color #the matrix empty spots will change to a selected color



    def show(self, element_width, element_height):

        if self.food:
            fill(self.color)
        elif self.obstacle:
            fill(self.color)
        elif self.sand:
            fill(self.color)
        elif self.mud:
            fill(self.color)
        elif self.watter:
            fill(self.color)

        stroke(0)
        rect(self.x * element_width, self.y * element_height, element_width, element_height)