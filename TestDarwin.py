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
    
    self.assertEqual(c.turns, 0)
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
    cmd = c.excute()
    
    self.assertEqual(c.counter,1)
  def test_creature5(self):
    s = Species('cat')
    s.addInstruction('hop')
    s.addInstruction('infect')
    c = Creature(s,'north')
    c.execute()
    cmd = c.excute()
    
    self.assertEqual(cmd, 'infect')
  def test_creature6(self):
    s = Species('cat')
    s.addInstruction('hop')
    s.addInstruction('infect')
    c = Creature(s,'north')
    c.excute()
    c.execute()
    
    self.assertEqual(c.counter,2)  
    
  #Darwin
  def test_darwin1(self):
    d = Darwin(2,2)
    self.assertEqual(str(d), '  01\n0 ..\n1 ..')
  def test_darwin2(self):
    d = Darwin(1,1)
    self.assertEqual(str(d),'  0\n0 .')
  
  #add  
  def test_darwin3(self):  
    d = Darwin(1,3)
    s = Species('cat')
    c1 = Creature(s,'south')
    c2 = Creature(s,'south')
    c3 = Creature(s,'south')
    d.add(c1,0,0)
    self.assertEqual(str(d),'  012\n0 c . .')
  def test_darwin4(self):  
    d = Darwin(1,3)
    s = Species('cat')
    c1 = Creature(s,'south')
    c2 = Creature(s,'south')
    c3 = Creature(s,'south')
    d.add(c1,0,0)
    d.add(c2,0,1)
    self.assertEqual(str(d),'  012\n0 c c .')
  def test_darwin5(self):  
    d = Darwin(1,3)
    s = Species('cat')
    c1 = Creature(s,'south')
    c2 = Creature(s,'south')
    c3 = Creature(s,'south')    
    d.add(c1,0,0)
    d.add(c2,0,1)
    d.add(c2,0,2)
    self.assertEqual(str(d), '  0123\n0 c c c')
    
  #go
  def test_darwin6(self):
    d = Darwin(2,2)
    s = Species('dog')
    s.addInstruction('hop')
    c = Creature(s,'south')
    d.add(c,1,0)
    d.go(1,0)
    self.assertEqual(str(d),'  01\n0 ..\n1 d.')
  def test_darwin7(self):
    d = Darwin(2,2)
    s = Species('dog')
    c = Creature(s,'north')
    d.add(c,1,0)
    d.go(1,0)
    self.assertEqual(str(d),'  01\n0 d.\n1 ..')
  def test_darwin8(self):
    d = Darwin(2,2)
    s = Species('dog')
    c = Creature(s,'south')
    d.add(c,1,0)
    d.go(1,1)
    self.assertEqual(str(d),'  01\n0 ..\n1 d.')
  
  #turn  
  def test_darwin9(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    c = Creature(s, 'east')
    d.add(c,0,0)
    d.turn()
    assert 1 == 2
    self.assertEqual(d.turns, 1)    
  def test_darwin10(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    c = Creature(s, 'east')
    d.add(c,0,0)
    d.turn()
    self.assertEqual(str(d),'  01\n0 . c')
  
  #isEmpty    
  def test_darwin11(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'east')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(True,d.isEmpty(c))
  def test_darwin12(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'south')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(False,d.isEmpty(c))
  def test_darwin13(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'west')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(False, d.isEmpty(c))
    
  #isWall
  def test_darwin14(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'west')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(True,d.isWall(c))
  def test_darwin15(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'south')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(True,d.isWall(c))
  def test_darwin16(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'east')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(False,d.isWall(c))
    
  #isEnemy
  def test_darwin17(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    c = Creature(s,'south')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(False,d.isEnemy(c))
  def test_darwin18(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    c = Creature(s,'east')
    c1 = Creature(s,'east')
    d.add(c,0,0)
    d.add(c,0,1)
    d.go(0,0)
    self.assertEqual(False,d.isEnemy(c))
  def test_darwin19(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    c = Creature(s,'east')
    d.add(c,0,0)
    d.go(0,0)
    self.assertEqual(False,d.isEnemy(c))  
  def test_darwin20(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    s1 = Species('dog')
    s1.addInstruction('hop')
    c = Creature(s,'east')
    c1 = Creature(s1,'east')
    d.add(c,0,0)
    d.add(c,0,1)
    d.go(0,0)
    self.assertEqual(True,d.isEnemy(c))     
    
  #hop
  def test_darwin21(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'east')
    d.add(c,0,0)
    d.go(0,0)
    
    d.hop(c)
    self.assertEqual(str(d), '  01\n0 . c')
  def test_darwin22(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'west')
    d.add(c,0,0)
    d.go(0,0)
    
    d.hop(c)
    self.assertEqual(str(d), '  01\n c .')
  def test_darwin23(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'south')
    d.add(c,0,0)
    d.go(0,0)
    
    d.hop(c)
    self.assertEqual(str(d), '  01\n c .')
    
  #left
  def test_darwin24(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'south')
    d.add(c,0,0)
    d.go(0,0)
    
    d.left(c)
    self.assertEqual('east', c.direction)  
  def test_darwin25(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'east')
    d.add(c,0,0)
    d.go(0,0)
    
    d.left(c)
    self.assertEqual('north',c.direction)
  def test_darwin26(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'north')
    d.add(c,0,0)
    d.go(0,0)
    
    d.left(c)
    self.assertEqual('west',c.direction)
  def test_darwin27(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'west')
    d.add(c,0,0)
    d.go(0,0)
    
    d.left(c)
    self.assertEqual('south',c.direction)
  
  #right
  def test_darwin28(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'south')
    d.add(c,0,0)
    d.go(0,0)
    
    d.right(c)
    self.assertEqual('west', c.direction)  
  def test_darwin29(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'west')
    d.add(c,0,0)
    d.go(0,0)
    
    d.right(c)
    self.assertEqual('north',c.direction)
  def test_darwin30(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'north')
    d.add(c,0,0)
    d.go(0,0)
    
    d.right(c)
    self.assertEqual('east',c.direction)
  def test_darwin31(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('infect')
    c = Creature(s,'east')
    d.add(c,0,0)
    d.go(0,0)
    
    d.right(c)
    self.assertEqual('south',c.direction)
  
  #infect
  def test_darwin32(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    c = Creature(s,'east')
    c1 = Creature(s,'east')
    d.add(c,0,0)
    d.add(c,0,1)
    d.go(0,0)
    
    d.infect(c)
    self.assertEqual(str(d), '  01\n c c')
  def test_darwin33(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    c = Creature(s,'north')
    d.add(c,0,0)
    d.go(0,0)
    
    d.right(c)
    d.infect(c)
    self.assertEqual(str(d),'  01\n c .')  
  def test_darwin34(self):
    d = Darwin(1,2)
    s = Species('cat')
    s.addInstruction('hop')
    s1 = Species('dog')
    s1.addInstruction('hop')
    c = Creature(s,'east')
    c1 = Creature(s1,'east')
    d.add(c,0,0)
    d.add(c,0,1)
    d.go(0,0)
    
    d.infect(c)
    self.assertEqual(str(d),'  01\n c c')  
 
    

main()
  