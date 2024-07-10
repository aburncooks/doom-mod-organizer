"""
Provides wxPython application data
"""
import wx


class DMOApplication(wx.App):
    """
    A class for DMOApplication
    """
    def __init__(self) -> None:
        """
        Create the DMOApplication app
        """
        super().__init__(DMOApplication)
        self.app_name = "Doom Mod Organizer"
