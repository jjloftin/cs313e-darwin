#-----------
#Darwin.py
#by John Loftin
#-----------

from random import randrange,seed

class Darwin :
  '''
  This is the game board class. Holds the creatures and tells them whether or not they can move as requested.
  Goes through the board to execute instructions of creatures. 
  
  World Variables
  world - the actual game board. 2D list with empty space tokens and stores pointers to creature instances
  
  World Attribute Variables
  j_max - maximum horizontal expanse of the world
  i_max - maximum vertical exxpanse of the world
  turns - keeps track of number of turns of the simulation has been run
  
  Creature Tracking Variables. Keep track of whats in front of creatures when running the game board.
  If the creature asks for allowed information about the board state, the game board returns it to the creature.
  Boolean valued.
  
  empty - is the space in front empty or a wall
  wall - is the space in front a wall
  enemy - is the space in front a different species
  '''
  def __init__(self,vert_size,hor_size):
    '''
    Initialize the data members and construct an empty game board.
    '''
    assert type(vert_size) == int
    assert type(hor_size) == int
    
    
    self.world = []
    for j in range(vert_size):
      self.world.append([])
      for i in range(hor_size):
        self.world[j].append('.')
    
    
    self.j_max = hor_size - 1
    self.i_max = vert_size - 1
    self.turns = 0
    
    self.empty = None
    self.wall = None    
    self.enemy = None
  def add(self,c,i,j):
    '''
    Add creature to the world if space is empty
    '''
    assert type(c) == Creature
    if(j <= self.j_max and i <= self.i_max):
      self.world[i][j] = c
    

  def go(self,i,j):
    '''
    If empty does nothing. Otherwise, tells creature to 'go' and execute its next action.
    '''
    assert i <= self.i_max
    assert j <= self.j_max
    
    if(self.world[i][j] == '.'):
      return 
      
    dir = self.world[i][j].getDirection()

    assert type(i) == int
    assert type(j) == int

    #Assign the status variables.
    if(dir == 'north'):
      if(i == 0):
        self.wall = True
        self.empty = False
        self.enemy = False
      elif(self.world[i-1][j] != '.'):
        self.empty = False
        self.wall = False
        
        if(str(self.world[i-1][j]) == str(self.world[i][j])):
          self.enemy = False
        else:
          self.enemy = True
      else:
        self.empty = True
        self.wall = False
        self.enemy = False
    elif(dir == 'south'):
      if(i == self.i_max):
        self.wall = True
        self.empty = False
        self.enemy = False
      elif(self.world[i+1][j] != '.'):
        self.empty = False
        self.wall = False
        if(str(self.world[i+1][j]) == str(self.world[i][j])):
          self.enemy = False
        else:
          self.enemy = True
      else:
        self.empty = True
        self.wall = False
        self.enemy = False    
    elif(dir == 'west'):
      if(j == 0):
        self.wall = True
        self.empty = False
        self.enemy = False
      elif(self.world[i][j-1] != '.'):
        self.empty = False
        self.wall = False
        if(str(self.world[i][j-1]) == str(self.world[i][j])):
          self.enemy = False
        else:
          self.enemy = True
      else:
        self.empty = True
        self.wall = False
        self.enemy = False
    elif(dir == 'east'):
      if(j == self.j_max):
        self.wall = True
        self.empty = False
        self.enemy = False
      elif(self.world[i][j+1] != '.'):
        self.empty = False
        self.wall = False
        if(str(self.world[i][j+1]) == str(self.world[i][j])):
          self.enemy = False
        else:
          self.enemy = True
      else:
        self.empty = True
        self.wall = False
        self.enemy = False   
    '''
    Creature - World Interaction Methods. These get called when the creature executes its turn. The game board needs to reconfigure itself to account
    for executions of turns by the creature.
    '''  
    def hop (c):
      '''
      If creature has nothing obstructing it, it hops forward one space
      '''
      if(dir == 'north' and self.empty) :
        self.world[i-1][j] = c
        self.world[i][j] = '.'
      elif(dir == 'south' and self.empty) :
        self.world[i + 1][j] = c
        self.world[i][j] = '.'
      elif(dir == 'west' and self.empty) :
        self.world[i][j-1] = c
        self.world[i][j] = '.'
      elif(dir == 'east' and self.empty) :
        self.world[i][j+1] = c
        self.world[i][j] = '.'
      
    def infect (c) : 
      '''
      If creature in next space is an enemy, that space is infected. IE it becomes another member of the infecting creatures species with initial counter = 0
      '''
      assert type(c) == Creature
      dir = c.getDirection()
      if(dir == 'north' and self.enemy) :
        self.world[i - 1][j].getInfected(c)
      elif(dir == 'south' and self.enemy) :
        self.world[i + 1][j].getInfected(c)
      elif(dir == 'west' and self.enemy) :
        self.world[i][j - 1].getInfected(c)
      elif(dir == 'east' and self.enemy) :
        self.world[i][j + 1].getInfected(c)
        
    #Now tell the creature to go
    cmd = self.world[i][j].execute(self)
    
    if(cmd == 'hop'):
      hop(self.world[i][j])
    elif(cmd == 'infect'):
      infect(self.world[i][j])
    
  
      
    
  def turn(self):
    '''
    Executes one run on the game board. Each creature getting to execute once.
    done = creatures who have executed their turns already
    '''    
    self.turns += 1
    done = []
    
    for i in range(self.i_max+1):
      for j in range(self.j_max+1):
        if(self.world[i][j] not in done):
          done.append(self.world[i][j])         
          self.go(i,j)
         
          
  '''
  Space Check Methods. These are the methods a creature can use while executing its turn to check the space in front of it.  
  '''  
  def isEmpty(self):
    '''
    Returns whether or not the space in front of the active creature is empty.
    '''
    return self.empty
  def isWall(self):
    '''
    Returns whether or not the space in front of the active creature is a wall.
    '''
    return self.wall
  
  def isEnemy(self):
    '''
    Returns whether or not space in front of the active creature contains an enemy. 
    '''
    return self.enemy
    
  def __str__(self):
    '''
    Returns the grid in printable form
    '''
    s = '  '
    for i in range(self.j_max+1):
      s += str(i)
    s += '\n'
    for i in range(self.i_max+1):
      s += str(i) + ' '
      for j in range(self.j_max+1):
        s+= str(self.world[i][j])
      s += '\n' 
    
    return s
    

    
    
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
  def getInstruction(self, counter):
    return self.instructions[counter]

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
  def execute(self,d = Darwin(1,1)):
    '''
    Creature executes directions until executing an action move. Returns that action move to the game board. 
    d - is a game board.
    '''
    while True:
      cmd = self.species.getInstruction(self.counter)
      #If an action command. Execute it then end turn.
      if(cmd in self.actions):
        self.counter += 1
        break
      
      #Execute control commands.
      if(cmd[:-2] == 'if_empty' and d.isEmpty()):
        self.counter = int(cmd[-1])
        continue
      if(cmd[:-2] == 'if_empty'):
        self.counter += 1
        continue
      if(cmd[:-2] == 'if_enemy' and d.isEnemy()):
        self.counter = int(cmd[-1])
        continue
      if(cmd[:-2] == 'if_enemy'):
        self.counter += 1
        continue
      if(cmd[:-2] == 'if_random'):
        if(randrange(0,2)):
          self.counter = int(cmd[-1])
          continue
        else:
          self.counter += 1
          continue
      if(cmd[:-2] == 'go'):
        self.counter = int(cmd[-1])
        
    if(cmd == 'left'):
      self.left()
    elif(cmd == 'right'):
      self.right()
          
    return cmd
  def getDirection(self):
    '''
    Method to tell the game board which direction
    '''
    return self.direction
    
  def left (self) :
    '''
    Turn creature left
    '''
    if(self.direction == 'north'):
      self.direction = 'west'
    elif(self.direction == 'west'):
      self.direction = 'south'
    elif(self.direction == 'south'):
      self.direction = 'east'
    elif(self.direction == 'east'):
      self.direction = 'north'
    
  def right (self) :
    '''
    Turn creature right
    '''  
    if(self.direction == 'north'):
      self.direction = 'east'
    elif(self.direction == 'east'):
      self.direction = 'south'
    elif(self.direction == 'south'):
      self.direction = 'west'
    elif(self.direction == 'west'):
      self.direction = 'north'
  def getInfected(self,c):
    '''
    Takes in an infecting species. Infected creature then takes on the infecting creature's species and resets its counter to 0. 
    '''
    self.species = c.species
    self.counter = 0    
  def __str__(self):
    '''
    Returns token representation of creature
    '''
    return self.species.name[0]
                 
    