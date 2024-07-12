"""
Various and sundry models
"""
import os.path

import yaml


class Mods:
    """
    Mods class
    """
    def __init__(self, config: dict) -> None:
        """
        Create a Mods class

        :param config: application config
        """
        self.config = config
        self.mods_path = self.config["mods_path"]
        self.mods = []

    def load_mods_from_mods_path_folder(self) -> None:
        """
        Get all the mods in the mods folder
        """
        # TODO: what if the mods folder stops existing?
        new_mods = []
        for file in os.listdir(self.mods_path):
            if not file.endswith((".wad", ".WAD")):
                # TODO: what about .pk3s?
                continue
            new_mods.append(os.path.join(self.mods_path, file))
        self.mods = new_mods

    def as_dict(self) -> dict:
        """
        Output this class as a dict

        :return: mods as a dict
        """
        return {"config": self.config,
                "mods_path": self.mods_path,
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
