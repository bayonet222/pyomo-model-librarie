import pyomo.modeling
from pyomo.core import *

# @model:
model = ConcreteModel()
# @:model

# @var:
model.x_1 = Var(within=NonNegativeReals)
model.x_2 = Var(within=NonNegativeReals)
# @:var

# @obj:
model.obj = Objective(expr=model.x_1 + 2*model.x_2)
# @:obj

# @con:
model.con1 = Constraint(expr=3*model.x_1 + 4*model.x_2 >= 1)
model.con2 = Constraint(expr=2*model.x_1 + 5*model.x_2 >= 2)
# @:con
