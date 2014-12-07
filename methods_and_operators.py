import pyhop

WORK_ENERGY_REQ = 30
WORK_FED_REQ = 20
WORK_HEALTH_REQ = 10
WORK_ENERGY_COST = 30
WORK_FOOD_COST = 30
WORK_HEALTH_COST = 20
BACKLOG_REDUCE_VAL = 10
BACKLOG_INCREMENT_VAL = 2
STUDY_VAL = 10
FED_VAL = 100
RELAX_VAL = 100
HEALTH_VAL = 100


def finish_thesis_task_1(state):
  if state.sph_left <= 0:
    return [('finish_thesis',)]
  return False


def finish_thesis_task_2(state):
  if state.sph_left > 0:
    return [('write_sph_task',), ('finish_thesis_task',)]
  return False


pyhop.declare_methods('finish_thesis_task', finish_thesis_task_1, finish_thesis_task_2)


def write_sph_task_1(state):
  if state.energy >= WORK_ENERGY_REQ and state.fed >= WORK_FED_REQ and state.health >= WORK_HEALTH_REQ and state.backlog < BACKLOG_REDUCE_VAL:
    return [('write_sph', ), ('study_task', )]
  return False


def write_sph_task_2(state):
  if state.energy < WORK_ENERGY_REQ:
    return [('relax_task',), ('write_sph_task',)]
  else:
    return False


def write_sph_task_3(state):
  if state.fed < WORK_FED_REQ:
    return [('eat_task',), ('write_sph_task',)]
  else:
    return False


def write_sph_task_4(state):
  if state.health < WORK_HEALTH_REQ:
    return [('gym_task',), ('write_sph_task',)]
  return False


def write_sph_task_5(state):
  if state.backlog >= BACKLOG_REDUCE_VAL:
    return [('write_other_task',), ('write_sph_task',)]
  return False


pyhop.declare_methods('write_sph_task', write_sph_task_1, write_sph_task_2, write_sph_task_3, write_sph_task_4, write_sph_task_5)


def write_other_task_1(state):
  if state.energy >= WORK_ENERGY_REQ and state.fed >= WORK_FED_REQ and state.health >= WORK_HEALTH_REQ:
    return [('write_other',)]
  return False


def write_other_task_2(state):
  if state.energy < WORK_ENERGY_REQ:
    return [('relax_task',), ('write_other_task',)]
  else:
    return False


def write_other_task_3(state):
  if state.fed < WORK_FED_REQ:
    return [('eat_task',), ('write_other_task',)]
  else:
    return False


def write_other_task_4(state):
  if state.health < WORK_HEALTH_REQ:
    return [('gym_task',), ('write_other_task',)]
  return False


pyhop.declare_methods('write_other_task', write_other_task_1, write_other_task_2, write_other_task_3,
                      write_other_task_4)


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


def eat_task_1(state):
  return [('eat',)]


pyhop.declare_methods('eat_task', eat_task_1)


def relax_task_1(state):
  return [('relax',)]


pyhop.declare_methods('relax_task', relax_task_1)


def study_task_1(state):
  if state.fed >= WORK_FED_REQ and state.energy >= WORK_ENERGY_REQ:
    return [('study',)]
  return False


def study_task_2(state):
  if state.fed < WORK_FED_REQ:
    return [('eat_task',), ('study_task',)]
  return False


def study_task_3(state):
  if state.energy < WORK_ENERGY_REQ:
    return [('relax_task',), ('study_task',)]
  return False


pyhop.declare_methods('study_task', study_task_1, study_task_2, study_task_3)

# operators

def finish_thesis(state):
  if state.sph_left <= 0:
    return state
  return False

def write_sph(state):
  if state.energy >= WORK_ENERGY_REQ and state.fed >= WORK_FED_REQ and state.health >= WORK_HEALTH_REQ and state.backlog < BACKLOG_REDUCE_VAL:
    state.energy = state.energy - WORK_ENERGY_COST
    state.fed = state.fed - WORK_FOOD_COST
    state.health = state.health - WORK_HEALTH_COST
    state.backlog = state.backlog + BACKLOG_INCREMENT_VAL
    state.sph_left = state.sph_left - state.knowledge
    state.backlog = state.backlog + BACKLOG_INCREMENT_VAL
    return state
  else:
    return False


def write_other(state):
  if state.energy >= WORK_ENERGY_REQ and state.fed >= WORK_FED_REQ and state.health >= WORK_HEALTH_REQ:
    state.energy = state.energy - WORK_ENERGY_COST
    state.fed = state.fed - WORK_FOOD_COST
    state.health = state.health - WORK_HEALTH_COST
    state.backlog = state.backlog - BACKLOG_REDUCE_VAL
    return state
  return False


def study(state):
  if state.fed >= WORK_FED_REQ and state.energy >= WORK_ENERGY_REQ:
    state.knowledge = state.knowledge + STUDY_VAL
    state.fed = state.fed - WORK_FOOD_COST
    state.energy = state.energy - WORK_ENERGY_COST
    state.health = state.health - WORK_HEALTH_COST
    return state
  else:
    return False


def eat(state):
  state.fed = state.fed + FED_VAL
  state.health = state.health - WORK_HEALTH_COST
  state.backlog = state.backlog + BACKLOG_INCREMENT_VAL
  return state


def relax(state):
  state.energy = state.energy + RELAX_VAL
  state.backlog = state.backlog + BACKLOG_INCREMENT_VAL
  return state


def gym(state):
  if state.fed >= WORK_FED_REQ:
    state.health = state.health + HEALTH_VAL
    state.energy = state.energy - WORK_ENERGY_COST
    state.fed = state.fed - WORK_FOOD_COST
    state.backlog = state.backlog + BACKLOG_INCREMENT_VAL
    return state
  return False


pyhop.declare_operators(finish_thesis, write_sph, write_other, study, eat, relax, gym)
