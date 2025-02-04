import os
import sys
import pickle
from typing import Dict
import traceback

# * ------------------------------------------------------------ *#

# from etc.logger import *

# * ------------------------------------------------------------ *#


class Config:
    VERSION: str = "1.0.1"

    def get_base_path() -> str:
        if getattr(sys, "frozen", False):
            # PyInstaller
            if hasattr(sys, "_MEIPASS"):
                return sys._MEIPASS
            # py2app
            else:
                return os.path.join(os.path.dirname(sys.executable), "..", "Resources")
        else:
            return os.getcwd()


    FONT_PATH: str = os.path.join(get_base_path(), "res", "NanumGothicBold.otf")
    ICON_PATH: str = os.path.join(get_base_path(), "res", "CRMM.ico")

    PLATFORMS_PATH: str = os.path.join(get_base_path(), "platforms")

    # logger = init_logger(
    #     name="Trader of YM Investment",
    #     version=VERSION,
    #     c_level=DEBUG,
    #     f_level=INFO,
    #     f_path="./log",
    # )

    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1.0"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1.0"
    os.environ["QT_SCALE_FACTOR"] = "1.0"

    DATA_PATH: str = "data.dat"
    DATA: Dict = {}

    @classmethod
    def save_data(cls) -> None:
        with open(cls.DATA_PATH, "wb") as f:
            pickle.dump(cls.DATA, f)

        return

    @classmethod
    def load_data(cls) -> None:
        if not os.path.isfile(cls.DATA_PATH):
            return

        try: 
            with open(cls.DATA_PATH, "rb") as f:
                cls.DATA: Dict = pickle.load(f)
        except: 
            exc_type, exc_value, exc_traceback = sys.exc_info()
            formatted_traceback = traceback.format_exception(
                exc_type, exc_value, exc_traceback
            )
            exc_msg = "".join(formatted_traceback)

            cls.logger.error(f"Error occured while loading the data:\n{exc_msg}")
            return
        
        return