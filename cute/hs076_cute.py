#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2010 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the Pyomo README.txt file.
#  _________________________________________________________________________
#
#   Taken from cute suite. Formulated in Pyomo by Logan Barnes.

from pyomo.core import *
model = ConcreteModel()
model.N = RangeSet(1,4)
model.x = Var(model.N,initialize=0.5,within=NonNegativeReals)

model.obj = Objective(expr = model.x[1]**2 + 0.5*model.x[2]**2 + model.x[3]**2 + 0.5*model.x[4]**2\
     - model.x[1]*model.x[3] + model.x[3]*model.x[4]\
     - model.x[1] - 3*model.x[2] + model.x[3] - model.x[4])

model.constr1 = Constraint(expr = model.x[1] + 2.0*model.x[2] + model.x[3] + model.x[4] <= 5.0)
model.constr2 = Constraint(expr = 3.0*model.x[1] + model.x[2] + 2.0*model.x[3] - model.x[4] <= 4.0)
model.constr3 = Constraint(expr = model.x[2] + 4*model.x[3] >= 1.5)
