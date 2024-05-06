# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/graph/distribution.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |                                                                                                 romulopauliv@bk.ru |
# |--------------------------------------------------------------------------------------------------------------------|

# | External Imports |-------------------------------------------------------------------------------------------------|
import numpy as np

import json

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.stats import gaussian_kde, norm

from matplotlib.axes    import Axes
from matplotlib.figure  import Figure
# |--------------------------------------------------------------------------------------------------------------------|


class Distribution(object):
    def __init__(self, data: np.ndarray, sample_space: list[str], prob: list[float]) -> None:
        """
        Initialize Distribution object.

        Args:
            data (np.ndarray): Data array containing trajectories.
            sample_space (List[int]): List of sample space values.
            prob (List[float]): List of probabilities.
        """
        self.data           : np.ndarray    = data
        self.sample_space   : list[int]     = sample_space
        self.prob           : list[float]   = prob
        
        self.fig1_ax1, self.fig1_ax2v, self.fig1 = self._define_fig1()
        
        self.variable_ram_controller: int = 5000
        
    def _define_fig1(self) -> tuple[Axes, Axes, Figure]:
        """
        Define Figure 1 for plotting.

        Returns:
            tuple[Axes, Axes, Figure]: Axes and Figure objects for plotting.
        """
        fig : Figure    = plt.figure(figsize=(12,6))
        gs  : GridSpec  = GridSpec(6, 12)
        
        ax_plot     : Axes = fig.add_subplot(gs[0:6,0:9])
        ax_hist_y   : Axes = fig.add_subplot(gs[0:6, 9:12])
        
        return ax_plot, ax_hist_y, fig

    def graph1_data(self) -> None:
        """
        Plot graph 1 data.
        """
        x: np.ndarray = np.arange(self.data.shape[1])
        for i in range(self.data.shape[0]):
            if i == self.variable_ram_controller:
                break
            self.fig1_ax1.plot(x, self.data[i, :], alpha=0.01, color="b")
    
    @staticmethod
    def norm(x: float, mean: float, std: float) -> float:
        """
        Compute the normal distribution probability density function.

        Args:
            x (float): Input value.
            mean (float): Mean of the distribution.
            std (float): Standard deviation of the distribution.

        Returns:
            float: Probability density function value.
        """
        exp = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * std ** 2))
        return exp

    def graph2_data(self) -> None:
        """
        Plot graph 2 data.
        """
        y: np.ndarray = self.data[:, -1]
        x: np.ndarray = np.arange(min(y), max(y))
        
        # Compute Gaussian KDE
        density: gaussian_kde = gaussian_kde(y)
        density.covariance_factor = lambda : .25
        density._compute_covariance()
        y_gauss: np.ndarray = np.array([self.norm(xt, self.mean[-1], self.std[-1]) for xt in x])
        
        self.fig1_ax2v.plot(density(x), x, color="b", alpha=0.5, label="pdf numerical")
        self.fig1_ax2v.plot(y_gauss, x, color="red", linestyle="dashed", alpha=0.5, label=r"$pdf(\mu, \sigma)$")
        
        plt.setp(self.fig1_ax2v.get_yticklabels(), visible=False)
    
    def _calc_graph2_data(self) -> None:
        """
        Calculate data for the second figure.
        """
        self.std    : np.ndarray = np.std(self.data, axis=0)
        self.mean   : np.ndarray = np.mean(self.data, axis=0)
    
    def graph1_info(self) -> None:
        """
        Provide information for graph 1.
        """
        eq1: str = r'$t=$'
        eq2: str = r'$\mu(t)=$'
        eq3: str = r'$\sigma(t)=$'
        
        st1: str = f"{eq1}{self.data.shape[1]}"
        st2: str = f"{eq2}{round(self.mean[-1], 4)}"
        st3: str = f"{eq3}{round(self.std[-1], 4)}"
        
        sample_space_string : str = json.dumps(self.sample_space)
        
        self.fig1_ax1.set_xlabel(r"$t$ (iterations)")
        self.fig1_ax1.set_ylabel(f"cumsum(E), E={sample_space_string}")
        
        self.fig1_ax1.set_title(f"{st1}, {st2}, {st3}")
        
        self.fig1_ax1.grid(True, "both")
    
    def graph2_info(self) -> None:
        """
        Provide information for graph 2.
        """
        self.fig1_ax2v.grid(True, "both")
        
        xlabel_str: str = r"$P(E, t) \rightarrow P(E,$"
        self.fig1_ax2v.set_xlabel(f"{xlabel_str}{self.data.shape[1]})")
        self.fig1_ax2v.legend()
        
    def plot(self) -> None:
        """
        Plot graphs.
        """
        self._calc_graph2_data()
        self.graph1_data()
        self.graph2_data()
        
        self.graph1_info()
        self.graph2_info()



