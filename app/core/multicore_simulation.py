# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                   app/core/multicore_simulation.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |                                                                                                 romulopauliv@bk.ru |
# |--------------------------------------------------------------------------------------------------------------------|

# | Internal Imports |-------------------------------------------------------------------------------------------------|
from generator.coinflip_chunk   import coinflip_simulations
from log.genlog                 import subprocess_log

# | External Imports |-------------------------------------------------------------------------------------------------|
from typing                     import Union
import multiprocessing          as mp
import numpy                    as np
# |--------------------------------------------------------------------------------------------------------------------|


class MultiCore(object):
    def __init__(self, cpu_offs: int) -> None:
        """
        Initializes the MultiCore object.

        Args:
            cpu_offs (int): Number of CPU cores to offset from the total available cores.
        """
        self.on_cpu: int = mp.cpu_count() - cpu_offs
    
    def coinflip_args(self, samples: int, sample_space: Union[float, int], prob: list[float], simulations: int,
                      cum: bool) -> None:
        """
        Set up parameters for coin flip simulations.

        Args:
            samples (int): Quantity of samples in the simulation.
            sample_space: (list[Union[float, int]]): Possible values for each random sample
            prob (list[float]): if sample_space = [-1, 1] -> probability of each sample 
                                being -1 or 1. In the list [p(-1), p(1)]
            simulations (int): The number of simulations to be run.
            cum (bool): Whether the simulation results will be accumulated or not.
        """
        self.samples        : int               = samples
        self.sample_space   : Union[float, int] = sample_space
        self.prob           : list[float]       = prob
        self.simulations    : int               = int(simulations/self.on_cpu)
        self.cumulative     : bool              = cum
    
    def _chunk(self) -> None:
        """
        Run coin flip simulations in chunks.
        """
        data: np.ndarray = coinflip_simulations(
            self.samples, self.prob, self.simulations, self.cumulative, self.sample_space
        )
    
    def _generate_subprocess(self) -> None:
        """
        Generate subprocesses for parallel execution.
        """
        self.process_list: list[mp.Process] = []
        for n in range(self.on_cpu):
            self.process_list.append(mp.Process(target=self._chunk))
    
    def _start_subprocess(self) -> None:
        """
        Start the generated subprocesses.
        """
        for n, process in enumerate(self.process_list):
            process.start()
            subprocess_log(n, process.pid, "start")
    
    def _join_subprocess(self) -> None:
        """
        Wait for subprocesses to finish and clean up resources.
        """
        for n, process in enumerate(self.process_list):
            process.join()
            subprocess_log(n, process.pid, "close")
            process.close()
            
    def run(self) -> None:
        """
        Run the multiprocessing simulation.
        """
        self._generate_subprocess()
        self._start_subprocess()
        self._join_subprocess()