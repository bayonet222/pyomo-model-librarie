import pyomo.environ
from pyomo.core import *

model = AbstractModel()

# @decl:
model.A = Set()
model.B = Param(model.A)
# @:decl

instance = model.create('param2a.dat')

keys = instance.B.keys()
for key in sorted(keys):
    print(str(key)+" "+str(value(instance.B[key])))
