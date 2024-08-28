"""
GUI implementation for the selections panel of the application
"""
import wx
from logbook import Logger


app_log = Logger(__name__)


class SelectionsPanel(wx.Panel):
    """
    Selections panel class
    """
    def __init__(self, parent, config) -> None:
        """
        Create a controls panel

        :param parent: wx element this panel belongs to
        :param config: the application config
        """
        wx.Panel.__init__(self, parent, id=wx.ID_ANY)
        self.panel_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.panel_sizer)
        self.Show()