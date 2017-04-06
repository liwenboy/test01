#codind:utf-8

import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super(MainFrame,self).__init__(None,title="test04",size=(800,600))
        self.Center()
        pn=wx.Panel(self)
        pn.SetBackgroundColour("White")
        

class ThisApp(wx.App):
    def OnInit(self):
        f=MainFrame()
        f.Show()
        return True
    
def main():
    app=ThisApp()
    app.MainLoop()
    
if __name__=="__main__":
    main()