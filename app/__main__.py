from core.multicore_simulation import MultiCore


multicore: MultiCore = MultiCore(cpu_offs=1)
multicore.coinflip_args(100, [-1, 1], [0.5, 0.5], 1000, True)
multicore.run()
