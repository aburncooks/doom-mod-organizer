"""
GUI implementation for the main frame of the application
"""
from typing import Self

import wx
from logbook import Logger

from gui.controls_panel import ControlsPanel
from gui.selections_panel import SelectionsPanel
from service.config import Config


app_log = Logger(__name__)


class MainFrame(wx.Frame):
    """
    Main frame class
    """
    __instance = None

    @classmethod
    def get_instance(cls) -> Self:
        """
        Get a sepcific instance of this class

        :return: TBC
        """
        return cls.__instance

    def __init__(self, title: str, config: Config) -> None:
        """
        Create a main frame

        :param title: window title
        :param config: the application config
        """
        self.title = title
        self.config = config

        # TODO: don't like None args
        wx.Frame.__init__(self, None, title=self.title)
        MainFrame.__instance = self
        self.SetIcon(wx.Icon(self.config.params["icon"]))

        # do some interesting stuff here
        self.main_frame_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.controls_panel = ControlsPanel(self, self.config)

        self.selections_panel = SelectionsPanel(self, self.config)

        self.main_frame_sizer.Add(self.controls_panel, 1, wx.EXPAND)
        self.main_frame_sizer.Add(self.selections_panel, 1, wx.EXPAND)

        self.SetSizer(self.main_frame_sizer)

        # display the frame
        self.Show()
