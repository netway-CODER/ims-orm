import wx


class MainWindow(wx.MDIChildFrame):

    def __init__(self, parent, *args, **kwargs):
        super(MainWindow, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.initUI()

    def initUI(self):
        # main panel:
        panel = wx.Panel(self)
        # panel.SetBackgroundColour('#4f5049')

        # main layout:
        vBox = wx.BoxSizer(wx.VERTICAL)

        bmp = wx.Bitmap('images/icon_person.png', wx.BITMAP_TYPE_PNG)
        btn1 = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp)
        btn1.SetLabel('Human Resource')
        self.Bind(wx.EVT_BUTTON, self.OnBtn1Click, btn1)
        btn2 = wx.Button(panel, label="Button 2", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.onBtn2Click, id=btn2.GetId())
        btn3 = wx.Button(panel, label="Button 3", size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.onBtn3Click, id=btn3.GetId())
        # another style to create a button
        btn4 = wx.Button(panel, wx.ID_ANY, 'Exit', (70, 30))
        self.Bind(wx.EVT_BUTTON, self.onQuit, id=btn4.GetId())

        vBox.Add(btn1, border=10)
        vBox.Add(btn2, border=10)
        vBox.Add(btn3, border=10)
        vBox.Add(btn4, border=10)
        panel.SetSizer(vBox)

    @staticmethod
    def OnBtn1Click(e):
        nWindow = wx.Frame(None, title='HR')
        nWindow.Show()
        e.Skip()

    @staticmethod
    def onBtn2Click(e):
        print("btn2 on clicked.")
        e.Skip()

    def onBtn3Click(self, e):
        ted = wx.TextEntryDialog(self, "Please enter a name:", "name")
        result = False
        if ted.ShowModal() == wx.ID_OK:
            result = ted.GetValue()
        print(result)
        e.Skip()

    def onQuit(self, e):
        self.Close(True)
        e.Skip()

    @staticmethod
    def empOnClicked():
        wx.MessageBox('working', 'info', wx.OK | wx.ICON_INFORMATION)

# end of file.