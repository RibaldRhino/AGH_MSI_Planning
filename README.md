## HTN Planning ##
## Help me plan how to finish my engineers thesis as fast as possible ##

This project aims to show a simple example of HTN planning using pyhop.

## Summary ##

I have to finish my engineers theses. However, I have to remember that:
1) I have a lot of other work. When I'm not doing it then it stacks and at a certain point it becomes crucial that I
take care of it.
2) I don't want my health to get ruined because of all the computer work. Visiting the gym from time to time i
necessary.
3) I can't work when I'm hungry.
4) all this work will make me really tired. I have to relax from time to time.
5) I can't do all the work in one go. I don't have the knowledge required. However each time I sit down and do some
work I gain some knowledge which helps me in the future.

## Domain ##

It is crucial that I maintain the following resources:
* Energy
* Health
* Fed
And keep them at decent levels

* Knowledge - Helps me do my thesis quicker
* Backlog - The amount of tasks I have to do besides my thesis (shouldn't be larger than 10)
* SPH_Left - How much work on my thesis is left

The initial state is defined in sph.py. Methods, operators and constants are defines in methods_and_operators.py.
Modifying any one of them can change the output significantly.

## Example ##

```python
def gym_task_1(state):
  if state.fed >= WORK_FED_REQ:
    return [('gym',)]
  else:
    return False


def gym_task_2(state):
  if state.fed < WORK_FED_REQ:
    return [('eat_task',), ('gym_task',)]
  else:
    return False

pyhop.declare_methods('gym_task', gym_task_1, gym_task_2)

def gym(state):
  if state.fed >= WORK_FED_REQ:
    state.health = state.health + HEALTH_VAL
    state.energy = state.energy - WORK_ENERGY_COST
    state.fed = state.fed - WORK_FOOD_COST
    state.backlog = state.backlog + BACKLOG_INCREMENT_VAL
    return state
  return False

```

## Example output ##

depth 0 tasks [('finish_thesis_task',)]
depth 1 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 2 tasks [('write_other_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 3 tasks [('write_other',), ('write_sph_task',), ('finish_thesis_task',)]
depth 4 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 5 tasks [('relax_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 6 tasks [('relax',), ('write_sph_task',), ('finish_thesis_task',)]
depth 7 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 8 tasks [('write_sph',), ('study_task',), ('finish_thesis_task',)]
depth 9 tasks [('study_task',), ('finish_thesis_task',)]
depth 10 tasks [('study',), ('finish_thesis_task',)]
depth 11 tasks [('finish_thesis_task',)]
depth 12 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 13 tasks [('eat_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 14 tasks [('eat',), ('write_sph_task',), ('finish_thesis_task',)]
depth 15 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 16 tasks [('gym_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 17 tasks [('gym',), ('write_sph_task',), ('finish_thesis_task',)]
depth 18 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 19 tasks [('write_other_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 20 tasks [('write_other',), ('write_sph_task',), ('finish_thesis_task',)]
depth 21 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 22 tasks [('relax_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 23 tasks [('relax',), ('write_sph_task',), ('finish_thesis_task',)]
depth 24 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 25 tasks [('write_sph',), ('study_task',), ('finish_thesis_task',)]
depth 26 tasks [('study_task',), ('finish_thesis_task',)]
depth 27 tasks [('study',), ('finish_thesis_task',)]
depth 28 tasks [('finish_thesis_task',)]
depth 29 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 30 tasks [('eat_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 31 tasks [('eat',), ('write_sph_task',), ('finish_thesis_task',)]
depth 32 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 33 tasks [('gym_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 34 tasks [('gym',), ('write_sph_task',), ('finish_thesis_task',)]
depth 35 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 36 tasks [('relax_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 37 tasks [('relax',), ('write_sph_task',), ('finish_thesis_task',)]
depth 38 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 39 tasks [('write_other_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 40 tasks [('write_other',), ('write_sph_task',), ('finish_thesis_task',)]
depth 41 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 42 tasks [('write_sph',), ('study_task',), ('finish_thesis_task',)]
depth 43 tasks [('study_task',), ('finish_thesis_task',)]
depth 44 tasks [('eat_task',), ('study_task',), ('finish_thesis_task',)]
depth 45 tasks [('eat',), ('study_task',), ('finish_thesis_task',)]
depth 46 tasks [('study_task',), ('finish_thesis_task',)]
depth 47 tasks [('study',), ('finish_thesis_task',)]
depth 48 tasks [('finish_thesis_task',)]
depth 49 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 50 tasks [('relax_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 51 tasks [('relax',), ('write_sph_task',), ('finish_thesis_task',)]
depth 52 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 53 tasks [('write_other_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 54 tasks [('write_other',), ('write_sph_task',), ('finish_thesis_task',)]
depth 55 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 56 tasks [('gym_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 57 tasks [('gym',), ('write_sph_task',), ('finish_thesis_task',)]
depth 58 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 59 tasks [('eat_task',), ('write_sph_task',), ('finish_thesis_task',)]
depth 60 tasks [('eat',), ('write_sph_task',), ('finish_thesis_task',)]
depth 61 tasks [('write_sph_task',), ('finish_thesis_task',)]
depth 62 tasks [('write_sph',), ('study_task',), ('finish_thesis_task',)]
depth 63 tasks [('study_task',), ('finish_thesis_task',)]
depth 64 tasks [('study',), ('finish_thesis_task',)]
depth 65 tasks [('finish_thesis_task',)]
depth 66 tasks [('finish_thesis',)]
depth 67 tasks []
** result = [('write_other',), ('relax',), ('write_sph',), ('study',), ('eat',), ('gym',), ('write_other',),
('relax',), ('write_sph',), ('study',), ('eat',), ('gym',), ('relax',), ('write_other',), ('write_sph',), ('eat',),
('study',), ('relax',), ('write_other',), ('gym',), ('eat',), ('write_sph',), ('study',), ('finish_thesis',)]
