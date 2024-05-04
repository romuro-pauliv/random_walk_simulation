# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                  app/log/genlog.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |                                                                                                 romulopauliv@bk.ru |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from colorama import Fore, Style
import datetime
# |--------------------------------------------------------------------------------------------------------------------|

def subprocess_log(process_n: int, pid: int, start_close: str) -> None:
    datetime_string: str = f"{Fore.CYAN}{datetime.datetime.now()}{Style.RESET_ALL}"
    info: str = f"[{Fore.GREEN if start_close == 'start' else Fore.MAGENTA}{start_close.upper()}]{Style.RESET_ALL}"
    dt_info: str = f"Core[{process_n}] -> PID:{Fore.MAGENTA}[{pid}]{Style.RESET_ALL}"
    print(f"{datetime_string} | {info} {dt_info}")


def bin_manager_log(path_: str, CRUD: str) -> None:
    datetime_string: str = f"{Fore.CYAN}{datetime.datetime.now()}{Style.RESET_ALL}"
    info_color: dict[str, str] = {
        "post": f"{Fore.GREEN}", "get": f"{Fore.CYAN}", "delete": f"{Fore.RED}"
    }
    info_class: str = f"{Fore.YELLOW}[BIN DUMP]{Style.RESET_ALL}"
    method: str = f"{info_color[CRUD]}[{CRUD.upper()}]{Style.RESET_ALL}"
    
    print(f"{datetime_string} | {info_class} | {method} -> {path_}")