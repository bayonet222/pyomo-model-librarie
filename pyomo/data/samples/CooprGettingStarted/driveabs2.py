# driveabs2.py
from __future__ import division
from pyomo.core import *
from pyomo.opt import SolverFactory

# Create a solver
opt = SolverFactory('cplex')

# get the model from another file
from abstract2 import model

# Create a model instance and optimize
instance = model.create('abstract2.dat')

# Create a 'dual' suffix component on the instance
# so the solver plugin will know which suffixes to collect
instance.dual = Suffix(direction=Suffix.IMPORT)

results = opt.solve(instance)

# get the results back into the instance for easy access
instance.load(results)

# display all duals
print "Duals"
from pyomo.core import Constraint
for c in instance.active_components(Constraint):
    print "   Constraint",c
    cobject = getattr(instance, c)
    for index in cobject:
        print "      ", index, instance.dual[cobject[index]]

# access (display, this case) one dual
print "Dual for Film=", instance.dual[instance.AxbConstraint['Film']]

