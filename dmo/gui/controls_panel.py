"""
GUI implementation for the control panel of the application
"""
import wx
from logbook import Logger

from service.models import Launcher, Profile


app_log = Logger(__name__)


class ControlsPanel(wx.Panel):
    """
    Controls panel class
    """
    def __init__(self, parent, config) -> None:
        """
        Create a controls panel

        :param parent: wx element this panel belongs to
        :param config: the application config
        """
        wx.Panel.__init__(self, parent, id=wx.ID_ANY)

        self.launcher = Launcher(config)

        self.panel_sizer = wx.BoxSizer(wx.VERTICAL)

        self.launch_button = wx.Button(self, wx.ID_ANY, 'Launch')

        self.Bind(wx.EVT_BUTTON, self.launch, self.launch_button)

        self.SetSizer(self.panel_sizer)
        self.Show()

    def launch(self, event: wx.Event) -> None:
        """
        Just launch the game already

        :param event: unused wx event handler
        """
        profile = Profile()
        profile.load_profile_from_file("profiles/my_profile.yaml")

        self. launcher.launch(profile)