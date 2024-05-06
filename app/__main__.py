# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app/__main__.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |                                                                                                 romulopauliv@bk.ru |
# |--------------------------------------------------------------------------------------------------------------------|

# | Internal Imports |-------------------------------------------------------------------------------------------------|
from core.multicore_simulation import MultiCore
from data.concatenate_bin_simulations import concat_simulations
# |--------------------------------------------------------------------------------------------------------------------|


# VARS |-------------------------------------------------------|
SAMPlES     : int           = 200
STATES      : list[int]     = [-1, 1]
PROB        : list[float]   = [0.5, 0.5]
SIMULATIONS : int           = 10000
ACUMULATE   : bool          = True

CPU_OFF     : int           = 1
# |------------------------------------------------------------|


# Multiprocessing Simulation
multicore: MultiCore = MultiCore(cpu_offs=CPU_OFF)
multicore.coinflip_args(SAMPlES, STATES, PROB, SIMULATIONS, ACUMULATE)
multicore.run()


# Graphs and analysis
import numpy as np
import matplotlib.pyplot as plt

data: np.ndarray = concat_simulations()

from graph.all_trajectories import Graph_AllTrajectories
from graph.distribution import Distribution, DistAnalysis

Graph_AllTrajectories(data, STATES, PROB).plot()
Distribution(data, STATES, PROB).plot()
DistAnalysis(data, STATES, PROB).plot()
plt.show()