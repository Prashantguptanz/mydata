"""
Test ability to open settings dialog.
"""
import unittest
import logging
import wx

from mydata.models.settings import SettingsModel
from mydata.views.settings import SettingsDialog

logger = logging.getLogger(__name__)


class SettingsDialogTester(unittest.TestCase):
    """
    Test ability to open settings dialog.

    References:
    http://wiki.wxpython.org/Unit%20Testing%20with%20wxPython
    http://wiki.wxpython.org/Unit%20Testing%20Quick%20Start%20Guide
    """
    def setUp(self):
        """
        If we're creating a wx application in the test, it's
        safest to do it in setUp, because we know that setUp
        will only be called once, so only one app will be created.
        """
        self.app = wx.PySimpleApp()
        self.frame = wx.Frame(parent=None, id=wx.ID_ANY)
        self.frame.Show()
        self.settingsModel = SettingsModel(configPath=None)
        self.settingsDialog = SettingsDialog(self.frame, self.settingsModel)

    def tearDown(self):
        self.frame.Hide()
        self.frame.Destroy()
        self.settingsDialog.Hide()
        self.settingsDialog.Destroy()
        self.app.Destroy()

    def test_settings_dialog(self):
        """
        Test ability to open settings dialog.
        """
        # pylint: disable=no-self-use
        self.settingsDialog.Show()


if __name__ == '__main__':
    unittest.main()
