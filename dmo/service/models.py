"""
Various and sundry models
"""
import os.path
from subprocess import Popen

import yaml

from service.config import Config


class Mods:
    """
    Mods class
    """
    def __init__(self, config: Config) -> None:
        """
        Create a Mods class

        :param config: application config
        """
        self.config = config
        self.mods_path = self.config.params["mods_path"]
        self.mods = []

    def load_mods_from_mods_path_folder(self) -> None:
        """
        Get all the mods in the mods folder
        """
        if not os.path.exists(self.mods_path):
            # mods folder stopped existing for some reason?
            self.mods = []
            return None

        new_mods = []
        for file in os.listdir(self.mods_path):
            if not file.endswith(tuple(self.config.params["mod_file_extensions"])):
                continue
            new_mods.append(os.path.join(self.mods_path, file))
        self.mods = new_mods

    def as_dict(self) -> dict:
        """
        Output this class as a dict

        :return: mods as a dict
        """
        return {"mods_path": self.mods_path,
                "mods": self.mods}


class Profile:
    """
    Profile class
    """
    def __init__(self) -> None:
        """
        Create a Profile class
        """
        self.name = None
        self.mods = []

    def load_profile_from_file(self, file_path: str) -> None:
        """
        Load a profile from a file
        """
        with open(file_path, "r") as profile_yaml:
            profile = yaml.safe_load(profile_yaml.read())
            # TODO: what if this fails?

        if "name" in profile.keys():
            self.name = profile["name"]

        if "mods" in profile.keys():
            self.mods = profile["mods"]

    def write_profile_to_file(self, file_path: str) -> None:
        """
        Create a YAML file from a profile
        """
        yaml_dict = self.as_dict()

        with open(file_path, "w") as yaml_file:
            # TODO: what if the path doesn't exist?
            yaml.dump(yaml_dict, yaml_file)

    def as_dict(self) -> dict:
        """
        Output this profile as a dict

        :return: profile as a dict
        """
        return {"name": self.name,
                "mods": self.mods}


class Launcher:
    """
    Launcher class, for launching the game
    """
    def __init__(self, config: Config) -> None:
        """
        Create a Launcher class

        :param config: application config
        """
        self.config = config

    def launch_prep(self, profile: Profile) -> list:
        """
        Prepare the launch params

        :param profile: the profile to launch the game with

        :return: list of launch params
        """
        launch_params = [self.config.params["source_port"]]

        if len(profile.mods) > 0:
            launch_params.append("-file")
            launch_params.extend(profile.mods)

        return launch_params

    def launch(self, profile: Profile) -> None:
        """
        Launch the game

        :param profile: the profile to launch the game with
        """
        launch_string = " ".join(self.launch_prep(profile))
        Popen(launch_string)  # TODO: what about return?
