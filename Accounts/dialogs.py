import wx

from Accounts import Session
from Accounts.model import User


# login dialog


class LoginDialog(wx.Dialog):
    def __init__(self, parent):
        super(LoginDialog, self).__init__(parent)
        self.parent = parent
        self.initUI()
        self.SetTitle('Sign-In')
        self.CenterOnParent()

    def initUI(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        # username field
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)
        user_label = wx.StaticText(self, label='User Name:')
        user_sizer.Add(user_label, 0, wx.ALL | wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        self.user.SetFocus()
        user_sizer.Add(self.user, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(user_sizer, 0, wx.ALL, 5)

        # password field
        pwd_sizer = wx.BoxSizer(wx.HORIZONTAL)  # buttons
        pwd_label = wx.StaticText(self, label='Password:')
        pwd_sizer.Add(pwd_label, 0, wx.ALL | wx.CENTER, 5)
        self.pwd = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        pwd_sizer.Add(self.pwd, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(pwd_sizer, 0, wx.ALL, 5)

        """ register
        register_box = wx.BoxSizer(wx.HORIZONTAL)
        register_label = wx.StaticText(self, label="Not a user?")
        register_box.Add(register_label, 0, wx.ALL, 5)
        register_button = wx.Button(self, label="Sign Up")
        register_box.Add(register_button, 0, wx.ALL | wx.RIGHT, 5)
        sizer.Add(register_box, 1, wx.ALL, 5)
        """

        # buttons
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        login_button = wx.Button(self, label='Sign In')
        cancel_button = wx.Button(self, label='Cancel')
        hbox.Add(login_button, 0, wx.ALL, 5)
        hbox.Add(cancel_button, 0, wx.ALL, 5)
        sizer.Add(hbox, 1, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)

        login_button.Bind(wx.EVT_BUTTON, self.onLogin)
        cancel_button.Bind(wx.EVT_BUTTON, self.onCancel)

    def onLogin(self, e):
        current_user_name = self.user.GetValue()
        if current_user_name:
            with Session() as session:
                lUser = session.query(User).filter(User.name == current_user_name).one()
                print(lUser)
        current_password = self.pwd.GetValue()
        if current_password == lUser.password:
            self.parent.user = current_user_name
            self.EndModal(True)
        else:
            wx.MessageBox("User is not existed or wrong password!", "Login False")
            self.pwd.SetFocus()
        e.Skip()

    def onCancel(self, e):
        self.EndModal(False)
        e.Skip()


# user entry form dialog:
class UserEntryFormDialog(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super(UserEntryFormDialog, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.top_panel = UserEntryForm(self)

        # buttons
        self.button_panel = BtnPanel(self, accept_button="Add")
        sizer.Add(self.top_panel, 1, wx.ALL | wx.EXPAND, 10)
        sizer.Add(self.button_panel, 1, wx.ALL | wx.ALIGN_LEFT, 10)
        self.SetSizer(sizer)

    def onAcceptBtnClicked(self, e):
        if self.top_panel.onComfirm():
            new_user = self.top_panel.getUser()
            if new_user:
                # TODO: Should I check if the user is already exists?
                with Session.begin() as session:
                    session.add(new_user)
                wx.MessageBox("Add user:{} successfully!".format(new_user), "Add new user")
                self.EndModal(True)
            else:
                self.EndModal(False)
        e.Skip()


# User entry form panel:
class UserEntryForm(wx.Panel):
    def __init__(self, parent):
        super(UserEntryForm, self).__init__(parent)
        self.initUI()

    def initUI(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        # name field:
        hbox_name = wx.BoxSizer(wx.HORIZONTAL)
        lbl_name = wx.StaticText(self, label="User Name:")
        self.name = wx.TextCtrl(self)
        hbox_name.Add(lbl_name, 0, wx.ALL, 5)
        hbox_name.Add(self.name, 0, wx.ALL | wx.EXPAND, 5)

        # email field:
        hbox_email = wx.BoxSizer(wx.HORIZONTAL)
        lbl_email = wx.StaticText(self, label="Email:")
        self.email = wx.TextCtrl(self)
        hbox_email.Add(lbl_email, 0, wx.ALL | wx.EXPAND, 5)
        hbox_email.Add(self.email, 0, wx.ALL, 5)

        # password field:
        hbox_password = wx.BoxSizer(wx.HORIZONTAL)
        lbl_password = wx.StaticText(self, label="Password:")
        self.password = wx.TextCtrl(self)
        hbox_password.Add(lbl_password, 0, wx.ALL | wx.EXPAND, 5)
        hbox_password.Add(self.password, 0, wx.ALL, 5)

        # comfirm password field:
        hbox_comfirm_password = wx.BoxSizer(wx.HORIZONTAL)
        lbl_comfirm_password = wx.StaticText(self, label="Comfirm Password:")
        self.comfirm_password = wx.TextCtrl(self)
        hbox_comfirm_password.Add(lbl_comfirm_password, 0, wx.ALL | wx.EXPAND, 5)
        hbox_comfirm_password.Add(self.comfirm_password, 0, wx.ALL, 5)

        # Add all BoxSizer to main sizer:
        sizer.Add(hbox_name, 1, wx.ALL, 5)
        sizer.Add(hbox_email, 1, wx.ALL, 5)
        sizer.Add(hbox_password, 1, wx.ALL, 5)
        sizer.Add(hbox_comfirm_password, 1, wx.ALL, 5)

        self.SetSizer(sizer)

    def getUser(self):
        nUser = User()
        nUser.name = self.name.GetValue()
        nUser.email = self.email.GetValue()
        if self.onComfirm():
            nUser.password = self.onComfirm()
            print(nUser)
            return nUser
        else:
            return None

    def onComfirm(self):
        new_password = self.password.GetValue()
        comfirm_password = self.comfirm_password.GetValue()
        if new_password != comfirm_password:
            wx.MessageBox("Comfirm password is not the same!", "Error", wx.OK | wx.ICON_ERROR)
            self.comfirm_password.SetFocus()
            return None
        else:
            return new_password


# Button Panel:
class BtnPanel(wx.Panel):
    def __init__(self, parent, accept_button="Apply"):
        super(BtnPanel, self).__init__(parent)
        self.parent = parent

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        acceptbutton = wx.Button(self, label=accept_button)
        cancel_button = wx.Button(self, label='Cancel')
        sizer.Add(acceptbutton, 0, wx.ALL, 5)
        sizer.Add(cancel_button, 0, wx.ALL, 5)
        self.SetSizer(sizer)

        acceptbutton.Bind(wx.EVT_BUTTON, self.parent.onAcceptBtnClicked)
        cancel_button.Bind(wx.EVT_BUTTON, self.onCancel)

    def onCancel(self, e):
        self.parent.EndModal(False)
        e.Skip()

# End of file.