class DistAnalysis(object):
    def __init__(self, data: np.ndarray, sample_space: list[str], prob: list[float]) -> None:
        """
        Initialize Distribution Analysis object.

        Args:
            data (np.ndarray): Data array containing trajectories.
            sample_space (List[int]): List of sample space values.
            prob (List[float]): List of probabilities.
        """
        self.data           : np.ndarray    = data
        self.sample_space   : list[int]     = sample_space
        self.prob           : list[float]   = prob

        self.mean_std()
        self.xy()
        self.define_fig()
        
    @staticmethod
    def norm(x: float, mean: float, std: float) -> float:
        """
        Compute the normal distribution probability density function.

        Args:
            x (float): Input value.
            mean (float): Mean of the distribution.
            std (float): Standard deviation of the distribution.

        Returns:
            float: Probability density function value.
        """
        exp = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * std ** 2))
        return exp

    def mean_std(self) -> None:
        """
        Calculate mean and standard deviation of the data.
        """
        self.std    : np.ndarray = np.std(self.data, axis=0)
        self.mean   : np.ndarray = np.mean(self.data, axis=0)
    
    def xy(self) -> None:
        """
        Compute x and y values for plotting.
        """
        self.y: np.ndarray = self.data[:, -1]
        self.x: np.ndarray = np.arange(min(self.y), max(self.y))
        
        # Compute Gaussian KDE
        density: gaussian_kde = gaussian_kde(self.y)
        density.covariance_factor = lambda : .25
        density._compute_covariance()
        
        self.y_kde  : np.ndarray = density(self.x)
        self.y_gauss: np.ndarray = np.array([self.norm(xt, self.mean[-1], self.std[-1]) for xt in self.x])
    
    def define_fig(self) -> None:
        """
        Define the figure for plotting.
        """
        self.FIG: tuple[Figure, tuple[Axes]] = plt.subplots(1, 3, figsize=(15, 3))
    
    def plot1(self) -> None:
        """
        Plot raw data histogram.
        """
        self.FIG[1][0].hist(self.y, bins=100, color="b", alpha=0.5, label="raw data")
        self.FIG[1][0].grid(True, "both")
        self.FIG[1][0].legend()
        self.FIG[1][0].set_xlabel(f"t = {self.data.shape[1]}")
    
    def plot2(self) -> None:
        """
        Plot PDFs.
        """
        self.FIG[1][1].plot(self.x, self.y_kde, color="b", alpha=0.5, label="pdf numerical")
        self.FIG[1][1].plot(self.x, self.y_gauss, color="r", alpha=0.5, linestyle="dashed", label=r"$pdf(\mu, \sigma)$")
        self.FIG[1][1].grid(True, "both")
        self.FIG[1][1].legend()
        self.FIG[1][1].set_xlabel(f"t = {self.data.shape[1]}")
        
    def plot3(self) -> None:
        """
        Plot cumulative sum of PDFs.
        """
        self.FIG[1][2].plot(self.x, np.cumsum(self.y_kde), color="b", alpha=0.5, label=r"$\int pdf$ numerical")
        self.FIG[1][2].plot(self.x, np.cumsum(self.y_gauss), color="r", alpha=0.5, linestyle="dashed", label=r"$\int pdf(\mu, \sigma)$")
        self.FIG[1][2].grid(True, "both")
        self.FIG[1][2].legend()
        self.FIG[1][2].set_xlabel(f"t = {self.data.shape[1]}")
    
    def plot(self) -> None:
        """
        Plot all figures.
        """
        self.plot1()
        self.plot2()
        self.plot3()