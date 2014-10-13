import logging
from pyomo.core import *

model = ConcreteModel()

model.x = Var([1,2], initialize=1.0)

# @decl1:
model.Diff= Constraint(expr=model.x[2]-model.x[1] <= 7.5)
# @:decl1
model.del_component('Diff')

# @decl2:
def Diff_rule(model):
    return model.x[2] - model.x[1] <= 7.5
model.Diff = Constraint()
# @:decl2

# @decl3:
N = [1,2,3]

a = {1:1, 2:3.1, 3:4.5}
b = {1:1, 2:2.9, 3:3.1}

model.y = Var(N, within=NonNegativeReals, initialize=0.0)

def CoverConstr_rule(model, i):
    return a[i] * model.y[i] >= b[i]
model.CoverConstr= Constraint(N)
# @:decl3

# @decl4:
def CapacityIneq_rule(model, i):
    return (0.25, (a[i] * model.y[i])/b[i], 1.0)
model.CapacityIneq = Constraint(N)
# @:decl4

# @decl5:
def CapacityEq_rule(model, i):
    return (0, a[i] * model.y[i] - b[i])
model.CapacityEq = Constraint(N)
# @:decl5

# @decl6:
TimePeriods = [1,2,3,4,5]
LastTimePeriod = 5

model.StartTime = Var(TimePeriods, initialize=1.0)

def Pred_rule(model, t):
    if t == LastTimePeriod:
        return Constraint.Skip
    else:
        return model.StartTime[t] <= model.StartTime[t+1]

model.Pred = Constraint(TimePeriods)
# @:decl6

logging.disable(logging.ERROR)
# @decl7a:
model.EMPTY = Set()
model.z = Var(model.EMPTY)

@simple_constraint_rule
def C2_rule(model, i):
    if i == 1:
        return summation(model.z) < 1
    if i == 2:
        return summation(model.z) < -1
    return None

try:
    model.C2 = Constraint([1,2,3])
except:
    pass
# @:decl7a

# @decl7b:
def C1_rule(model, i):
    if i == 1:
        return Constraint.Feasible
    if i == 2:
        return Constraint.Infeasible
    return Constraint.Skip

try:
    model.C1 = Constraint([1,2,3])
except:
    pass
# @:decl7b
logging.disable(logging.NOTSET)

model.display()