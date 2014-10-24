from MonteCarloExercise import energy,ChangeParticle,CompareEnergies
from nose.tools import assert_equal
from mock import Mock
from numpy import array, any, sum, exp, log

def test_energy_not_integer():
  """ Test for integer numbers"""
  # Test something
  # def f(x): return 0.5*x*(x-1)
  f = Mock(name="myroutine", return_value=2) 
  try:  energy(f,['i',2,1])
  except: pass
  else: raise AssertionError("non integers did not raise an error")
  
def test_energy_not_positive():
  """ Test for positive numbers """
  # Test something
  # def f(x): return 0.5*x*(x-1)
  f = Mock(name="myroutine", return_value=2) 
  try:  energy(f,[-5,2,1])
  except: pass
  else: raise AssertionError("negative number did not raise an error")
  
def test_energy_right():
  """ The right one """
  # Test something
  # def f(x): return 0.5*x*(x-1)
  f = Mock(name="myroutine", return_value=2) 
  v=[3,2,1]
  expected=6
  actual=energy(f,v)
  assert_equal(expected,actual)
  
def test_ChangeParticle_not_positive():
  """ Test for the positivity""" 
  try:  ChangeParticle([-5,2,1],0,0)# 0 is left and 1 is right.
  except: pass
  else: raise AssertionError("negative number did not raise an error")

  
def test_ChangeParticle_wrong_dimension():
  """ Test for the right dimension reference """
  try:  ChangeParticle([5,2,1],4,0)# 0 is left and 1 is right.
  except: pass
  else: raise AssertionError("wrong dimension reference did not raise an error")
  
def test_ChangeParticle_wrong_direction():
  """ Test for the right direction """
  try:  ChangeParticle([5,2,1],2,3)# 0 is left and 1 is right.
  except: pass
  else: raise AssertionError("wrong direction did not raise an error")

def test_ChangeParticle_move_right_the_last():
  """ Test for moving the last particle on the right """
  i = 2
  v=[5,2,1]
  direction=1 # 0 is left and 1 is right.
  expected=[6,2,0]
  actual=ChangeParticle(v,i,direction)
  #actual=[6,2,0]
  assert_equal(all(expected),all(actual))

def test_ChangeParticle_move_left_the_first():
  """ Test for moving the first particle on the left """
  i = 0
  v=[5,2,1]
  direction=0 # 0 is left and 1 is right.
  expected=[4,2,2]
  actual=ChangeParticle(v,i,direction)
  assert_equal(all(expected),all(actual))
 
def test_ChangeParticle_right():
  """ Test for moving non boundaries particles on the right """
  i = 0
  v=[5,2,1]
  direction=1 # 0 is left and 1 is right.
  expected=[4,3,1]
  actual=ChangeParticle(v,i,direction)
  assert_equal(all(expected),all(actual))

 
def test_CompareEnergies_T_negative():
 """ Test for positive temperature """
 E0=12
 E1=10
 T=-273
 p1=0.4
 try:  CompareEnergies(E0,E1,T,p1)
 except: pass
 else: raise AssertionError("negative T did not raise an error")

 
def test_CompareEnergies_E1_less_than_E0():
 """ Test in case E0>E1 """
 E0=12
 E1=10
 T=273
 p1=0.4
 expected=1
 actual=CompareEnergies(E0,E1,T,p1) 
 assert_equal(expected,actual)
 
def test_CompareEnergies_E1_equal_E0():
 """ Test in case E1=E0"""
 E0=10
 E1=10
 T=273
 p1=0.4
 expected=1
 actual=CompareEnergies(E0,E1,T,p1) 
 assert_equal(expected,actual)
 
def test_CompareEnergies_p0_greater_p1():
 """ Test in case p0>p1 """
 E0=10
 E1=12
 T=273
 p1=0.1
 expected=1
 actual=CompareEnergies(E0,E1,T,p1) 
 assert_equal(expected,actual)
 
 
def test_CompareEnergies_p1_equal_p0():
 """ Test in case p1=p0 """
 E0=10
 E1=11
 T=1/log(2)
 p1=0.5
 expected=0
 actual=CompareEnergies(E0,E1,T,p1) 
 assert_equal(expected,actual)
 
def test_CompareEnergies_p1_greater_p0():
 """ Test in case p1=p0"""
 E0=10
 E1=12
 T=1
 p1=0.4
 expected=0
 actual=CompareEnergies(E0,E1,T,p1) 
 assert_equal(expected,actual)