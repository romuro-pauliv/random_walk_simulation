from core.multicore_simulation import MultiCore
from data.concatenate_bin_simulations import concat_simulations


# VARS |-------------------------------------------------------|
SAMPlES     : int           = 200
STATES      : list[int]     = [-1, 1]
PROB        : list[float]   = [0.5, 0.5]
SIMULATIONS : int           = 100000
ACUMULATE   : bool          = True

CPU_OFF     : int           = 1
# |------------------------------------------------------------|


multicore: MultiCore = MultiCore(cpu_offs=CPU_OFF)
multicore.coinflip_args(SAMPlES, STATES, PROB, SIMULATIONS, ACUMULATE)
multicore.run()


import numpy as np
data: np.ndarray = concat_simulations()

import matplotlib.pyplot as plt
from graph.all_trajectories import Graph_AllTrajectories
from graph.distribution import Distribution, DistAnalysis

Graph_AllTrajectories(data, STATES, PROB).plot()
Distribution(data, STATES, PROB).plot()
DistAnalysis(data, STATES, PROB).plot()
plt.show()