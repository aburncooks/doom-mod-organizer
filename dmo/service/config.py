"""
Config parsing and management
"""
import yaml


class Config:
    """
    Config class
    """
    def __init__(self, defaults=True):
        """
        Create a Config class

        :param defaults: set the defaults automatically on creation
        """
        self.params = {}

        if defaults:
            self.set_defaults()

    def set_defaults(self) -> None:
        """
        Set the default config values
        """
        self.define_param("icon", "DMOIcon.png")
        self.define_param("mods_path", "F:\\GZDoom\\WADs")
        self.define_param("source_port", "F:\\GZDoom\\GZDoom.exe")
        self.define_param("mod_file_extensions", [".wad", ".WAD"])

    def define_param(self, param_name: str, default_value) -> None:
        """
        Define a new config parameter

        :param param_name: the parameter name
        :param default_value: the default value
        """
        self.params[param_name] = default_value

    def from_yaml(self, yaml_file: str) -> None:
        """
        Load config from a yaml, overwriting existing entries

        :param yaml_file: yaml file path to load config from
        """
        with open(yaml_file, "r") as config_yaml:
            config = yaml.safe_load(config_yaml.read())

        # overwrite the default values if they are set in the yaml
        for param, value in config.items():
            self.params[param] = value
