import pyomo.modeling
from pyomo.core import *

model = AbstractModel()

model.A = Set()

instance = model.create('import3.tab.dat')

print('A '+str(sorted(list(instance.A.data()))))
