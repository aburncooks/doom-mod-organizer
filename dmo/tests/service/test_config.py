"""
Tests for config class
"""
import os.path

import yaml
from tempfile import TemporaryDirectory

from service.config import Config


class TestMods:
    """
    A test config class for Config class tests
    """
    def test_new_config_without_defaults(self):
        """
        Make a Config class without default values
        """
        config = Config(defaults=False)

        assert config.params == {}

    def test_define_new_config_params(self):
        """
        Make a Config class and define new params
        """
        config = Config(defaults=False)

        config.define_param("my_param", "my_value")
        config.define_param("my_other_param", ["my_value1", "my_value2"])

        assert config.params["my_param"] == "my_value"
        assert config.params["my_other_param"] == ["my_value1", "my_value2"]

    def test_define_new_config_from_yaml(self):
        """
        Make a Config class from a YAML file
        """
        config = Config(defaults=False)
        config.define_param("my_param", "my_value")
        config.define_param("my_other_param", "my_value4")

        with TemporaryDirectory() as test_dir:
            yaml_dict = {
                "my_param": "another_value",
                "something_else": "param value",
                "mods": ["my_value1", "my_value2"]
            }

            config_path = os.path.join(test_dir, "test-config.yaml")
            with open(config_path, "w") as test_file:
                yaml.dump(yaml_dict, test_file)

            config.from_yaml(config_path)

            assert config.params["my_param"] == "another_value"
            assert config.params["my_other_param"] == "my_value4"
            assert config.params["something_else"] == "param value"
            assert config.params["mods"] == ["my_value1", "my_value2"]
