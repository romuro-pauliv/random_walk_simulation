# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                        app/chunk/coinflip_chunk.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |                                                                                                 romulopauliv@bk.ru |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from generator.coinflip import GeneratorRandomWalk
import numpy as np
# |--------------------------------------------------------------------------------------------------------------------|

def coinflip_simulations(samples: int, prob: list[float], simulations: int, cumulative: bool) -> list[np.ndarray]:
    """
    Generate the coin flip simulation using the GeneratorRandomWalk object n times.
    (n times is provided by the input of the "simulation" function.) 
    Args:
        samples (int): Quantity of samples in the simulation.
        prob (list[float]): Probability of each sample being -1 or 1. In the list [p(-1), p(1)].
        simulations (int): The number of simulations to be run.
        cumulative (bool): Whether the simulation results will be accumulated or not.

    Returns:
        np.ndarray: The chunk of simulations
    """
    generator: GeneratorRandomWalk = GeneratorRandomWalk(samples, prob)
    
    sim_chunk: list[np.ndarray] = []
    for _ in range(simulations):
        generator.run()
        sim_chunk.append(generator.get_cum_array()) if cumulative == True else sim_chunk.append(generator.get_array())
    
    return np.array(sim_chunk)