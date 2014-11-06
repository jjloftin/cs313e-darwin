#-----------
#Darwin.py
#-----------


class Darwin :
  '''
  This is the game board class. Holds the creatures and tells them whether or not they can move as requested.
  Goes through the board to execute instructions of creatures. Also, this holds all of the instructions
  '''
  def __init__(self,x,y):
    self.world = []
    self.turns = 0  
  def add(self,c,x,y):
    '''
    Add creature to the world if space is empty
    '''
    self.world[x,y] = c
  def execute(self,x,y):
    '''
    Creature in spot executes its turn. If empty does nothing.
    '''
  def turn(self):
    '''
    Executes one run on the game board. Each creature getting to execute once.
    '''    



class Species :
  '''
  Species class is made to hold instructions for individual creatures.
  '''
  def __init__(self,s):
    self.name = s
    self.instructions = []
  def addInstruction (self, s) :
    self.instructions.append(s)

class Creature :
  '''
  Individual creatures which sit in the game board and interact with other creatues.
  Have a list of instructions from species, a program counter to tell them
  where in the list they are, and they have a direction. 
  '''
  def __init__(self,species,direction):
    self.species = species
    self.direction = 0
    self.counter = 0
    
  def go(self):
    '''
    Creature executes directions until accomplishing one action move
    '''
  def hop (self, c):
    '''
    If creature has nothing obstructing it, it hops forward one space
    '''
    pass
  
  def infect (self, c) : 
    '''
    If creature in front is enemy, turn it into enacting creatures species
    '''
    pass
    
  def left (self, c) :
    '''
    Turn creature left
    '''
    
  def right (self, c) :
    '''
    Turn creature right
    '''
  