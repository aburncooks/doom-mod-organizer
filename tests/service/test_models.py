"""
Tests for models classes
"""
import os.path

from tempfile import TemporaryDirectory

from dmo.service.models import Mods


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

    def test_load_mods_from_folder(self):
        """
        Load the valid mods from a folder
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

            assert mods.load_mods_from_folder() == [f"{os.path.join(test_dir, m)}" for m in my_valid_files]
