# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                            app/data/concatenate_bin_simulations.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |                                                                                                 romulopauliv@bk.ru |
# |--------------------------------------------------------------------------------------------------------------------|

# | Internal Imports |-------------------------------------------------------------------------------------------------|
from bin.binary_manager import BinManager

# | External Imports |-------------------------------------------------------------------------------------------------|
import numpy as np
# |--------------------------------------------------------------------------------------------------------------------|

def concat_simulations() -> np.ndarray:
    """
    Concatenates binary data from multiple files into a single NumPy array.
    Returns:
        np.ndarray: Concatenated binary data.
    """
    bin_manager: BinManager = BinManager()
    bin_data: list[np.ndarray] = []
    # Iterate over the list of binary files and retrieve their data
    for filename in bin_manager.bin_files_list():
        bin_data.append(bin_manager.get(filename))
    # Concatenate the binary data into a single NumPy array
    return np.concatenate(bin_data)