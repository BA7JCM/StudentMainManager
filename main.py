﻿#!/usr/bin/env python3
# coding: UTF-8
# This is only a UI file. The main functions are in the utils.py program.

import wx
import wx.adv
import utils
import threading
import time

pathToJiYu = utils.jiYuPath
winOnTop = utils.winOnTop
version = '1.0.2'


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        if winOnTop:
            kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL | wx.STAY_ON_TOP
        else:
            kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("StudentMain Manager")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("image-res\\StudentMainManager.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.NullColour)

        self.frame_statusbar = self.CreateStatusBar(1)
        self.frame_statusbar.SetStatusWidths([70])

        self.notebook = wx.Notebook(self, wx.ID_ANY)

        self.statusPage = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.statusPage, u"状态")

        grid_sizer_1 = wx.GridSizer(3, 2, 0, 0)

        label_1 = wx.StaticText(self.statusPage, wx.ID_ANY, u"极域教室安装状态")
        label_1.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER, 0)

        self.installStatusText = wx.TextCtrl(self.statusPage, wx.ID_ANY, "")
        grid_sizer_1.Add(self.installStatusText, 0, wx.ALIGN_CENTER, 0)

        label_2 = wx.StaticText(self.statusPage, wx.ID_ANY, u"极域教室运行状态")
        label_2.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        grid_sizer_1.Add(label_2, 0, wx.ALIGN_CENTER, 0)

        self.runStatusText = wx.TextCtrl(self.statusPage, wx.ID_ANY, "")
        grid_sizer_1.Add(self.runStatusText, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        self.killPage = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.killPage, u"结束极域")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.killOptionBox = wx.RadioBox(self.killPage, wx.ID_ANY, u"请选择一个操作", choices=[u"NTSD强制结束", u"PsSuspend挂起", u"强制破坏极域教室"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.killOptionBox.SetSelection(0)
        sizer_1.Add(self.killOptionBox, 0, wx.EXPAND, 0)

        self.killButton = wx.Button(self.killPage, wx.ID_ANY, u"执行操作")
        sizer_1.Add(self.killButton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        sizer_3 = wx.StaticBoxSizer(wx.StaticBox(self.killPage, wx.ID_ANY, u"警告"), wx.VERTICAL)
        sizer_1.Add(sizer_3, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)

        label_4 = wx.StaticText(self.killPage, wx.ID_ANY, u"使用NTSD强制结束时教师端会有提示！\n请谨慎使用！\n不建议使用强制删除极域教室的操作。")
        sizer_3.Add(label_4, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.controlPage = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.controlPage, u"限制极域的操作")

        sizer_4 = wx.BoxSizer(wx.VERTICAL)

        self.controlOptionBox = wx.RadioBox(self.controlPage, wx.ID_ANY, u"请选择一个操作", choices=[u"IE全屏窗口化", u"读取极域教室控制密码", u"替换sethc.exe快捷键", u"还原sethc.exe快捷键", u"启动JiYuTrainer"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.controlOptionBox.SetSelection(0)
        sizer_4.Add(self.controlOptionBox, 0, wx.EXPAND, 0)

        self.controlButton = wx.Button(self.controlPage, wx.ID_ANY, u"执行操作")
        sizer_4.Add(self.controlButton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.restorePage = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.restorePage, u"启动极域")

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        self.startOption = wx.RadioBox(self.restorePage, wx.ID_ANY, u"请选择一个操作", choices=[u"从默认安装路径启动", u"PsSuspend恢复进程"], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.startOption.SetSelection(0)
        sizer_2.Add(self.startOption, 0, wx.EXPAND, 0)

        self.startButton = wx.Button(self.restorePage, wx.ID_ANY, u"执行操作")
        sizer_2.Add(self.startButton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.configPage = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.configPage, u"设置")

        sizer_6 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_2 = wx.GridSizer(3, 2, 0, 0)
        sizer_6.Add(grid_sizer_2, 0, 0, 0)
        label_5 = wx.StaticText(self.configPage, wx.ID_ANY, u"极域教室安装路径")
        label_5.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        grid_sizer_2.Add(label_5, 0, wx.ALIGN_CENTER, 0)

        self.installPathText = wx.TextCtrl(self.configPage, wx.ID_ANY, pathToJiYu)
        self.installPathText.SetMinSize((180, 25))
        grid_sizer_2.Add(self.installPathText, 0, wx.ALIGN_CENTER, 0)

        label_6 = wx.StaticText(self.configPage, wx.ID_ANY, u"窗口置顶")
        label_6.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        grid_sizer_2.Add(label_6, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.windowAtTopCheck = wx.CheckBox(self.configPage, wx.ID_ANY, "")
        self.windowAtTopCheck.SetValue(1)
        grid_sizer_2.Add(self.windowAtTopCheck, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.saveButton = wx.Button(self.configPage, wx.ID_ANY, u"保存设置")
        sizer_6.Add(self.saveButton, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.aboutPage = wx.Panel(self.notebook, wx.ID_ANY)
        self.notebook.AddPage(self.aboutPage, u"关于")

        sizer_5 = wx.BoxSizer(wx.VERTICAL)

        logoBmp = wx.StaticBitmap(self.aboutPage, wx.ID_ANY, wx.Bitmap("D:/Michael/Coding/Python/StudentMainManager/image-res/StudentMainManager.ico", wx.BITMAP_TYPE_ANY))
        logoBmp.SetMinSize((64, 64))
        sizer_5.Add(logoBmp, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        label_3 = wx.StaticText(self.aboutPage, wx.ID_ANY, "StudentMain Manager")
        label_3.SetFont(wx.Font(17, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_5.Add(label_3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        label_8 = wx.StaticText(self.aboutPage, wx.ID_ANY, "Version " + version)
        label_8.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_5.Add(label_8, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        label_9 = wx.StaticText(self.aboutPage, wx.ID_ANY, u"开发者：杨舜怀")
        label_9.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_5.Add(label_9, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.viewWebsite = wx.adv.HyperlinkCtrl(self.aboutPage, wx.ID_ANY, u"访问 GitHub 仓库", "https://github.com/yangshunhuai/StudentMainManager")
        self.viewWebsite.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_5.Add(self.viewWebsite, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.viewLicense = wx.adv.HyperlinkCtrl(self.aboutPage, wx.ID_ANY, u"查看开放源代码协议: Apache-2.0 License", "https://github.com/yangshunhuai/StudentMainManager/blob/main/LICENSE")
        self.viewLicense.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_5.Add(self.viewLicense, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.viewTrainerLicense = wx.adv.HyperlinkCtrl(self.aboutPage, wx.ID_ANY, u"查看 JiYuTrainer 开放源代码协议: MIT License", "https://github.com/imengyu/JiYuTrainer/blob/master/LICENSE")
        self.viewTrainerLicense.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_5.Add(self.viewTrainerLicense, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.checkUpdate = wx.adv.HyperlinkCtrl(self.aboutPage, wx.ID_ANY, u"检查 StudentMain Manager 更新", "https://github.com/yangshunhuai/StudentMainManager/releases")
        self.checkUpdate.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_5.Add(self.checkUpdate, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.aboutPage.SetSizer(sizer_5)

        self.configPage.SetSizer(sizer_6)

        self.restorePage.SetSizer(sizer_2)

        self.controlPage.SetSizer(sizer_4)

        self.killPage.SetSizer(sizer_1)

        self.statusPage.SetSizer(grid_sizer_1)

        self.Layout()
        self.Centre()

        self.Bind(wx.EVT_BUTTON, self.executeKill, self.killButton)
        self.Bind(wx.EVT_BUTTON, self.executeControl, self.controlButton)
        self.Bind(wx.EVT_BUTTON, self.executeRestart, self.startButton)
        self.Bind(wx.EVT_BUTTON, self.saveConfig, self.saveButton)
        # end wxGlade
        # Make a new thread for refreshing JiYu's status.
        statusThread = threading.Thread(target=self.refreshStatus(), daemon=True)
        # Start the thread created before.
        statusThread.start()
    def refreshStatus(self):
        jiYuExist, jiYuRunningStatus = utils.getJiYuStatus()
        if jiYuExist:
            self.installStatusText.SetValue('已安装')
        else:
            self.installStatusText.SetValue('未安装')
        if jiYuRunningStatus == 'running':
            self.runStatusText.SetValue('正在运行')
        elif jiYuRunningStatus == 'stopped':
            self.runStatusText.SetValue('被挂起')
        else:
            self.runStatusText.SetValue('不在运行')
        time.sleep(1)
    def executeKill(self, event):  # wxGlade: MainFrame.<event_handler>
        killOption = self.killOptionBox.GetSelection()
        if killOption == 0:
            if utils.NTSDKill() == 1:
                dlg = wx.MessageDialog(self, '没有找到NTSD程序！可能原因如下：\n1. NTSD路径设置错误（检查配置文件）', 'StudentMain Manager 错误', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
        elif killOption == 1:
            result = utils.suspend()
            if result == 0:
                dlg = wx.MessageDialog(self, '挂起成功！', 'StudentMain Manager 提示', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
            elif result == 1:
                dlg = wx.MessageDialog(self, '挂起失败！可能原因如下：\n1. 进程不存在（可能没有安装极域教室）\n2. 权限不足（建议以管理员身份重新运行本程序）', 'StudentMain Manager 提示', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
            else:
                dlg = wx.MessageDialog(self, '没有找到PsSuspend程序！可能原因如下：\n1. PsSuspend路径设置错误（检查配置文件）','StudentMain Manager 错误', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
        elif killOption == 2:
            if utils.trashJiYu() == 1:
                dlg = wx.MessageDialog(self, '极域教室路径设置错误！可能原因如下：\n1. 极域教室路径设置错误（检查配置文件）', 'StudentMain Manager 错误', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
    def executeControl(self, event):  # wxGlade: MainFrame.<event_handler>
        controlOption = self.controlOptionBox.GetSelection()
        if controlOption == 0:
            dlg = wx.MessageDialog(self, '接下来将会打开一个IE窗口，打开之后继续用不要关，当极域教室的广播出现后将会显示为一个窗口，将其最小化即可。\n如果想退出IE，只需按下Win键，右键点击任务栏里的IE并点击关闭窗口即可。', 'StudentMain Manager 提示', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            utils.fullscreenIE()
        elif controlOption == 1:
            password = utils.readPassword()
            if password != None:
                dlg = wx.MessageDialog(self, '极域教室密码为：\n' + password, 'StudentMain Manager 提示', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
            else:
                dlg = wx.MessageDialog(self, '极域教室密码获取失败！可能原因如下：\n1. 极域教室没有安装\n2. 没设密码（可能性不大，没见过有老师不设密码的）', 'StudentMain Manager 错误', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
        elif controlOption == 2:
            dlg = wx.MessageDialog(self, '接下来将替换sethc.exe快捷键程序。\n替换后，在极域控屏的时候按下5次Shift键即可强制关闭极域教室。\n替换时，必须以管理员权限运行本程序。', 'StudentMain Manager 提示', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            if utils.replaceSethc() == 0:
                dlg = wx.MessageDialog(self, '替换成功！', 'StudentMain Manager 提示', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
            else:
                dlg = wx.MessageDialog(self, '替换失败！可能原因如下：\n1. 没有使用管理员权限运行本程序（请右键点击使用管理员身份运行）', 'StudentMain Manager 错误', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
        elif controlOption == 3:
            dlg = wx.MessageDialog(self, '接下来将还原sethc.exe快捷键程序。\n替换后，在极域控屏的时候按下5次Shift键将无法强制关闭极域教室。\n还原时，必须以管理员权限运行本程序。', 'StudentMain Manager 提示', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            if utils.restoreSethc() == 0:
                dlg = wx.MessageDialog(self, '还原成功！', 'StudentMain Manager 提示', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
            else:
                dlg = wx.MessageDialog(self, '还原失败！可能原因如下：\n1. 没有使用管理员权限运行本程序（请右键点击使用管理员身份运行）', 'StudentMain Manager 错误', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
        elif controlOption == 4:
            if utils.launchTrainer() == 1:
                dlg = wx.MessageDialog(self, 'JiYuTrainer启动失败！可能原因如下：\n1. JiYuTrainer路径设置错误（检查配置文件）', 'StudentMain Manager 错误', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
    def executeRestart(self, event):  # wxGlade: MainFrame.<event_handler>
        restartOption = self.startOption.GetSelection()
        if restartOption == 0:
            if utils.launchJiYu() == 1:
                dlg = wx.MessageDialog(self, '极域教室启动失败！可能原因如下：\n1. 极域教室路径设置错误（检查配置文件）', 'StudentMain Manager 错误', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
        elif restartOption == 1:
            result = utils.resume()
            if result == 0:
                dlg = wx.MessageDialog(self, '恢复成功！', 'StudentMain Manager 提示', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
            elif result == 1:
                dlg = wx.MessageDialog(self, '恢复失败！可能原因如下：\n1. 进程不存在（可能没有安装极域教室）\n2. 权限不足（建议以管理员身份重新运行本程序）', 'StudentMain Manager 提示', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
            else:
                dlg = wx.MessageDialog(self, '没有找到PsSuspend程序！可能原因如下：\n1. PsSuspend路径设置错误（检查配置文件）', 'StudentMain Manager 错误', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
    
    def saveConfig(self, event):
        jiyuPath = self.installPathText.GetValue()
        windowOnTop = self.windowAtTopCheck.GetValue()
        utils.writeConfig(jiyuPath, windowOnTop)
        if windowOnTop:
            self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL | wx.STAY_ON_TOP)
        else:
            self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

# end of class MainFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    main = MyApp(0)
    main.locale = wx.Locale(wx.LANGUAGE_CHINESE_SIMPLIFIED)
    main.MainLoop()
