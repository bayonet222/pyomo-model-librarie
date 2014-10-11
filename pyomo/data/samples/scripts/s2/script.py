from pyomo.core import *
import pyomo.opt
import pyomo.modeling
#
# Import model
import knapsack
#
# Create the model instance
instance = knapsack.model.create("knapsack.dat")
#
# Setup the optimizer
opt = pyomo.opt.SolverFactory("glpk")
#
# Optimize
results = opt.solve(instance, suffixes=['.*'])
#
# Update the results, to use the same labels as the model
transformed_results = instance.update_results(results)
#
# Print the results
i = 0
for sol in transformed_results.solution:
    print("Solution "+str(i))
    #
    print(sorted(sol.variable.keys()))
    for var in sorted(sol.variable.keys()):
        print("  Variable "+str(var))
        for key in sorted(sol.variable[var].keys()):
            print('     '+str(key)+' '+str(sol.variable[var][key]))
    #
    for con in sorted(sol.constraint.keys()):
        print("  Constraint "+str(con))
        for key in sorted(sol.constraint[con].keys()):
            print('     '+str(key)+' '+str(sol.constraint[con][key]))
    #
    i += 1
#
# An alternate way to print just the constraint duals
print("")
print("Dual Values")
for con in sorted(transformed_results.solution(0).constraint.keys()):
    print(str(con)+' '+str(transformed_results.solution(0).constraint[con]["Dual"]))
