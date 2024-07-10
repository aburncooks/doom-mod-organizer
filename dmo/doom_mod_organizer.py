"""
Initializes data and launches the application
"""
import os.path
import sys

import yaml
from logbook import Logger, NestedSetup, StreamHandler, TimedRotatingFileHandler

from gui.app import DMOApplication
from gui.main_frame import MainFrame


app_log = Logger(__name__)


# launch the application
if __name__ == "__main__":
    with open("config.yaml", "r") as config_yaml:
        config = yaml.safe_load(config_yaml.read())

    log_handlers = []
    if "handlers" in config["logger"].keys():
        for handler, options in config["logger"]["handlers"].items():
            if handler == "stream":
                log_handlers.append(StreamHandler(sys.stdout, **options))
            if handler == "timed_rotating_file":
                log_handlers.append(TimedRotatingFileHandler(os.path.abspath("logs"), **options))

    log_setup = NestedSetup(log_handlers)
    with log_setup:
        app_log.info("Starting Doom Mod Organizer")
        app = DMOApplication()

        main_frame = MainFrame(app.app_name, config)
        app.MainLoop()
