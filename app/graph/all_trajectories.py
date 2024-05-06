# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                      app/graph/all_trajectories.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |                                                                                                 romulopauliv@bk.ru |
# |--------------------------------------------------------------------------------------------------------------------|

# | External Imports |-------------------------------------------------------------------------------------------------|
import numpy as np
import json

import matplotlib.pyplot as plt

from matplotlib.axes    import Axes
from matplotlib.figure  import Figure
# |--------------------------------------------------------------------------------------------------------------------|

class Graph_AllTrajectories(object):
    def __init__(self, data: np.ndarray, sample_space: list[int], prob: list[float]) -> None:
        """
        Initialize Graph_AllTrajectories object.

        Args:
            data (np.ndarray): Data array containing trajectories.
            sample_space (List[int]): List of sample space values.
            prob (List[float]): List of probabilities.
        """
        self.data           : np.ndarray    = data
        self.sample_space   : list[int]     = sample_space
        self.prob           : list[float]   = prob
        self.FIG            : tuple[Figure, tuple[Axes, Axes]] = plt.subplots(1, 2, figsize=(12, 6))

        self.variable_ram_controller: int = 5000
        
    def _fig1_data(self) -> None:
        """
        Plot data for the first figure.
        """
        x: np.ndarray = np.arange(self.data.shape[1])
        for i in range(self.data.shape[0]):
            if i == self.variable_ram_controller:
                break
            self.FIG[1][0].plot(x, self.data[i, :], alpha=0.01, color="b")
    
    def _fig1_infos(self) -> None:
        """
        Set information for the first figure.
        """
        self.FIG[1][0].grid(True, "both")
        self.FIG[1][0].set_xlabel(r"$t$ (iterations)")
        
        sample_space_string : str = json.dumps(self.sample_space)
        prob_string         : str = json.dumps(self.prob)
        
        sim_string  : str = f"Sim: [{self.data.shape[0]}]"
        t_string    : str = f"{r'$t$'}: [{self.data.shape[1]}]"
        E_string    : str = f"{r'$E$'}: {sample_space_string}"
        P_string    : str = f"{r'$P$'}: {prob_string}"
        
        self.FIG[1][0].set_ylabel(f"cumsum(E), E={sample_space_string}")
        self.FIG[1][0].set_title(f" {sim_string} | {t_string} | {E_string} | {P_string}")
    
    def _calc_fig2_data(self) -> None:
        """
        Calculate data for the second figure.
        """
        self.std    : np.ndarray = np.std(self.data, axis=0)
        self.mean   : np.ndarray = np.mean(self.data, axis=0)
    
    def _fig2_data(self) -> None:
        """
        Plot data for the second figure.
        """
        x: np.ndarray = np.arange(self.data.shape[1])
        label1: str = r"$\mu(t) + \sigma(t)$"
        label2: str = r"$\mu(t) + 3\sigma(t)$"
        label3: str = r"$\mu(t)$"
        self.FIG[1][1].plot(x, self.mean+self.std, '-o', color="red", markersize=0.5, alpha=0.5, label=label1)
        self.FIG[1][1].plot(x, self.mean+3*self.std, '-o', color="orange", markersize=0.5, alpha=0.5, label=label2)
        self.FIG[1][1].plot(x, self.mean, color="r", alpha=0.5, linestyle="dashed", label=label3)
    
    def _fig2_infos(self) -> None:
        """
        Set information for the second figure.
        """
        self.FIG[1][1].grid(True, "both")
        self.FIG[1][1].set_xlabel(r"$t$ (iterations)")
        self.FIG[1][1].legend()
        
        eq1: str = r'$t=$'
        eq2: str = r'$\mu(t)=$'
        eq3: str = r'$\sigma(t)=$'
        
        st1: str = f"{eq1}{self.data.shape[1]}"
        st2: str = f"{eq2}{round(self.mean[-1], 4)}"
        st3: str = f"{eq3}{round(self.std[-1], 4)}"
        
        self.FIG[1][1].set_title(f"{st1}, {st2}, {st3}")

    
    def plot(self) -> None:
        """
        Plot all trajectories.
        """
        self._fig1_data()
        self._fig1_infos()
        
        self._calc_fig2_data()
        self._fig2_data()
        self._fig2_infos()