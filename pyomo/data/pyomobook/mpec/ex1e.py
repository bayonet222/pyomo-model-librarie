# file ex1e.py

from pyomo.environ import *
from pyomo.mpec import *

n = 5

model = ConcreteModel()

model.x = Var( range(1,n+1) )

model.f = Objective( expr=sum(i*(model.x[i]-1)**2 for i in range(1,n+1)) )

model.compl = ComplementarityList(
    rule=(complements(model.x[i] >= 0, model.x[i+1] >= 0) for i in range(1,n)) )
