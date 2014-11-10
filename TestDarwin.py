#-------------
#TestDarwin.py
#-------------

from io import StringIO
from unittest import main, TestCase
from Darwin import Darwin, Species, Creature

class TestDarwin(TestCase):

  #Species
  
  #basics
  def test_species1 (self):
    s = Species('dingo')
    self.assertEqual(s.name,'dingo')
  def test_species2 (self):  
    s = Species('dingo')
    self.assertEqual(s.instructions,[])
  
  #addInstruction
  def test_species3 (self):  
    s = Species('dingo')
    s.addInstruction('hop')
    self.assertEqual(s.instructions,['hop'])
  def test_species4(self):
    s = Species('dingo')
    s.addInstruction('hop')
    s.addInstruction('infect')
    self.assertEqual(s.instructions,['hop','infect']) 
  def test_species5(self):
    s = Species('dingo')
    s.addInstruction('hop')
    s.addInstruction('infect')
    s.addInstruction('hop')
    self.assertEqual(s.instructions,['hop','infect','hop'])
  
  #Creature
  
  #basics
  def test_creature1(self):
    s = Species('cat')
    s.addInstruction('hop')
    s.addInstruction('infect')
    c = Creature(s,'north')
    
    self.assertEqual(c.counter, 0)
  def test_creature2(self):
    s = Species('cat')
    s.addInstruction('hop')
    s.addInstruction('infect')
    c = Creature(s,'north')
    
    self.assertEqual(c.direction, 'north')

  
  #execute
  def test_creature3(self):
    s = Species('cat')
    s.addInstruction('hop')
    s.addInstruction('infect')
    c = Creature(s,'north')
    cmd = c.execute()  
    self.assertEqual(cmd, 'hop')
  def test_creature4(self):
    s = Species('cat')
    s.addInstruction('hop')
    s.addInstruction('infect')
    c = Creature(s,'north')
    cmd = c.execute()
    
    self.assertEqual(c.counter,1)
  def test_creature5(self):
    s = Species('cat')
    s.addInstruction('hop')
    s.addInstruction('infect')
    c = Creature(s,'north')
    c.execute()
    cmd = c.execute()
    
    self.assertEqual(cmd, 'infect')
  def test_creature6(self):
    s = Species('cat')
    s.addInstruction('hop')
    s.addInstruction('infect')
    c = Creature(s,'north')
    c.execute()
    c.execute()
    
    self.assertEqual(c.counter,2)  
  #left
  def test_creature7(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'south')
    d.add(c,0,0)
    d.go(0,0)
    
    c.left()
    self.assertEqual('east', c.direction)  
  def test_creature8(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'east')
    d.add(c,0,0)
    d.go(0,0)
    
    c.left()
    self.assertEqual('north',c.direction)
  def test_creature9(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'north')
    d.add(c,0,0)
    d.go(0,0)
    
    c.left()
    self.assertEqual('west',c.direction)
  def test_creature10(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'west')
    d.add(c,0,0)
    d.go(0,0)
    
    c.left()
    self.assertEqual('south',c.direction)
  
  #right
  def test_creature11(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'south')
    d.add(c,0,0)
    d.go(0,0)
    
    c.right()
    self.assertEqual('west', c.direction)  
  def test_creature12(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'west')
    d.add(c,0,0)
    d.go(0,0)
    
    c.right()
    self.assertEqual('north',c.direction)
  def test_creature13(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'north')
    d.add(c,0,0)
    d.go(0,0)
    
    c.right()
    self.assertEqual('east',c.direction)
  def test_creature14(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'east')
    d.add(c,0,0)
    d.go(0,0)
    
    c.right()
    self.assertEqual('south',c.direction)
    
  #getInfected
  
  def test_creature15(self):
    s = Species('dog')
    c = Creature('dog','east')
    c.counter = 3
    s1 = Species('cat')
    c1 = Creature(s1, 'north')
    
    c.getInfected(c1)
    self.assertEqual(c.direction,'east')
  def test_creature16(self):
    s = Species('dog')
    c = Creature('dog','east')
    c.counter = 3
    s1 = Species('cat')
    c1 = Creature(s1, 'north')
    
    c.getInfected(c1)
    self.assertEqual(c.counter,0)
  def test_creature17(self):
    s = Species('dog')
    c = Creature('dog','east')
    c.counter = 3
    s1 = Species('cat')
    c1 = Creature(s1, 'north')
    
    c.getInfected(c1)
    self.assertEqual(c.species.name,c1.species.name)
  #execute again
  def test_creature18(self):
    s = Species('dog')
    c = Creature(s,'east')
    s.addInstruction('hop')
    s.addInstruction('if_enemy 2')
    s.addInstruction('if_empty 3')
    s.addInstruction('if_random 4')
    s.addInstruction('go 0')
    d = Darwin(2,2)
    d.add(c,0,0)
    d.go(0,0)
    cmd = c.execute()
    self.assertEqual(cmd, 'hop')
  #Darwin
  def test_darwin1(self):
    d = Darwin(2,2)
    self.assertEqual(str(d), '  01\n0 ..\n1 ..\n')
  def test_darwin2(self):
    d = Darwin(1,1)
    self.assertEqual(str(d),'  0\n0 .\n')
  
  #add  
  def test_darwin3(self):  
    d = Darwin(1,3)
    s = Species('cat')
    c1 = Creature(s,'south')
    c2 = Creature(s,'south')
    c3 = Creature(s,'south')
    d.add(c1,0,0)
    self.assertEqual(str(d),'  012\n0 c..\n')
  def test_darwin4(self):  
    d = Darwin(1,3)
    s = Species('cat')
    c1 = Creature(s,'south')
    c2 = Creature(s,'south')
    c3 = Creature(s,'south')
    d.add(c1,0,0)
    d.add(c2,0,1)
    self.assertEqual(str(d),'  012\n0 cc.\n')
  def test_darwin5(self):  
    d = Darwin(1,3)
    s = Species('cat')
    c1 = Creature(s,'south')
    c2 = Creature(s,'south')
    c3 = Creature(s,'south')    
    d.add(c1,0,0)
    d.add(c2,0,1)
    d.add(c2,0,2)
    self.assertEqual(str(d), '  012\n0 ccc\n')
    
  #go - hop
  def test_darwin6(self):
    d = Darwin(2,2)
    s = Species('dog')
    s.addInstruction('hop')
    c = Creature(s,'south')
    d.add(c,0,1)
    d.go(0,1)
    self.assertEqual(str(d),'  01\n0 ..\n1 .d\n')
  def test_darwin7(self):
    d = Darwin(2,2)
    s = Species('dog')
    s.addInstruction('hop')
    c = Creature(s,'north')
    d.add(c,0,1)
    d.go(0,1)
    self.assertEqual(str(d),'  01\n0 .d\n1 ..\n')
  def test_darwin8(self):
    d = Darwin(2,2)
    s = Species('dog')
    c = Creature(s,'south')
    d.add(c,0,1)
    d.go(0,0)
    self.assertEqual(str(d),'  01\n0 .d\n1 ..\n')
  
  #turn  
  def test_darwin9(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    c = Creature(s, 'east')
    d.add(c,0,0)
    d.turn()
    self.assertEqual(d.turns, 1)    
  def test_darwin10(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    c = Creature(s, 'east')
    d.add(c,0,0)
    d.turn()
    self.assertEqual(str(d),'  01\n0 .c\n')
  
  #isEmpty    
  def test_darwin11(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'east')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(True,d.isEmpty())
  def test_darwin12(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'south')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(False,d.isEmpty())
  def test_darwin13(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'west')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(False, d.isEmpty())
    
  #isWall
  def test_darwin14(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'west')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(True,d.isWall())
  def test_darwin15(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'south')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(True,d.isWall())
  def test_darwin16(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'east')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(False,d.isWall())
    
  #isEnemy
  def test_darwin17(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    c = Creature(s,'south')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(False,d.isEnemy())
  def test_darwin18(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    c = Creature(s,'east')
    c1 = Creature(s,'east')
    d.add(c,0,0)
    d.add(c,0,1)
    d.go(0,0)
    self.assertEqual(False,d.isEnemy())
  def test_darwin19(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    c = Creature(s,'east')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(False,d.isEnemy())  
  def test_darwin20(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    s1 = Species('dog')
    s1.addInstruction('hop')
    c = Creature(s,'east')
    c1 = Creature(s1,'east')
    d.add(c,0,0)
    d.add(c1,0,1)
    d.go(0,0)
    self.assertEqual(True,d.isEnemy()) 

  #go- infect
  def test_darwin21(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'east')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(str(d), '  01\n0 c.\n')
  def test_darwin22(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'east')
    d.add(c,0,0)
    s1 = Species('dog')
    c1 = Creature(s,'east')
    d.add(c,0,1)
    d.go(0,0)
    self.assertEqual(str(d), '  01\n0 cc\n')
  def test_darwin23(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'east')
    d.add(c,0,0)
    c1 = Creature(s,'east')
    d.add(c,1,0)
    d.go(0,0)
    assert c != c1
 
    

main()
  