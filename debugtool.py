
# -*- coding: gbk -*-  

import wx  
import os
import commands
  
class MyFrame(wx.Frame):  
  
    def __init__(self):  
        wx.Frame.__init__(self, parent=None,title="Debug Tool",pos = (100,100), size=(500,500), style=wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN) 
          
        panelParam = wx.Panel(parent=self,pos = (0,0)) 
        wx.StaticText(parent=panelParam, label= " Src Path:", pos=(12, 24),size=(100, 25))  
        self.srcCtrl = wx.TextCtrl(parent=panelParam, value = "G:\\Code\\Project\\lianhuaOKCard\\OKcard", pos=(100, 24),size=(350, 25))  
        wx.StaticText(parent=panelParam, label= " Dir Name:", pos=(12, 70),size=(100, 25))  
        self.pushCtrl = wx.TextCtrl(parent=panelParam, value = "00000001", pos=(100, 70),size=(350, 25)) 
        wx.StaticText(parent=panelParam, label= " Pull Path:", pos=(12, 106),size=(100, 25))  
        self.pullCtrl = wx.TextCtrl(parent=panelParam, value = "C:\\Users\\xiongxq\\Desktop\\a", pos=(100, 106),size=(350, 25)) 

        self.pushBtn=wx.Button(parent=panelParam,label= "Push",pos=(10, 140),size=(100, 100))  
        self.pushBtn.Bind(wx.EVT_BUTTON,  self.OnPushButtonClick) 
        self.clearCacheBtn=wx.Button(parent=panelParam,label= "Clear Cache",pos=(120, 140),size=(100, 100))  
        self.clearCacheBtn.Bind(wx.EVT_BUTTON,  self.OnClearCacheButtonClick) 
        self.clearSrcBtn=wx.Button(parent=panelParam,label= "Clear Source",pos=(230, 140),size=(100, 100))  
        self.clearSrcBtn.Bind(wx.EVT_BUTTON,  self.OnClearSrcButtonClick) 
        self.clearDBBtn=wx.Button(parent=panelParam,label= "Clear DB",pos=(340, 140),size=(100, 100))  
        self.clearDBBtn.Bind(wx.EVT_BUTTON,  self.OnClearDBButtonClick) 
        self.pullDBBtn=wx.Button(parent=panelParam,label= "Pull DB",pos=(10, 250),size=(100, 100))  
        self.pullDBBtn.Bind(wx.EVT_BUTTON,  self.OnPullDBButtonClick) 
        self.pullSrcBtn=wx.Button(parent=panelParam,label= "Pull Src",pos=(120, 250),size=(100, 100))  
        self.pullSrcBtn.Bind(wx.EVT_BUTTON,  self.OnPullSrcButtonClick) 
        self.pullSharelibsBtn=wx.Button(parent=panelParam,label= "Pull Sharelibs",pos=(230, 250),size=(100, 100))  
        self.pullSharelibsBtn.Bind(wx.EVT_BUTTON,  self.OnPullShareButtonClick)   
        self.clearConsloleBtn=wx.Button(parent=panelParam,label= "Clear Console",pos=(340, 250),size=(100, 100))  
        self.clearConsloleBtn.Bind(wx.EVT_BUTTON,  self.OnClearConsoleButtonClick)   
        self.area_text = wx.TextCtrl(panelParam, -1, u'',pos=(10, 370), size=(450, 90),  
                                     style=(wx.TE_MULTILINE | wx.TE_AUTO_SCROLL | wx.TE_DONTWRAP)) 
        self.area_text.SetEditable(False)
        icon = wx.Icon('.\debugtool.ico')
        self.SetIcon(icon)
        # self.taskBarIcon=wx.TaskBarIcon()  
        # self.taskBarIcon.SetIcon(icon,"Debug Tool") 
        self.Centre()
        self.Show(True)  
          
    def GetSrcPath(self):
        return self.srcCtrl.GetValue()
    def GetPushPath(self):
        return self.pushCtrl.GetValue()
    def GetPullPath(self):
        return self.pullCtrl.GetValue()

    def CheckStatusForDisplay(self, status, do):
        if (status == 0):
            self.area_text.WriteText('%s Done\n' % do)
        else :
            self.area_text.WriteText('%s Fail\n' % do)

    def OnClearConsoleButtonClick(self,event): 
        self.area_text.Clear()

    def OnClearSrcButtonClick(self,event): 
        print 'clear src click'
        pushPath = self.GetPushPath()
        print pushPath
        cmd = "adb shell rm -rf /Share/UmsTssMaster/resource/" + pushPath
        print cmd
        # result = os.popen(cmd)
        # print result.read()
        result = os.system(cmd)
        self.CheckStatusForDisplay(result, 'Clear Src')

    def OnClearDBButtonClick(self,event): 
        print 'clear db click'
        pushPath = self.GetPushPath()
        print pushPath
        cmd = "adb shell rm -rf /Share/UmsTssMaster/storage/" + pushPath
        print cmd
        result = os.system(cmd)
        self.CheckStatusForDisplay(result, 'Clear DB')

    def OnClearCacheButtonClick(self,event):
        print 'clear cache click'
        cmd = "adb shell pm clear com.ums.tss.mastercontrol"
        print cmd
        result = os.system(cmd)
        self.CheckStatusForDisplay(result, 'Clear Cache')
        # result = os.popen(cmd)
        # print result.read()
        # (status, output) = commands.getstatusoutput(cmd)
        # self.area_text.SetValue("Status: %s\nOutput: %s" % (str(status), str(output)))
    def OnPushButtonClick(self,event): 
        print 'push click'
        srcPath = self.GetSrcPath()
        print 'srcPath' + srcPath
        pushPath = self.GetPushPath()
        print 'push'+pushPath
        cmd = "adb push %s /Share/UmsTssMaster/resource/%s" % (srcPath,pushPath)
        print cmd
        result = os.system(cmd)
        self.CheckStatusForDisplay(result, 'Push')
    def OnPullDBButtonClick(self,event):
        print 'pull db click'
        pushPath = self.GetPushPath()
        print 'pushPath:' + pushPath
        pullPath = self.GetPullPath()
        print 'pullPath:'+pullPath
        cmd = "adb pull /Share/UmsTssMaster/storage/%s %s\\DB" % (pushPath,pullPath)
        print cmd
        result = os.system(cmd)
        self.CheckStatusForDisplay(result, 'Pull DB')
    def OnPullSrcButtonClick(self,event): 
        print 'pull src click'
        pushPath = self.GetPushPath()
        print 'pushPath:' + pushPath
        pullPath = self.GetPullPath()
        print 'pullPath:'+pullPath
        cmd = "adb pull /Share/UmsTssMaster/resource/%s %s\\src" % (pushPath,pullPath)
        print cmd
        result = os.system(cmd)
        self.CheckStatusForDisplay(result, 'Pull Src')
    def OnPullShareButtonClick(self,event): 
        print 'pull share click'
        pushPath = self.GetPushPath()
        print 'pushPath:' + pushPath
        pullPath = self.GetPullPath()
        print 'pullPath:'+pullPath
        cmd = "adb pull /Share/UmsTssMaster/resource/sharelibs %s\\sharelibs" % (pullPath)
        print cmd
        result = os.system(cmd)
        self.CheckStatusForDisplay(result, 'Pull Sharelibs')

    def OnQuit(self, event): 
        # self.taskBarIcon.Destroy()
        self.Close()  
          
          
#################################################################################  
if __name__ == '__main__':  
    app = wx.App()  
    frame = MyFrame()  
    app.MainLoop()  
#################################################################################