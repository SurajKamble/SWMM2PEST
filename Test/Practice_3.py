from pyswmm import Simulation, Subcatchments
dir = "groof09Q1.inp"
with Simulation(dir) as sim:
    subcatch_object = Subcatchments(sim)
    print(vars(subcatch_object))
    SC1 = subcatch_object["FS10"]
    print(SC1.area)
    print(vars(SC1))
    print(sim.execute())

    sim.report()