"""
Test ability to open settings dialog and save fields.
"""
import unittest
import tempfile
import os
import wx

from mydata.models.settings import SettingsModel
from mydata.views.settings import SettingsDialog


class SettingsDialogTester(unittest.TestCase):
    """
    Test ability to open settings dialog and save fields.

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
        self.app = wx.App()
        self.frame = wx.Frame(parent=None, id=wx.ID_ANY,
                              title="Settings Dialog test")
        self.frame.Show()
        self.settingsModel = SettingsModel(configPath=None)
        self.settingsDialog = SettingsDialog(self.frame, self.settingsModel)
        self.settingsDialog.Show()
        self.tempConfig = tempfile.NamedTemporaryFile()
        self.tempFilePath = self.tempConfig.name
        self.tempConfig.close()

    def tearDown(self):
        if os.path.exists(self.tempFilePath):
            os.remove(self.tempFilePath)
        self.settingsDialog.Hide()
        self.frame.Destroy()

    def test_settings_dialog(self):
        """
        Test ability to open settings dialog and save fields.
        """
        self.settingsModel.SaveFieldsFromDialog(self.settingsDialog,
                                                configPath=self.tempFilePath,
                                                saveToDisk=True)


if __name__ == '__main__':
    unittest.main()
