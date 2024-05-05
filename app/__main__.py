from core.multicore_simulation import MultiCore
from data.concatenate_bin_simulations import concat_simulations

multicore: MultiCore = MultiCore(cpu_offs=1)
multicore.coinflip_args(200, [-1, 1], [0.5, 0.5], 100000, True)
multicore.run()


import numpy as np
data: np.ndarray = concat_simulations()


from graph.all_trajectories import Graph_AllTrajectories
import matplotlib.pyplot as plt

Graph_AllTrajectories(data, [-1, 1], [0.5, 0.5]).plot()
plt.show()