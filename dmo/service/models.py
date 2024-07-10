"""
Various and sundry models
"""
import os.path


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

    def load_mods_from_folder(self) -> list:
        """
        Get all the mods in the mods folder

        :return: dict of mods
        """
        # TODO: what if the mods folder stops existing?
        new_mods = []
        for file in os.listdir(self.mods_path):
            if not file.endswith((".wad", ".WAD")):
                # TODO: what about .pk3s?
                continue
            new_mods.append(os.path.join(self.mods_path, file))
        return new_mods
