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