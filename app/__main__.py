from core.multicore_simulation import MultiCore
from data.concatenate_bin_simulations import concat_simulations

multicore: MultiCore = MultiCore(cpu_offs=1)
multicore.coinflip_args(100, [-1, 1], [0.5, 0.5], 10000, True)
multicore.run()


concat_simulations()