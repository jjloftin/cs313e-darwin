#-----------
#Darwin.py
#by John Loftin
#-----------


class Darwin :
  '''
  This is the game board class. Holds the creatures and tells them whether or not they can move as requested.
  Goes through the board to execute instructions of creatures. 
  
  World Variables
  world - the actual game board. 2D list with empty space tokens and stores pointers to creature instances
  
  World Attribute Variables
  x_max - maximum horizontal expanse of the world
  y_max - maximum vertical exxpanse of the world
  turns - keeps track of number of turns of the simulation has been run
  
  Creature Tracking Variables. Keep track of whats in front of creatures when running the game board.
  If the creature asks for allowed information about the board state, the game board returns it to the creature.
  Boolean valued.
  
  empty - is the space in front empty or a wall
  wall - is the space in front a wall
  enemy - is the space in front a different species
  '''
  def __init__(self,x,y):
    '''
    Initialize the data members and construct an empty game board.
    '''
    self.world = []
    
    self.x_max = x-1
    self.y_max = y-1
    self.turns = 0
    
    self.empty = None
    self.wall = None    
    self.enemy = None
  def add(self,c,x,y):
    '''
    Add creature to the world if space is empty
    '''
    
    return ''

  def go(self,x,y):
    '''
    If empty does nothing. Otherwise, tells creature to 'go' and execute its next action.
    '''
    
  '''
  Space Check Methods. These are the methods a creature can use while executing its turn to check the space in front of it.
  '''  
  def isEmpty(self,c):
    '''
    Takes a creature in and returns whether or not the space in front of the creature is empty.
    '''
    return '1'
  def isWall(self,c):
    '''
    Takes a creature in and returns whether or not the space in front of the creature is a wall.
    '''
    return '1'
  
  def isEnemy(self,c):
    '''
    Takes in a creature and lets you know if the space in front of the creature contains an enemy. 
    '''
    return '1'
    
  def turn(self):
    '''
    Executes one run on the game board. Each creature getting to execute once.
    '''    
    return False
  def __str__(self):
    '''
    Returns the grid in printable form
    '''
    s = '  '
    return s
    
  '''
  Creature - World Interaction Methods. These get called when the creature executes its turn. The game board needs to reconfigure itself to account
  for executions of turns by the creature.
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
    
class Species :
  '''
  Species class is made to hold instructions for individual creatures.
  '''
  def __init__(self,name):
    assert type(name) is str
    assert name[0].isalpha()
    
    self.name = name.lower()
    self.instructions = []
  def addInstruction (self, s):
      self.instructions.append(s)
  
 
class Creature :
  '''
  Individual creatures which sit in the game board and interact with other creatues.
  Have a list of instructions from species, a program counter to tell them
  where in the list they are, and they have a direction. 
  
  We also hardcode in the list of actions. This weill help us know when a creature executes its turn if it committed an action
  species - the species of the creature
  direction - the direction of the creature stored as a string 'north', 'south', 'west', 'east'
  counter - stores where in the species instruction list the creature is
  actions - stores the action commands. if one of these is executed a creature ceases to execute directions
  '''
  def __init__(self,species,direction):
    self.species = species
    self.direction = direction
    self.counter = 0
    self.actions = ['hop', 'infect', 'left', 'right']
  def execute(self):
    '''
    Creature executes directions until executing an action move. Returns that action move to the game board. 
    '''
    return ''
  