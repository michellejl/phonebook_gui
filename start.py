import wx

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()


    def basicGUI(self):
        # Create the menu bar
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_CLOSE, 'Exit Program', 'status message')

        menuBar.Append(fileButton, 'File')

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.quitProgram, exitItem)

        self.SetTitle('Epic Window')
        self.Show(True)

    def quitProgram(self, e):
        self.Close()


def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()



main()








