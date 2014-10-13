from pyomo.core import *
from pyutilib.misc import Options

model = AbstractModel()

model.S_SI = Set(ordered=True)

model.P_REP_CASES = Param(model.S_SI)
model.P_POP = Param()

model.I = Var(model.S_SI, bounds=(0,model.P_POP), initialize=1)
model.S = Var(model.S_SI, bounds=(0,model.P_POP), initialize=300)
model.beta = Var(bounds=(0.05, 70))
model.alpha = Var(bounds=(0.5, 1.5))
model.eps_I = Var(model.S_SI, initialize=0.0)

def _objective(model):
    return sum((model.eps_I[i])**2 for i in model.S_SI)
model.objective = Objective(rule=_objective, sense=minimize)

def _InfDynamics(model, i):
    if i != 1:
        return model.I[i] == (model.beta * model.S[i-1] * model.I[i-1]**model.alpha)/model.P_POP
    return Constraint.Skip
model.InfDynamics = Constraint(model.S_SI, rule=_InfDynamics)

def _SusDynamics(model, i):
    if i != 1:
        return model.S[i] == model.S[i-1] - model.I[i]
    return Constraint.Skip
model.SusDynamics = Constraint(model.S_SI, rule=_SusDynamics)

def _Data(model, i):
    return model.P_REP_CASES[i] == model.I[i]+model.eps_I[i]
model.Data = Constraint(model.S_SI, rule=_Data)

# @script:
instance = model.create('DiseaseEstimation.dat');

options = Options()
options.solver = 'ipopt'
options.quiet = True

# solve the problem
results, opt = scripting.util.apply_optimizer(options, instance)

# load the results to plot the solution
instance.load(results)
est_incidence = []
act_incidence = []
for i in instance.S_SI:
    est_incidence.append(value(instance.I[i]))
    act_incidence.append(value(instance.P_REP_CASES[i]))

import matplotlib.pyplot as plt

plt.plot(est_incidence)
plt.plot(act_incidence, 'o')
plt.show()
# @:script