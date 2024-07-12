"""
Tests for models classes
"""
import os.path

import yaml
from tempfile import TemporaryDirectory

from dmo.service.models import Mods, Profile


class TestMods:
    """
    A test mods class for Mods class tests
    """
    def test_new_mods(self):
        """
        Make a Mods class
        """
        my_path = "my/file/path"
        my_config = {
            "some_key": "some_value",
            "mods_path": my_path
        }

        mods = Mods(my_config)

        assert mods.config == my_config
        assert mods.mods_path == my_path
        assert mods.mods == []

    def test_load_mods_from_mods_path(self):
        """
        Load the valid mods from the mods path folder
        """
        my_valid_files = [
            "my_mod.wad",
            "my_other_mod.WAD"
        ]

        all_files = [
            "my_other_mod.pk3"
        ]

        with TemporaryDirectory() as test_dir:
            all_files.extend(my_valid_files)
            for file in all_files:
                with open(os.path.join(test_dir, file), "w") as f:
                    f.write("...")

            mods = Mods({"mods_path": test_dir})
            mods.load_mods_from_mods_path_folder()

            assert mods.mods == [f"{os.path.join(test_dir, m)}" for m in my_valid_files]

    def test_mods_as_dict(self):
        """
        Return the mods as a dictionary
        """
        my_path = "my/file/path"
        my_config = {
            "some_key": "some_value",
            "mods_path": my_path
        }
        my_mods = ["something/somewhere.WAD"]

        mods = Mods(my_config)
        mods.mods = my_mods

        assert mods.as_dict() == {"config": my_config,
                                  "mods_path": my_path,
                                  "mods": my_mods}


class TestProfile:
    """
    A test mods class for Profile class tests
    """
    def test_new_profiles(self):
        """
        Make a Profile class
        """
        profile = Profile()

        assert profile.name is None
        assert profile.mods == []

    def test_load_profile_from_file(self):
        """
        Create a Profile class from a profile YAML file
        """
        name = "myprofile"
        mods = [
            "something/somewhere.wad",
            "something/else.WAD"
        ]

        with TemporaryDirectory() as test_dir:
            yaml_dict = {
                "name": name,
                "mods": mods
            }
            profile_path = os.path.join(test_dir, "test-profile.yaml")
            with open(profile_path, "w") as test_file:
                yaml.dump(yaml_dict, test_file)

            profile = Profile()
            profile.load_profile_from_file(profile_path)

            assert profile.name == name
            assert profile.mods == mods

    def test_write_profile_to_file(self):
        """
        Create a new profile file from a profile
        """
        with TemporaryDirectory() as test_dir:
            profile_dict = {
                "name": "myprofile",
                "mods": ["something/somewhere.wad"]
            }

            profile = Profile()
            profile.name = profile_dict["name"]
            profile.mods = profile_dict["mods"]

            test_file = os.path.join(test_dir, "my-profile.yaml")
            profile.write_profile_to_file(test_file)

            with open(test_file, "r") as test_yaml:
                output = yaml.safe_load(test_yaml.read())

            assert output == profile_dict

    def test_profile_as_dict(self):
        """
        Return the profile as a dictionary
        """
        name = "myprofile"
        mods = [
            "something/somewhere.wad",
            "something/else.WAD"
        ]

        profile = Profile()
        profile.name = name
        profile.mods = mods

        assert profile.as_dict() == {"name": name,
                                     "mods": mods}
