# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/bin/binary_manager.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |                                                                                                 romulopauliv@bk.ru |
# |--------------------------------------------------------------------------------------------------------------------|

# | External Imports |-------------------------------------------------------------------------------------------------|
from pathlib    import Path, PosixPath
from typing     import Any
import pickle
import os
# | Internal Imports |-------------------------------------------------------------------------------------------------|
from log.genlog import bin_manager_log
# |--------------------------------------------------------------------------------------------------------------------|

class BinManager(object):
    def __init__(self) -> None:
        """
        Initializes the BinManager object.
        """
        self.ext    : str       = ".bin"
        self.path_  : PosixPath = Path("app", "bin")
    
    def _path_conversor(self, name: str) -> PosixPath:
        """
        Converts the given name to a PosixPath with the appropriate extension.
        Args:
            name (str): The name of the binary file.
        Returns:
            PosixPath: The converted path.
        """
        return Path(self.path_, f"{name}{self.ext}")
    
    def bin_files_list(self) -> list[str]:
        """
        Retrieves a list of binary files in the bin directory.
        Returns:
            list[str]: List of binary file names.
        """
        bin_files: list[str] = []

        for f in os.listdir(self.path_):
            f_split: list[str] = f.split(".")
            if len(f_split) >= 2:
                bin_files.append(f_split[0]) if f_split[1] == self.ext[1::] else None
                    
        return bin_files
    
    def bin_exists(self, name: str) -> bool:
        """
        Checks if the binary file with the given name exists.
        Args:
            name (str): The name of the binary file.
        
        Returns:
            bool: True if the binary file exists, False otherwise.
        """
        return os.path.exists(self._path_conversor(name))
    
    def delete(self, name: str) -> None:
        """
        Deletes the binary file with the given name.
        Args:
            name (str): The name of the binary file to delete.
        """
        path_: PosixPath = self._path_conversor(name)
        os.remove(path_)
        bin_manager_log(path_, "delete")
        
    def post(self, name: str, obj: Any) -> None:
        """
        Stores the object in a binary file with the given name.
        Args:
            name (str): The name of the binary file.
            obj (Any): The object to store.
        """
        if self.bin_exists(name):
            self.delete(name)
        
        path_: PosixPath = self._path_conversor(name)
        
        with open(path_, "wb") as f:
            pickle.dump(obj, f)
            f.close()
        bin_manager_log(path_, "post")
    
    def get(self, name: str) -> Any:
        """
        Retrieves the object stored in the binary file with the given name.
        Args:
            name (str): The name of the binary file.
        Returns:
            Any: The object stored in the binary file.
        """
        path_: PosixPath = self._path_conversor(name)
        with open(path_, "wb") as f:
            file: Any = pickle.load(f)
        
        bin_manager_log(path_, "get")
        return file
