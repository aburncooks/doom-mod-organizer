"""
Initializes data and launches the application
"""
import os.path
import sys

import yaml
from logbook import Logger, NestedSetup, StreamHandler, TimedRotatingFileHandler, NullHandler

from gui.app import DMOApplication
from gui.main_frame import MainFrame
from service.config import Config


app_log = Logger(__name__)


# launch the application
if __name__ == "__main__":
    dmo_config = Config()
    dmo_config.from_yaml("config.yaml")

    log_handlers = [StreamHandler(sys.stdout, level="INFO", bubble=False)]

    if log_handlers is False:
        # TODO: just cooking this for now for pyinstaller experimentations, there must be a better way
        log_handlers.append(NullHandler())

    log_setup = NestedSetup(log_handlers)

    with log_setup:
        app_log.info("Starting Doom Mod Organizer")
        app = DMOApplication()

        main_frame = MainFrame(app.app_name, dmo_config)
        app.MainLoop()
