import wx
from sqlalchemy.sql.functions import current_user

from Accounts.dialogs import LoginDialog
from MyWxLib.menus import MainMenu
from mainWindow import MainWindow


class BlankWindow(wx.MDIParentFrame):
    def __init__(self, *args, **kwargs):
        super(BlankWindow, self).__init__(*args, **kwargs)
        self.user = None
        self.initUI()
        self.initWindows()
        self.SetTitle(kwargs['title'])
        self.SetBackgroundColour('gray')
        self.ShowFullScreen(True)

    def initUI(self):
        # add menu
        nMenu = MainMenu(self)
        self.SetMenuBar(nMenu)

    def initWindows(self):
        mWindow = MainWindow(self)
        if LoginDialog(self).ShowModal():
            if self.user:
                wx.MessageBox("Hi, {}".format(self.user))
                mWindow.Show()
        else:
            self.Close()



def main():
    app = wx.App()
    window = BlankWindow(None, title="Netway Computer Management System")
    window.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()