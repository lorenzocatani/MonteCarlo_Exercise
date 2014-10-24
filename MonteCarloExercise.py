from numpy import array, any, sum, exp, log
  
def energy(f,density):
  density = array(density)
  if density.dtype.kind != 'i' and len(density) > 0:
    raise TypeError ("Expected array of *integers*.")
  if any (density < 0):
    raise ValueError ("Expected array of *positive* integers.")
  E=0
  for element in density:
	   E = f(element) + E   
  return E
  
def ChangeParticle(density,i,direction):
  density = array(density)
  if density[i]<0:
    raise ValueError("No more particles in this box!") # In case you use it more times and you have boxes with zero particles.
  if i<0 or i>(len(density)-1):
    raise ValueError("i has to refer to one element of the density array")
  if direction!=0 and direction!=1:
    raise ValueError("Direction has to be either 0=left or 1=right")
  density[i] = density[i]-1 # Move a particle from the i-th position.
  d=len(density) 
  if i==d-1 and direction==1: density[0]=density[0]+1
  elif i==0 and direction==0: density[d-1]=density[d-1]+1
  elif direction==0 : density[i-1]= density[i-1]+1 # Particle moved on the left
  else : density[i+1]=density[i+1]+1 # Particle moved on the right
  return density

def CompareEnergies(E0,E1,T,p1):
  if T<=0:
    raise ValueError("T is a positive quantity!")
  p0=exp((E0-E1)/T)
  if E0>E1: return 1 # 1 means to accept
  elif p0>p1 : return 1
  else: return 0