import wx


class MainToolbar(wx.ToolBar):
    def __init__(self, *args, **kwargs):
        super(MainToolbar, self).__init__(*args, **kwargs)
        self.initUI()
        self.Realize()

    def initUI(self):
        emp = self.AddTool(wx.ID_ANY, 'Employee', wx.Bitmap('images/icon_person.png'), shortHelp='Employee Department')
        self.Bind(wx.EVT_MENU, self.empOnClicked, emp)

    def empOnClicked(self, e):
        wx.MessageBox("working!")