from core.multicore_simulation import MultiCore


multicore: MultiCore = MultiCore(cpu_offs=1)
multicore.coinflip_args(200, [-5, -1, 1, 5],[0.25, 0.25, 0.25, 0.25], 10000, True)
multicore.run()