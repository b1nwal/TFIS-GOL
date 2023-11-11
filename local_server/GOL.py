lfmap = {} 
cells = []
future_cells = []
steps = 5 # temporary steps var

class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def affect_lfmap(self):
        for _x in range(-1,2):
            for _y in range(-1,2):
                if _x == 0 and _y == 0:
                    continue
                loc = (self.x + _x, self.y + _y)
                lfmap[loc] = lfmap.get(loc,0) + 1
    def affect_state(self): # you should treat yourself NOW!
        lf = lfmap.get((self.x,self.y), 0)
        if lf == 0: return
        del lfmap[(self.x,self.y)]
        if 2 <= lf <= 3:
            future_cells.append(self)
    def iaffect_lfmap():
        for i in cells:
            i.affect_lfmap()
    def iaffect_state():
        for i in cells:
            i.affect_state()
    def idisplay_state():
        for i in cells:
            ### This will be the code the outputs state information
            print(i.x,i.y) # for now, just print it to stdout
            		   # could remain this way, if cmd_gen.exe just reads stdout

### temporary initial code ###

ls = [(0,-1),(1,-1),(2,-1),(2,-2),(1,-3)]

for i in ls:
    cells.append(Cell(i[0],i[1])) 

##############################

for i in range(steps):
    Cell.iaffect_lfmap()
    Cell.iaffect_state()
    for i in lfmap: 
        if lfmap[i] == 3:
            future_cells.append(Cell(i[0],i[1]))
    cells = future_cells
    lfmap = {}
    future_cells = []

Cell.idisplay_state()
