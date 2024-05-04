# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/generator/coinflip.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |                                                                                                 romulopauliv@bk.ru |
# |--------------------------------------------------------------------------------------------------------------------|

# | External Imports |-------------------------------------------------------------------------------------------------|
import  numpy       as np
from    typing      import Union
# |--------------------------------------------------------------------------------------------------------------------|

class GeneratorRandomWalk(object):
    def __init__(self, samples: int, prob: list[float], sample_space: list[Union[float, int]]) -> None:
        """
        Initialize the GeneratorRandomWalk instance.
        Args:
            samples (int): Quantity of samples in the simulation.
            sample_space: (list[Union[float, int]]): Possible values for each random sample
            prob (list[float]): if sample_space = [-1, 1] -> probability of each sample 
                                being -1 or 1. In the list [p(-1), p(1)]

        """
        self.sample_space   : list[Union[float, int]]   = sample_space
        self.samples        : int                       = samples
        self.prob           : list[float]               = prob
        
    def run(self) -> None:
        """
        Creates an array with n-self.samples with values equal to -1 or 1 based on the 
        probability entered by self.prob.
        """
        self.data: list[np.float64] = []
        for _ in range(self.samples):
            self.data.append(np.random.choice(self.sample_space, p=self.prob))
        self.data: np.ndarray = np.array(self.data)
    
    def get_array(self) -> np.ndarray:
        """
        returns the simulation array. Example: if sample_space = [-1, 1] -> [-1, 1, 1, -1, ..., -1]
        Returns:
            np.ndarray: The simulation array
        """
        return self.data
    
    def get_cum_array(self) -> np.ndarray:
        """
        returns the accumulated simulation array. Example: if sample_space = [-1, 1] [-1, 1, 1, -1, ..., -1]
        Returns:
            np.ndarray: The accumulated simulation array
        """
        return np.cumsum(self.data)
    