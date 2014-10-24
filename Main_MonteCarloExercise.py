from MonteCarloExercise import energy,ChangeParticle,CompareEnergies 
from numpy import array, any, sum, exp, log
import random
density0=[5,2,4,5,1,2,3]
d = len(density0)
i = random.randint(0,d-1)
direction=random.randint(0,1)
T=273,5
p1=random.random()

def f(density): 
 return 0.5 * sum(density * (density-1))

E0=energy(f(density0),density0)
density1=ChangeParticle(density0,i,direction)
E1=energy(f(density1),density1)

CompareEnergies(E0,E1,T,p1)