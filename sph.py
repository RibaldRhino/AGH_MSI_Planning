# from pyhop import *
import pyhop
import methods_and_operators

state0 = pyhop.State('state0')
state0.energy = 50
state0.knowledge = 10
state0.health = 50
state0.fed = 100
state0.backlog = 10
state0.sph_left = 100

pyhop.pyhop(state0, [('finish_thesis_task',)], verbose=2)