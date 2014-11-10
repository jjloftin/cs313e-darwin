from random import randrange, seed
import sys

from Darwin import Species, Creature, Darwin

f = Species('food')
f.addInstruction('left')
f.addInstruction('go 0')

h = Species('hopper')
h.addInstruction('hop')
h.addInstruction('go 0')

t = Species('trap')
t.addInstruction('if_enemy 3')
t.addInstruction('left')
t.addInstruction('go 0')
t.addInstruction('infect')
t.addInstruction('go 0')

r = Species('rover')
r.addInstruction('if_enemy 9')
r.addInstruction('if_empty 7')
r.addInstruction('if_random 5')
r.addInstruction('left')
r.addInstruction('go 0')
r.addInstruction('right')
r.addInstruction('go 0')
r.addInstruction('hop')
r.addInstruction('go 0')
r.addInstruction('infect')
r.addInstruction('go 0')


print('*** Darwin 8x8 ***')
seed(0)
d = Darwin(8,8)
c1 = Creature(f,'east')
d.add(c1,0,0)
c2 = Creature(h,'north')
d.add(c2,3,3)
d.add(Creature(h,'east'),3,4)
d.add(Creature(h,'south'),4,4)
d.add(Creature(h,'west'),4,3)
d.add(Creature(f,'north'),7,7)

for i in range(6):
  print('Turn = ' + str(d.turns) + '.')
  print(d)
  d.turn()

print('*** Darwin 7x9 ***')
seed(0)

d = Darwin(7,9)
d.add(Creature(t,'south'),0,0)
d.add(Creature(h,'east'),3,2)
d.add(Creature(r,'north'),5,4)
d.add(Creature(t,'west'),6,8)

for i in range(6):
  print('Turn = ' + str(d.turns) + ',')
  print(d)
  d.turn()

print('*** Darwin 72x72 without Best***')
seed(0)
d = Darwin(72,72)

for l in range(10):
  i = randrange(0,72)
  j = randrange(0,72)
  k = randrange(0,4)
  
  if k == 0:
    k = 'west'
  elif k == 1:
    k = 'north'
  elif k == 2:
    k = 'east'
  elif k == 3:
    k = 'south'
  
  d.add(Creature(f,k),i,j)  
for l in range(10):
  i = randrange(0,72)
  j = randrange(0,72)
  k = randrange(0,4)
  
  if k == 0:
    k = 'west'
  elif k == 1:
    k = 'north'
  elif k == 2:
    k = 'east'
  elif k == 3:
    k = 'south'
  
  d.add(Creature(h,k),i,j)  
for l in range(10):
  i = randrange(0,72)
  j = randrange(0,72)
  k = randrange(0,4)
  
  if k == 0:
    k = 'west'
  elif k == 1:
    k = 'north'
  elif k == 2:
    k = 'east'
  elif k == 3:
    k = 'south'
  
  d.add(Creature(r,k),i,j)    
for l in range(10):
  i = randrange(0,72)
  j = randrange(0,72)
  k = randrange(0,4)
  
  if k == 0:
    k = 'west'
  elif k == 1:
    k = 'north'
  elif k == 2:
    k = 'east'
  elif k == 3:
    k = 'south'
  
  d.add(Creature(t,k),i,j)  
  
for l in range(1001):
  if (l < 10 or l % 100 == 0):
    print('Turn = ' + str(d.turns) + ',')
    print(d)
  d.turn()