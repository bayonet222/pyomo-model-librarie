import pyomo.environ
from pyomo.core import *

model = AbstractModel()

# @decl:
model.A = Set()
model.B = Set(model.A)
# @:decl
model.C = Set(model.A,model.A)

instance = model.create('set3.dat')

#print(list(instance.A.data()))
print(sorted(list(instance.B[1].data())))
print(sorted(list(instance.B['aaa'].data())))