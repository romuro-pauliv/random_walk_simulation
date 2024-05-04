from core.multicore_simulation import MultiCore


multicore: MultiCore = MultiCore(1)
multicore.coinflip_args(200, [0.5, 0.5], 10000, True)
multicore.run()