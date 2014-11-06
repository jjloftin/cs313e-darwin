#-------------
#TestDarwin.py
#-------------

from io import StringIO
from unittest import main, TestCase
from Darwin import Darwin, Species, Creature

class TestDarwin(TestCase):

  #Species
  def test_species1 (self):
    s = Species('dingo')
    self.assertEqual(s.name,'dingo')
  def test_species3 (self):  
    s = Species('dingo')
    self.assertEqual(s.instructions,[])
  def test_species4 (self):  
    s = Species('dingo')
    s.addInstruction('hop')
    self.assertEqual(s.instructions,['hop'])
  def test_species5(self):
    s = Species('dingo')
    s.addInstruction('hop')
    s.addInstruction('infect')
    self.assertEqual(s.instructions,['hop','infect']) 
  def test_species6(self):
    s = Species('dingo')
    s.addInstruction('hop')
    s.addInstruction('infect')
    s.addInstruction('hop')
    self.assertEqual(s.instructions,['hop','infect','hop'])

  #Darwin
  def test_darwin1(self):
    d = Darwin(2,2)
    self.assertEqual(d.world, [['.','.'],['.','.']])
  def test_darwin2(self):
    d = Darwin(1,1)
    self.assertEqual(d.world, [['.']])
    
  def test_darwin3(self):  
    d = Darwin(1,3)
    s = Species('cat')
    c1 = Creature(s,'south')
    c2 = Creature(s,'south')
    c3 = Creature(s,'south')
    d.add(c1,1,1)
    self.assertEqual(d.world,[['c','.','.']])
  def test_darwin4(self):  
    d = Darwin(1,3)
    s = Species('cat')
    c1 = Creature(s,'south')
    c2 = Creature(s,'south')
    c3 = Creature(s,'south')
    d.add(c1,1,1)
    d.add(c2,1,2)
    self.assertEqual(d.world,[['c','c','.']])
  def test_darwin5(self):  
    d = Darwin(1,3)
    s = Species('cat')
    c1 = Creature(s,'south')
    c2 = Creature(s,'south')
    c3 = Creature(s,'south')    
    d.add(c1,1,1)
    d.add(c2,1,2)
    d.add(c2,1,3)
    self.assertEqual(d.world,[['c','c','c']])
    
  def test_darwin6(self):
    d = Darwin(2,2)
    s = Species('dog')
    s.addInstruction('hop')
    c = Creature(s,'south')
    d.add(c,2,1)
  def test_darwin7(self):
    d = Darwin(2,2)
    s = Species('dog')
    c = Creature(s,'south')
    d.add(c,2,1)
  def test_darwin8(self):
    d = Darwin(2,2)
    s = Species('dog')
    c = Creature(s,'south')
    
  def test_darwin9(self):
    pass
  def test_darwin10(self):
    pass
  def test_darwin11(self):
    pass
  #Creature
  
main()
  