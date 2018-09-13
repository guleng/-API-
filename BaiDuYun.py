#!/usr/bin/env python
# -*- coding: utf-8 -*

import wx
import wx.grid
import ConfigParser
import SignUtils
import uniqid
import requests
import time
from Crypto.Cipher import AES
import logging
import json
from threading import Thread
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1268, 850), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.SetBackgroundColour(wx.Colour(250, 243, 252))

        self.baiduHttp = "http://bcc.bj.baidubce.com"
        self.host = "bcc.bj.baidubce.com"
        self.v = "2"

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_bpButton1 = wx.BitmapButton(self, wx.ID_ANY,
                                           wx.Bitmap(u"1.png", wx.BITMAP_TYPE_ANY),
                                           wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        gbSizer2.Add(self.m_bpButton1, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"     开天创世百度云API工具", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(18, 74, 90, 92, False, "Calibri"))
        self.m_staticText1.SetForegroundColour(wx.Colour(206, 10, 4))

        gbSizer2.Add(self.m_staticText1, wx.GBPosition(0, 1), wx.GBSpan(1, 1),
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gbSizer2, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT | wx.EXPAND, 5)

        self.m_staticline4 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer1.Add(self.m_staticline4, 0, wx.EXPAND | wx.ALL, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        gbSizer6 = wx.GridBagSizer(0, 0)
        gbSizer6.SetFlexibleDirection(wx.BOTH)
        gbSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        #----------
        self.m_radioBtn4 = wx.RadioButton(self, wx.ID_ANY, u"沙巴克", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
        gbSizer6.Add(self.m_radioBtn4, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        #----------

        gSizer13 = wx.GridSizer(1, 2, 0, 0)

        self.m_staticText39 = wx.StaticText(self, wx.ID_ANY, u"专属实例id", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText39.Wrap(-1)
        gSizer13.Add(self.m_staticText39, 0, wx.ALL, 5)

        self.m_textCtrl58 = wx.TextCtrl(self, wx.ID_ANY, u"d-x3Hw**-", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer13.Add(self.m_textCtrl58, 0, wx.ALL, 5)

        gbSizer6.Add(gSizer13, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gSizer131 = wx.GridSizer(1, 2, 0, 0)

        self.m_staticText271 = wx.StaticText(self, wx.ID_ANY, u"   Bcc模板ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText271.Wrap(-1)
        gSizer131.Add(self.m_staticText271, 0, wx.ALL, 5)

        self.m_textCtrl461 = wx.TextCtrl(self, wx.ID_ANY, u"m-b26KxHMG", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer131.Add(self.m_textCtrl461, 0, wx.ALL, 5)

        gbSizer6.Add(gSizer131, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gSizer132 = wx.GridSizer(1, 2, 0, 0)

        self.m_staticText272 = wx.StaticText(self, wx.ID_ANY, u"      Eip名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText272.Wrap(-1)
        gSizer132.Add(self.m_staticText272, 0, wx.ALL, 5)

        self.m_textCtrl462 = wx.TextCtrl(self, wx.ID_ANY, u"s1**1.gs", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer132.Add(self.m_textCtrl462, 0, wx.ALL, 5)

        gbSizer6.Add(gSizer132, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gSizer26 = wx.GridSizer(1, 2, 0, 0)

        self.m_staticText27 = wx.StaticText(self, wx.ID_ANY, u"        CDS模板ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText27.Wrap(-1)
        gSizer26.Add(self.m_staticText27, 0, wx.ALL, 5)

        self.m_textCtrl46 = wx.TextCtrl(self, wx.ID_ANY, u"s-FdqOg1mZ", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer26.Add(self.m_textCtrl46, 0, wx.ALL, 5)

        gbSizer6.Add(gSizer26, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.EXPAND, 5)

        bSizer6.Add(gbSizer6, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT | wx.ALIGN_RIGHT | wx.ALIGN_TOP | wx.ALL | wx.BOTTOM | wx.EXPAND | wx.FIXED_MINSIZE | wx.LEFT | wx.RIGHT | wx.SHAPED | wx.TOP,
                    5)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer6.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        gbSizer61 = wx.GridBagSizer(0, 0)
        gbSizer61.SetFlexibleDirection(wx.BOTH)
        gbSizer61.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        #---------------
        self.m_radioBtn5 = wx.RadioButton(self, wx.ID_ANY, u"y2game", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer61.Add(self.m_radioBtn5, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        #---------------

        gSizer133 = wx.GridSizer(1, 2, 0, 0)

        self.m_staticText392 = wx.StaticText(self, wx.ID_ANY, u"专属实例id", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText392.Wrap(-1)
        gSizer133.Add(self.m_staticText392, 0, wx.ALL, 5)

        self.m_textCtrl581 = wx.TextCtrl(self, wx.ID_ANY, u"d-CRcc3***", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer133.Add(self.m_textCtrl581, 0, wx.ALL, 5)

        gbSizer61.Add(gSizer133, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gSizer1311 = wx.GridSizer(1, 2, 0, 0)

        self.m_staticText2711 = wx.StaticText(self, wx.ID_ANY, u"   Bcc模板ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2711.Wrap(-1)
        gSizer1311.Add(self.m_staticText2711, 0, wx.ALL, 5)

        self.m_textCtrl4611 = wx.TextCtrl(self, wx.ID_ANY, u"m-wnTtGJEF", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1311.Add(self.m_textCtrl4611, 0, wx.ALL, 5)

        gbSizer61.Add(gSizer1311, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gSizer1321 = wx.GridSizer(1, 2, 0, 0)

        self.m_staticText2721 = wx.StaticText(self, wx.ID_ANY, u"      EipName", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2721.Wrap(-1)
        gSizer1321.Add(self.m_staticText2721, 0, wx.ALL, 5)

        self.m_textCtrl4621 = wx.TextCtrl(self, wx.ID_ANY, u"s2**1.gs", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1321.Add(self.m_textCtrl4621, 0, wx.ALL, 5)

        gbSizer61.Add(gSizer1321, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.EXPAND, 5)

        gSizer261 = wx.GridSizer(1, 2, 0, 0)

        self.m_staticText273 = wx.StaticText(self, wx.ID_ANY, u"        CDS模板ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText273.Wrap(-1)
        gSizer261.Add(self.m_staticText273, 0, wx.ALL, 5)

        self.m_textCtrl463 = wx.TextCtrl(self, wx.ID_ANY, u"s-K3YI9wd5", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer261.Add(self.m_textCtrl463, 0, wx.ALL, 5)

        gbSizer61.Add(gSizer261, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.EXPAND, 5)

        bSizer6.Add(gbSizer61, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT | wx.ALIGN_RIGHT | wx.ALIGN_TOP | wx.ALL | wx.BOTTOM | wx.EXPAND | wx.FIXED_MINSIZE | wx.LEFT | wx.RIGHT | wx.SHAPED | wx.TOP, 5)

        self.m_staticline7 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer6.Add(self.m_staticline7, 0, wx.EXPAND | wx.ALL, 5)


        gbSizer8 = wx.GridBagSizer(0, 0)
        gbSizer8.SetFlexibleDirection(wx.BOTH)
        gbSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"DccId"), wx.VERTICAL)

        gSizer11 = wx.GridSizer(7, 2, 0, 0)

        self.m_staticText61 = wx.StaticText(self, wx.ID_ANY, u"专属实例ID:1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        gSizer11.Add(self.m_staticText61, 0, wx.ALL, 5)

        self.m_textCtrl251 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer11.Add(self.m_textCtrl251, 0, wx.ALL, 5)

        self.m_staticText71 = wx.StaticText(self, wx.ID_ANY, u"专属实例ID:2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)
        gSizer11.Add(self.m_staticText71, 0, wx.ALL, 5)

        self.m_textCtrl261 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer11.Add(self.m_textCtrl261, 0, wx.ALL, 5)

        self.m_staticText81 = wx.StaticText(self, wx.ID_ANY, u"专属实例ID:3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText81.Wrap(-1)
        gSizer11.Add(self.m_staticText81, 0, wx.ALL, 5)

        self.m_textCtrl271 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer11.Add(self.m_textCtrl271, 0, wx.ALL, 5)

        self.m_staticText34 = wx.StaticText(self, wx.ID_ANY, u"专属实例ID:4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)
        gSizer11.Add(self.m_staticText34, 0, wx.ALL, 5)

        self.m_textCtrl26 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer11.Add(self.m_textCtrl26, 0, wx.ALL, 5)

        self.m_staticText35 = wx.StaticText(self, wx.ID_ANY, u"专属实例ID:5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        gSizer11.Add(self.m_staticText35, 0, wx.ALL, 5)

        self.m_textCtrl27 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer11.Add(self.m_textCtrl27, 0, wx.ALL, 5)

        self.m_staticText36 = wx.StaticText(self, wx.ID_ANY, u"专属实例ID:6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText36.Wrap(-1)
        gSizer11.Add(self.m_staticText36, 0, wx.ALL, 5)

        self.m_textCtrl28 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer11.Add(self.m_textCtrl28, 0, wx.ALL, 5)

        self.m_staticText421 = wx.StaticText(self, wx.ID_ANY, u"专属实例ID:7", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText421.Wrap(-1)
        gSizer11.Add(self.m_staticText421, 0, wx.ALL, 5)
        self.m_textCtrl23 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer11.Add(self.m_textCtrl23, 0, wx.ALL, 5)
        sbSizer1.Add(gSizer11, 0, 0, 5)

        gbSizer8.Add(sbSizer1, wx.GBPosition(0, 0), wx.GBSpan(1, 1), 0, 5)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Bcc名"), wx.VERTICAL)

        gSizer111 = wx.GridSizer(7, 2, 0, 0)

        self.m_staticText611 = wx.StaticText(self, wx.ID_ANY, u"Bcc名:1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText611.Wrap(-1)
        gSizer111.Add(self.m_staticText611, 0, wx.ALL, 5)

        self.m_textCtrl2511 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer111.Add(self.m_textCtrl2511, 0, wx.ALL, 5)

        self.m_staticText711 = wx.StaticText(self, wx.ID_ANY, u"Bcc名:2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText711.Wrap(-1)
        gSizer111.Add(self.m_staticText711, 0, wx.ALL, 5)

        self.m_textCtrl2611 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer111.Add(self.m_textCtrl2611, 0, wx.ALL, 5)

        self.m_staticText811 = wx.StaticText(self, wx.ID_ANY, u"Bcc名:3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText811.Wrap(-1)
        gSizer111.Add(self.m_staticText811, 0, wx.ALL, 5)

        self.m_textCtrl29 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer111.Add(self.m_textCtrl29, 0, wx.ALL, 5)

        self.m_staticText38 = wx.StaticText(self, wx.ID_ANY, u"Bcc名:4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText38.Wrap(-1)
        gSizer111.Add(self.m_staticText38, 0, wx.ALL, 5)

        self.m_textCtrl30 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer111.Add(self.m_textCtrl30, 0, wx.ALL, 5)

        self.m_staticText391 = wx.StaticText(self, wx.ID_ANY, u"Bcc名:5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText391.Wrap(-1)
        gSizer111.Add(self.m_staticText391, 0, wx.ALL, 5)

        self.m_textCtrl31 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer111.Add(self.m_textCtrl31, 0, wx.ALL, 5)

        self.m_staticText40 = wx.StaticText(self, wx.ID_ANY, u"Bcc名:6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText40.Wrap(-1)
        gSizer111.Add(self.m_staticText40, 0, wx.ALL, 5)

        self.m_textCtrl32 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer111.Add(self.m_textCtrl32, 0, wx.ALL, 5)

        self.m_staticText431 = wx.StaticText(self, wx.ID_ANY, u"Bcc名:7", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText431.Wrap(-1)
        gSizer111.Add(self.m_staticText431, 0, wx.ALL, 5)
        self.m_textCtrl24 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer111.Add(self.m_textCtrl24, 0, wx.ALL, 5)
        sbSizer2.Add(gSizer111, 1, wx.EXPAND, 5)

        gbSizer8.Add(sbSizer2, wx.GBPosition(0, 1), wx.GBSpan(1, 1), 0, 5)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Eip名"), wx.VERTICAL)

        gSizer112 = wx.GridSizer(7, 2, 0, 0)

        self.m_staticText612 = wx.StaticText(self, wx.ID_ANY, u"Eip名:1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText612.Wrap(-1)
        gSizer112.Add(self.m_staticText612, 0, wx.ALL, 5)

        self.m_textCtrl2512 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer112.Add(self.m_textCtrl2512, 0, wx.ALL, 5)

        self.m_staticText712 = wx.StaticText(self, wx.ID_ANY, u"Eip名:2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText712.Wrap(-1)
        gSizer112.Add(self.m_staticText712, 0, wx.ALL, 5)

        self.m_textCtrl2612 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer112.Add(self.m_textCtrl2612, 0, wx.ALL, 5)

        self.m_staticText812 = wx.StaticText(self, wx.ID_ANY, u"Eip名:3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText812.Wrap(-1)
        gSizer112.Add(self.m_staticText812, 0, wx.ALL, 5)

        self.m_textCtrl2712 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer112.Add(self.m_textCtrl2712, 0, wx.ALL, 5)

        self.m_staticText42 = wx.StaticText(self, wx.ID_ANY, u"Eip名:4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText42.Wrap(-1)
        gSizer112.Add(self.m_staticText42, 0, wx.ALL, 5)

        self.m_textCtrl34 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer112.Add(self.m_textCtrl34, 0, wx.ALL, 5)

        self.m_staticText43 = wx.StaticText(self, wx.ID_ANY, u"Eip名:5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText43.Wrap(-1)
        gSizer112.Add(self.m_staticText43, 0, wx.ALL, 5)

        self.m_textCtrl35 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer112.Add(self.m_textCtrl35, 0, wx.ALL, 5)

        self.m_staticText44 = wx.StaticText(self, wx.ID_ANY, u"Eip名:6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText44.Wrap(-1)
        gSizer112.Add(self.m_staticText44, 0, wx.ALL, 5)

        self.m_textCtrl36 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer112.Add(self.m_textCtrl36, 0, wx.ALL, 5)

        self.m_staticText441 = wx.StaticText(self, wx.ID_ANY, u"Eip名:7", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText441.Wrap(-1)
        gSizer112.Add(self.m_staticText441, 0, wx.ALL, 5)
        self.m_textCtrl25 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer112.Add(self.m_textCtrl25, 0, wx.ALL, 5)
        sbSizer5.Add(gSizer112, 1, 0, 5)

        gbSizer8.Add(sbSizer5, wx.GBPosition(0, 2), wx.GBSpan(1, 1), 0, 5)

        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"CDS"), wx.VERTICAL)

        gSizer113 = wx.GridSizer(7, 2, 0, 0)

        self.m_staticText613 = wx.StaticText(self, wx.ID_ANY, u"CDS:1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText613.Wrap(-1)
        gSizer113.Add(self.m_staticText613, 1, wx.ALL | wx.EXPAND, 5)

        m_comboBox2Choices = [u"yes        ", u"no        "]
        self.m_comboBox2 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices,
                                       0)
        gSizer113.Add(self.m_comboBox2, 0, wx.ALL, 5)

        self.m_staticText23 = wx.StaticText(self, wx.ID_ANY, u"CDS:2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        gSizer113.Add(self.m_staticText23, 0, wx.ALL, 5)

        m_comboBox3Choices = [u"yes        ", u"no        "]
        self.m_comboBox3 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices,
                                       0)
        gSizer113.Add(self.m_comboBox3, 0, wx.ALL, 5)

        self.m_staticText24 = wx.StaticText(self, wx.ID_ANY, u"CDS:3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)
        gSizer113.Add(self.m_staticText24, 0, wx.ALL, 5)

        m_comboBox4Choices = [u"yes        ", u"no        "]
        self.m_comboBox4 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox4Choices,
                                       0)
        gSizer113.Add(self.m_comboBox4, 0, wx.ALL, 5)

        self.m_staticText45 = wx.StaticText(self, wx.ID_ANY, u"CDS:4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText45.Wrap(-1)
        gSizer113.Add(self.m_staticText45, 0, wx.ALL, 5)

        m_comboBox5Choices = [u"yes        ", u"no        "]
        self.m_comboBox5 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox5Choices,
                                       0)
        gSizer113.Add(self.m_comboBox5, 0, wx.ALL, 5)

        self.m_staticText47 = wx.StaticText(self, wx.ID_ANY, u"CDS:5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText47.Wrap(-1)
        gSizer113.Add(self.m_staticText47, 0, wx.ALL, 5)

        m_comboBox6Choices = [u"yes        ", u"no        "]
        self.m_comboBox6 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox6Choices,
                                       0)
        gSizer113.Add(self.m_comboBox6, 0, wx.ALL, 5)

        self.m_staticText48 = wx.StaticText(self, wx.ID_ANY, u"CDS:6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText48.Wrap(-1)
        gSizer113.Add(self.m_staticText48, 0, wx.ALL, 5)

        m_comboBox7Choices = [u"yes        ", u"no        "]
        self.m_comboBox7 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox7Choices,
                                       0)
        gSizer113.Add(self.m_comboBox7, 0, wx.ALL, 5)

        self.m_staticText452 = wx.StaticText(self, wx.ID_ANY, u"CDS:7", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText452.Wrap(-1)
        gSizer113.Add(self.m_staticText452, 0, wx.ALL, 5)
        m_comboBox19Choices = [u"yes        ", u"no        "]
        self.m_comboBox19 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox19Choices,
                                        0)
        gSizer113.Add(self.m_comboBox19, 0, wx.ALL, 5)
        sbSizer6.Add(gSizer113, 1, 0, 5)

        gbSizer8.Add(sbSizer6, wx.GBPosition(0, 3), wx.GBSpan(1, 1), 0, 5)

        #------------------
        sbSizer62 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"安全组"), wx.VERTICAL)

        gSizer1131 = wx.GridSizer(7, 2, 0, 0)

        self.m_staticText6131 = wx.StaticText(self, wx.ID_ANY, u"安全组:1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6131.Wrap(-1)
        gSizer1131.Add(self.m_staticText6131, 1, wx.ALL | wx.EXPAND, 5)

        m_comboBox21Choices = [u"安卓_gs", u"IOS_gs", u"越狱_gs", u"cross", u"默认安全组"]
        self.m_comboBox21 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox21Choices,
                                        0)
        gSizer1131.Add(self.m_comboBox21, 0, wx.ALL, 5)

        self.m_staticText231 = wx.StaticText(self, wx.ID_ANY, u"安全组:2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText231.Wrap(-1)
        gSizer1131.Add(self.m_staticText231, 0, wx.ALL, 5)

        m_comboBox31Choices = [u"安卓_gs", u"IOS_gs", u"越狱_gs", u"cross", u"默认安全组"]
        self.m_comboBox31 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox31Choices,
                                        0)
        gSizer1131.Add(self.m_comboBox31, 0, wx.ALL, 5)

        self.m_staticText241 = wx.StaticText(self, wx.ID_ANY, u"安全组:3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText241.Wrap(-1)
        gSizer1131.Add(self.m_staticText241, 0, wx.ALL, 5)

        m_comboBox41Choices = [u"安卓_gs", u"IOS_gs", u"越狱_gs", u"cross", u"默认安全组"]
        self.m_comboBox41 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox41Choices,
                                        0)
        gSizer1131.Add(self.m_comboBox41, 0, wx.ALL, 5)

        self.m_staticText451 = wx.StaticText(self, wx.ID_ANY, u"安全组:4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText451.Wrap(-1)
        gSizer1131.Add(self.m_staticText451, 0, wx.ALL, 5)

        m_comboBox51Choices = [u"安卓_gs", u"IOS_gs", u"越狱_gs", u"cross", u"默认安全组"]
        self.m_comboBox51 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox51Choices,
                                        0)
        gSizer1131.Add(self.m_comboBox51, 0, wx.ALL, 5)

        self.m_staticText471 = wx.StaticText(self, wx.ID_ANY, u"安全组:5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText471.Wrap(-1)
        gSizer1131.Add(self.m_staticText471, 0, wx.ALL, 5)

        m_comboBox61Choices = [u"安卓_gs", u"IOS_gs", u"越狱_gs", u"cross", u"默认安全组"]
        self.m_comboBox61 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox61Choices,
                                        0)
        gSizer1131.Add(self.m_comboBox61, 0, wx.ALL, 5)

        self.m_staticText481 = wx.StaticText(self, wx.ID_ANY, u"安全组:6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText481.Wrap(-1)
        gSizer1131.Add(self.m_staticText481, 0, wx.ALL, 5)

        m_comboBox71Choices = [u"安卓_gs", u"IOS_gs", u"越狱_gs", u"cross", u"默认安全组"]
        self.m_comboBox71 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox71Choices,
                                        0)
        gSizer1131.Add(self.m_comboBox71, 0, wx.ALL, 5)

        self.m_staticText46 = wx.StaticText(self, wx.ID_ANY, u"安全组:7", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText46.Wrap(-1)
        gSizer1131.Add(self.m_staticText46, 0, wx.ALL, 5)
        m_comboBox20Choices = [u"安卓_gs", u"IOS_gs", u"越狱_gs", u"cross", u"默认安全组"]
        self.m_comboBox20 = wx.ComboBox(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, m_comboBox20Choices,
                                        0)
        gSizer1131.Add(self.m_comboBox20, 0, wx.ALL, 5)
        sbSizer62.Add(gSizer1131, 1, 0, 5)

        gbSizer8.Add(sbSizer62, wx.GBPosition(0, 5), wx.GBSpan(1, 1), 0, 5)
        #------------------

        sbSizer61 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"创建"), wx.VERTICAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.Size(-1, 25), 0)
        sbSizer61.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.Size(-1, 25), 0)
        sbSizer61.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.Size(-1, 25), 0)
        sbSizer61.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.Size(-1, 25), 0)
        sbSizer61.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.Size(-1, 25), 0)
        sbSizer61.Add(self.m_button5, 0, wx.ALL, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.Size(-1, 25), 0)
        sbSizer61.Add(self.m_button6, 0, wx.ALL, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.Size(-1, 25), 0)
        sbSizer61.Add(self.m_button7, 0, wx.ALL, 5)

        gbSizer8.Add(sbSizer61, wx.GBPosition(0, 6), wx.GBSpan(1, 1), 0, 5)

        bSizer6.Add(gbSizer8, 0, wx.EXPAND, 5)

        self.m_staticline7 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer6.Add(self.m_staticline7, 0, wx.EXPAND | wx.ALL, 5)

        gSizer114 = wx.GridSizer(1, 2, 0, 0)

        self.m_staticText50 = wx.StaticText(self, wx.ID_ANY, u"所有的空格里的值(大小写字母、数字以及-_ /.特殊字符，必须以字母开头，长度1-65)",
                                            wx.DefaultPosition, wx.DefaultSize, 0 | wx.DOUBLE_BORDER)
        self.m_staticText50.Wrap(-1)
        self.m_staticText50.SetFont(wx.Font(11, 71, 90, 92, False, wx.EmptyString))
        self.m_staticText50.SetForegroundColour(wx.Colour(255, 0, 0))
        self.m_staticText50.SetBackgroundColour(wx.Colour(2, 2, 2))

        bSizer6.Add(self.m_staticText50, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer6.Add(gSizer114, 0, wx.ALIGN_CENTER, 5)

        sbSizer51 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"info"), wx.VERTICAL)

        self.m_grid1 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid1.CreateGrid(7, 8)
        self.m_grid1.EnableEditing(True)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.SetGridLineColour(wx.Colour(255, 255, 215))
        self.m_grid1.EnableDragGridSize(True)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.SetColSize(0, 141)
        self.m_grid1.SetColSize(1, 141)
        self.m_grid1.SetColSize(2, 141)
        self.m_grid1.SetColSize(3, 142)
        self.m_grid1.SetColSize(4, 142)
        self.m_grid1.SetColSize(5, 142)
        self.m_grid1.SetColSize(6, 141)
        self.m_grid1.SetColSize(7, 141)
        self.m_grid1.EnableDragColMove(True)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelSize(30)
        self.m_grid1.SetColLabelValue(0, u"BccName")
        self.m_grid1.SetColLabelValue(1, u"BccStatus")
        self.m_grid1.SetColLabelValue(2, u"EipName")
        self.m_grid1.SetColLabelValue(3, u"Eip")
        self.m_grid1.SetColLabelValue(4, u"EipMount")
        self.m_grid1.SetColLabelValue(5, u"CdsStatus")
        self.m_grid1.SetColLabelValue(6, u"CdsMount")
        self.m_grid1.SetColLabelValue(7, u"SecurityGroup")
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid1.SetRowSize(0, 40)
        self.m_grid1.SetRowSize(1, 40)
        self.m_grid1.SetRowSize(2, 40)
        self.m_grid1.SetRowSize(3, 40)
        self.m_grid1.SetRowSize(4, 40)
        self.m_grid1.SetRowSize(5, 40)
        self.m_grid1.SetRowSize(6, 40)
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelSize(90)
        self.m_grid1.SetRowLabelValue(0, u"实例1")
        self.m_grid1.SetRowLabelValue(1, u"实例2")
        self.m_grid1.SetRowLabelValue(2, u"实例3")
        self.m_grid1.SetRowLabelValue(3, u"实例4")
        self.m_grid1.SetRowLabelValue(4, u"实例5")
        self.m_grid1.SetRowLabelValue(5, u"实例6")
        self.m_grid1.SetRowLabelValue(6, u"实例7")
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.m_grid1.SetLabelBackgroundColour(wx.Colour(193, 168, 198))
        self.m_grid1.SetLabelTextColour(wx.Colour(128, 64, 64))

        # Cell Defaults
        self.m_grid1.SetDefaultCellBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.m_grid1.SetDefaultCellTextColour(wx.Colour(0, 213, 0))
        self.m_grid1.SetDefaultCellFont(wx.Font(11, 70, 90, 92, False, wx.EmptyString))
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        sbSizer51.Add(self.m_grid1, 0, wx.ALL, 5)

        self.m_staticline8 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        sbSizer51.Add(self.m_staticline8, 0, wx.EXPAND | wx.ALL, 5)

        bSizer6.Add(sbSizer51, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer6, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.ok1)
        self.m_button2.Bind(wx.EVT_BUTTON, self.ok2)
        self.m_button3.Bind(wx.EVT_BUTTON, self.ok3)
        self.m_button4.Bind(wx.EVT_BUTTON, self.ok4)
        self.m_button5.Bind(wx.EVT_BUTTON, self.ok5)
        self.m_button6.Bind(wx.EVT_BUTTON, self.ok6)
        self.m_button7.Bind(wx.EVT_BUTTON, self.OK7)

    def __del__(self):
        pass

    """
    认证文件的AK,SK
    """
    def Sign_key(self, ak, sk):
        self.ak = ak
        self.sk = sk

        # 初始化ak,sk类信息
        self.credentials = SignUtils.BceCredentials(self.ak, self.sk)


    """
    创建BCC
    """
    def createInstance(self, DCC, BccName, BccimageId, passwd):
        pad_it = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
        key = self.sk[0:16]
        mode = AES.MODE_ECB
        cryptor = AES.new(key, mode, key)
        cipheradminpass = cryptor.encrypt(pad_it(passwd)).encode('hex')
        Bbody = {
            "instanceType": "bcc.g1.medium",
            "ephemeralDisks": [{
                "storageType": "SSD",
                "sizeInGB": 40}],
            "adminPass": str(cipheradminpass),
            "name": BccName,
            "imageId": BccimageId,
            "localDiskSizeInGB": 40,
            "networkCapacityInMbps": 0,
            "dedicatedHostId": DCC,
            "purchaseCount": 1,
            "billing": {
                "paymentTiming": "Postpaid"}
            # "securityGroupId": "g-xDFsHlEy"
        }

        # 生成clentToken
        clientToken = uniqid.uniqid('', 'true')
        path = "/v2/instance"
        param = {
            'clientToken': clientToken
        }
        timestamp = int(time.time())
        headers = {
            "host": self.host,
            "Content-Type": "application/json",
            "x-bce-date": SignUtils.get_canonical_time(timestamp)
        }
        http_method = "POST"
        result = SignUtils.sign(self.credentials, http_method, path, headers, param, timestamp, 60, {"host", "x-bce-date"})
        headers["Authorization"] = result
        reques = requests.post(self.baiduHttp + "/v2/instance?clientToken=" + clientToken, headers=headers, json=Bbody)
        return reques.status_code, reques.text
        reques.close()

    '''
        获取实例详情
    '''
    def getInstanceDetail(self, instanceId):
        http_method = "GET"
        path = "/v" + self.v + "/instance/" + instanceId
        timestamp = int(time.time())
        headers = {
            "host": self.host,
            "Content-Type": "application/json",
            "x-bce-date": SignUtils.get_canonical_time(timestamp)
        }
        result = SignUtils.sign(self.credentials, http_method, path, headers, {}, timestamp)
        headers["Authorization"] = result
        reques = requests.get(self.baiduHttp + path, headers=headers)
        k = reques.text
        pp = json.loads(str(k.encode("utf-8")))["instance"]["status"]
        return reques.status_code, pp
        reques.close()

    """
        创建DCS
    """
    def createDCS(self, CdsimageId):
        Dbody = {
            "storageType": "std1",
            "cdsSizeInGB": 50,
            "purchaseCount": 1,
            "snapshotId": CdsimageId,
            "billing": {
                "paymentTiming": "Postpaid"
            }
        }
        # 生成clentToken
        clientToken = uniqid.uniqid('', 'true')
        path = "/v2/volume"
        param = {
            'clientToken': clientToken
        }
        timestamp = int(time.time())
        headers = {
            "host": self.host,
            "Content-Type": "application/json",
            "x-bce-date": SignUtils.get_canonical_time(timestamp)
        }
        http_method = "POST"
        result = SignUtils.sign(self.credentials, http_method, path, headers, param, timestamp, 60, {"host", "x-bce-date"})
        headers["Authorization"] = result
        reques = requests.post(self.baiduHttp + "/v2/volume?clientToken=" + clientToken, headers=headers, json=Dbody)
        return reques.status_code, reques.text
        reques.close()

        """
            查看CDS实例详情
        """

    def GetCDSinfo(self, VID):
        path = "/v2/volume/" + VID
        param = {}
        timestamp = int(time.time())
        headers = {
            "host": self.host,
            "Content-Type": "application/json",
            "x-bce-date": SignUtils.get_canonical_time(timestamp)
        }
        http_method = "GET"
        result = SignUtils.sign(self.credentials, http_method, path, headers, param, timestamp, 60, {"host", "x-bce-date"})
        headers["Authorization"] = result
        reques = requests.get(self.baiduHttp + path, headers=headers)
        s = json.dumps(reques.text)
        ss = s.replace('false', '\\"false\\"')
        BccI = json.loads(ss)
        BccId = json.loads(BccI)
        status = BccId['volume']['status']
        return reques.status_code, status
        reques.close()

    """
        创建EIP
    """
    def createEIP(self, EipName):
        Ebody = {
            "name": EipName,
            "bandwidthInMbps": 50,
            "billing": {
                "paymentTiming": "Postpaid",
                "billingMethod": "ByTraffic"
            }
        }
        baiduHttp = "http://eip.bj.baidubce.com"
        host = "eip.bj.baidubce.com"
        # 生成clentToken
        clientToken = uniqid.uniqid('', 'true')
        path = "/v1/eip"
        param = {
            'clientToken': clientToken
        }
        timestamp = int(time.time())
        headers = {
            "host": host,
            "Content-Type": "application/json",
            "x-bce-date": SignUtils.get_canonical_time(timestamp)
        }
        http_method = "POST"
        result = SignUtils.sign(self.credentials, http_method, path, headers, param, timestamp, 60, {"host", "x-bce-date"})
        headers["Authorization"] = result
        reques = requests.post(baiduHttp + "/v1/eip?clientToken=" + clientToken, headers=headers, json=Ebody)
        return reques.status_code, reques.text
        reques.close()

    """
        绑定EIP
    """

    def mountEIP(self, BccId, EIP):
        # 生成clentToken
        clientToken = uniqid.uniqid('', 'true')
        baiduHttp = "http://eip.bj.baidubce.com"
        host = "eip.bj.baidubce.com"
        path = "/v1/eip/" + EIP
        param = {'bind': '',
                 'clientToken': clientToken
                 }
        timestamp = int(time.time())
        headers = {
            "host": host,
            "Content-Type": "application/json",
            "x-bce-date": SignUtils.get_canonical_time(timestamp)
        }
        http_method = "PUT"
        result = SignUtils.sign(self.credentials, http_method, path, headers, param, timestamp, 60, {"host", "x-bce-date"})
        headers["Authorization"] = result
        body = {"instanceType": "BCC",
                "instanceId": BccId
                }
        reques = requests.put(baiduHttp + path + "?bind&clientToken=" + clientToken, headers=headers, json=body)
        return reques.status_code, reques.text
        reques.close()

    """
        挂在CDS实例
    """

    def mountCDS(self, CDSID, BCCID):
        path = "/v2/volume/" + CDSID
        param = {'attach': ''}
        timestamp = int(time.time())
        headers = {
            "host": self.host,
            "Content-Type": "application/json",
            "x-bce-date": SignUtils.get_canonical_time(timestamp)
        }
        http_method = "PUT"
        result = SignUtils.sign(self.credentials, http_method, path, headers, param, timestamp, 60, {"host", "x-bce-date"})
        headers["Authorization"] = result
        body = {"instanceId": BCCID}
        reques = requests.put(self.baiduHttp + path + "?attach", headers=headers, json=body)
        return reques.status_code, reques.text
        reques.close()

    """
        实例加入安全组
    """

    def addInstanceSec(self, secId, BccId):
        path = "/v2/instance/" + BccId
        param = {'bind': ''}
        timestamp = int(time.time())
        headers = {
            "host": self.host,
            "Content-Type": "application/json",
            "x-bce-date": SignUtils.get_canonical_time(timestamp)
        }
        http_method = "PUT"
        result = SignUtils.sign(self.credentials, http_method, path, headers, param, timestamp, 60, {"host", "x-bce-date"})
        body = {
                "securityGroupId": secId
                }
        headers["Authorization"] = result
        reques = requests.put(self.baiduHttp + path + "?bind", headers=headers, json=body)
        return reques.status_code, reques.text
        reques.close()


    logging.basicConfig(level=logging.NOTSET, filename='BccUtils.log', format='%(asctime)-10s %(levelname)s %(message)s')
    # Virtual event handlers, overide them in your derived class
    def ok11(self):

        # 读取配置文件
        config = ConfigParser.ConfigParser()
        config.read("config.cfg")

        if self.m_radioBtn4.GetValue()  == True:
            ak = config.get("sbk_config", "ak")
            sk = config.get("sbk_config", "sk")
            xiangmu = "沙巴克"
        else:
            ak = config.get("y2game_config", "ak")
            sk = config.get("y2game_config", "sk")
            xiangmu = "y2game"

        # 初始化ak,sk类信息
        self.Sign_key(ak, sk)

        DCC1 = self.m_textCtrl251.GetValue()
        if str(DCC1[0]) in '1234567890':
            self.m_textCtrl251.SetValue(u"数字开头！" + DCC1)
            assert False

        BccName1 = self.m_textCtrl2511.GetValue()
        if str(BccName1[0]) in '1234567890':
            self.m_textCtrl2511.SetValue(u"数字开头！" + BccName1)
            assert False
        self.m_grid1.SetCellValue(0, 0, BccName1)

        EipName1 = self.m_textCtrl2512.GetValue()
        if str(EipName1[0]) in '1234567890':
            self.m_textCtrl2512.SetValue(u"数字开头！"  +EipName1)
            assert False
        self.m_grid1.SetCellValue(0, 2, EipName1)

        Sec1 = self.m_comboBox21.GetValue().encode("utf-8")

        if self.m_radioBtn4.GetValue() == True:
            BccimageId = self.m_textCtrl461.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl461.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "s3@EwwwwwwVga"

            CdsimageId = self.m_textCtrl46.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl46.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec1 == "安卓_gs":
                SecId = "g-k8wUmJRs"
            elif Sec1 == "IOS_gs":
                SecId = "g-u5UoWLlG"
            elif Sec1 == "越狱_gs":
                SecId = "g-birc2UX2"
            elif Sec1 == "cross":
                SecId = "g-cvUO4Azr"
            else:
                SecId = "g-BGEHzEIX"

        else:
            BccimageId = self.m_textCtrl4611.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl4611.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "@kdssss35a"

            CdsimageId = self.m_textCtrl463.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl463.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec1 == "安卓_gs":
                SecId = "g-ponf77kU"
            elif Sec1 == "IOS_gs":
                SecId = "g-XACjQ0m5"
            elif Sec1 == "越狱_gs":
                SecId = "g-Z969fwDv"
            elif Sec1 == "cross":
                SecId = "g-KJpH38Rh"
            else:
                SecId = "g-xDFsHlEy"


        logging.info("**项目1***" + xiangmu + "BCC创建" + "--" + str(BccName1).encode("utf-8"))
        BCC_conde, Bcc_text = self.createInstance(DCC1, BccName1, BccimageId, passwd)
        self.m_grid1.SetCellValue(0, 1, str(BCC_conde))
        logging.info(str(BCC_conde) + "--" + Bcc_text)
        logging.info("---------------------" +"\n")

        if BCC_conde == 200 :
            assert True
        else:
            self.m_grid1.SetCellValue(0, 1, str("DccID Error"))
            assert False

        BccId = json.loads(str(Bcc_text.encode("utf-8")))["instanceIds"][0]

        logging.info("**项目1***" + xiangmu + "EIP创建" + "--" + str(BccName1).encode("utf-8"))
        EIP_conde, EIP_text = self.createEIP(EipName1)
        logging.info(str(EIP_conde) + "--" +EIP_text )
        logging.info("---------------------" +"\n")

        EIP = json.loads(str(EIP_text.encode("utf-8")))["eip"]
        self.m_grid1.SetCellValue(0, 3, str(EIP))

        Cds1 = self.m_comboBox2.GetValue().encode("utf-8")

        if 'yes        ' == Cds1:
            logging.info("**项目1***" + xiangmu + "CDS创建" + "--" + str(BccName1).encode("utf-8"))
            CDS_conde, CDS_text = self.createDCS(CdsimageId)
            self.m_grid1.SetCellValue(0, 5, str(CDS_conde))
            logging.info(str(CDS_conde) + "--" + CDS_text)
            logging.info("---------------------" + "\n")



        while True:
            Bcc_status_code, BCC_status_text = self.getInstanceDetail(BccId)
            if BCC_status_text == "Running":
                logging.info("**项目1***" + xiangmu + "BCC加入安全组" + "--" + str(BccName1).encode("utf-8"))
                Sec_add_conde, Sec_add_text = self.addInstanceSec(SecId, BccId)
                self.m_grid1.SetCellValue(0, 7, str(Sec_add_conde))
                logging.info(str(Sec_add_conde) + "--" + Sec_add_text)
                logging.info("---------------------" +"\n")


                logging.info("**项目1***" + xiangmu + "EIP挂载" + "--" + str(BccName1).encode("utf-8"))
                Eip_mount_conde, Eip_mount_text = self.mountEIP(BccId, EIP)
                self.m_grid1.SetCellValue(0, 4, str(Eip_mount_conde))
                logging.info(str(Eip_mount_conde) + "--" + Eip_mount_text)
                logging.info("---------------------" +"\n")

                break
            else:
                time.sleep(30)

        while True:
            CDSID = json.loads(str(CDS_text.encode("utf-8")))["volumeIds"][0]
            CDS_s_conde, CDS_s_text = self.GetCDSinfo(CDSID)
            if CDS_conde == 200 and CDS_s_text == "Available":
                logging.info("**项目1***" + xiangmu + "CDS挂载" + "--" + str(BccName1).encode("utf-8"))
                Cds_mount_conde, Cds_mount_text = self.mountCDS(CDSID, BccId)
                self.m_grid1.SetCellValue(0, 6, str(Cds_mount_conde))
                logging.info(str(Cds_mount_conde) + "--" + Cds_mount_text)
                logging.info("---------------------" + "\n")

                break
            else:
                time.sleep(30)


    def ok1(self, event):
        t = Thread(target=self.ok11)
        t.start()

    def ok22(self):

        # 读取配置文件
        config = ConfigParser.ConfigParser()
        config.read("config.cfg")

        if self.m_radioBtn4.GetValue()  == True:
            ak = config.get("sbk_config", "ak")
            sk = config.get("sbk_config", "sk")
            xiangmu = "沙巴克"
        else:
            ak = config.get("y2game_config", "ak")
            sk = config.get("y2game_config", "sk")
            xiangmu = "y2game"

        # 初始化ak,sk类信息
        self.Sign_key(ak, sk)

        DCC = self.m_textCtrl261.GetValue()
        if str(DCC[0]) in '1234567890':
            self.m_textCtrl261.SetValue(u"数字开头！" + DCC)
            assert False

        BccName = self.m_textCtrl2611.GetValue()
        if str(BccName[0]) in '1234567890':
            self.m_textCtrl2611.SetValue(u"数字开头！" + BccName)
            assert False
        self.m_grid1.SetCellValue(1, 0, BccName)

        EipName = self.m_textCtrl2612.GetValue()
        if str(EipName[0]) in '1234567890':
            self.m_textCtrl2612.SetValue(u"数字开头！"  +EipName)
            assert False
        self.m_grid1.SetCellValue(1, 2, EipName)

        Sec = self.m_comboBox31.GetValue().encode("utf-8")

        if self.m_radioBtn4.GetValue() == True:
            BccimageId = self.m_textCtrl461.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl461.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "s3@Esssssg8Vga"

            CdsimageId = self.m_textCtrl46.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl46.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec == "安卓_gs":
                SecId = "g-k8wUmJRs"
            elif Sec == "IOS_gs":
                SecId = "g-u5UoWLlG"
            elif Sec == "越狱_gs":
                SecId = "g-birc2UX2"
            elif Sec == "cross":
                SecId = "g-cvUO4Azr"
            else:
                SecId = "g-BGEHzEIX"

        else:
            BccimageId = self.m_textCtrl4611.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl4611.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "@kd2222222acs5a"

            CdsimageId = self.m_textCtrl463.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl463.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec == "安卓_gs":
                SecId = "g-ponf77kU"
            elif Sec == "IOS_gs":
                SecId = "g-XACjQ0m5"
            elif Sec == "越狱_gs":
                SecId = "g-Z969fwDv"
            elif Sec == "cross":
                SecId = "g-KJpH38Rh"
            else:
                SecId = "g-xDFsHlEy"


        logging.info("**项目2***" + xiangmu + "BCC创建" + "--" + str(BccName).encode("utf-8"))
        BCC_conde, Bcc_text = self.createInstance(DCC, BccName, BccimageId, passwd)
        self.m_grid1.SetCellValue(1, 1, str(BCC_conde))
        logging.info(str(BCC_conde) + "--" + Bcc_text)
        logging.info("---------------------" +"\n")

        if BCC_conde == 200 :
            assert True
        else:
            self.m_grid1.SetCellValue(1, 1, str("DccID Error"))
            assert False

        BccId = json.loads(str(Bcc_text.encode("utf-8")))["instanceIds"][0]

        logging.info("**项目2***" + xiangmu + "EIP创建" + "--" + str(BccName).encode("utf-8"))
        EIP_conde, EIP_text = self.createEIP(EipName)
        logging.info(str(EIP_conde) + "--" +EIP_text )
        logging.info("---------------------" +"\n")

        EIP = json.loads(str(EIP_text.encode("utf-8")))["eip"]
        self.m_grid1.SetCellValue(1, 3, str(EIP))

        Cds = self.m_comboBox3.GetValue().encode("utf-8")

        if 'yes        ' == Cds:
            logging.info("**项目2***" + xiangmu + "CDS创建" + "--" + str(BccName).encode("utf-8"))
            CDS_conde, CDS_text = self.createDCS(CdsimageId)
            self.m_grid1.SetCellValue(1, 5, str(CDS_conde))
            logging.info(str(CDS_conde) + "--" + CDS_text)
            logging.info("---------------------" + "\n")



        while True:
            Bcc_status_code, BCC_status_text = self.getInstanceDetail(BccId)
            if BCC_status_text == "Running":
                logging.info("**项目2***" + xiangmu + "BCC加入安全组" + "--" + str(BccName).encode("utf-8"))
                Sec_add_conde, Sec_add_text = self.addInstanceSec(SecId, BccId)
                self.m_grid1.SetCellValue(1, 7, str(Sec_add_conde))
                logging.info(str(Sec_add_conde) + "--" + Sec_add_text)
                logging.info("---------------------" +"\n")


                logging.info("**项目2***" + xiangmu + "EIP挂载" + "--" + str(BccName).encode("utf-8"))
                Eip_mount_conde, Eip_mount_text = self.mountEIP(BccId, EIP)
                self.m_grid1.SetCellValue(1, 4, str(Eip_mount_conde))
                logging.info(str(Eip_mount_conde) + "--" + Eip_mount_text)
                logging.info("---------------------" +"\n")
                break

            else:
                time.sleep(30)


        while True:
            CDSID = json.loads(str(CDS_text.encode("utf-8")))["volumeIds"][0]
            CDS_s_conde, CDS_s_text = self.GetCDSinfo(CDSID)
            if CDS_conde == 200 and CDS_s_text == "Available":
                logging.info("**项目2***" + xiangmu + "CDS挂载" + "--" + str(BccName).encode("utf-8"))
                Cds_mount_conde, Cds_mount_text = self.mountCDS(CDSID, BccId)
                self.m_grid1.SetCellValue(1, 6, str(Cds_mount_conde))
                logging.info(str(Cds_mount_conde) + "--" + Cds_mount_text)
                logging.info("---------------------" + "\n")
                break

            else:
                time.sleep(30)


    def ok2(self, event):
        t = Thread(target=self.ok22)
        t.start()

    def ok33(self):

        # 读取配置文件
        config = ConfigParser.ConfigParser()
        config.read("config.cfg")

        if self.m_radioBtn4.GetValue()  == True:
            ak = config.get("sbk_config", "ak")
            sk = config.get("sbk_config", "sk")
            xiangmu = "沙巴克"
        else:
            ak = config.get("y2game_config", "ak")
            sk = config.get("y2game_config", "sk")
            xiangmu = "y2game"

        # 初始化ak,sk类信息
        self.Sign_key(ak, sk)

        DCC = self.m_textCtrl271.GetValue()
        if str(DCC[0]) in '1234567890':
            self.m_textCtrl271.SetValue(u"数字开头！" + DCC)
            assert False

        BccName = self.m_textCtrl29.GetValue()
        if str(BccName[0]) in '1234567890':
            self.m_textCtrl29.SetValue(u"数字开头！" + BccName)
            assert False
        self.m_grid1.SetCellValue(2, 0, BccName)

        EipName = self.m_textCtrl2712.GetValue()
        if str(EipName[0]) in '1234567890':
            self.m_textCtrl2712.SetValue(u"数字开头！"  +EipName)
            assert False
        self.m_grid1.SetCellValue(2, 2, EipName)

        Sec = self.m_comboBox41.GetValue().encode("utf-8")

        if self.m_radioBtn4.GetValue() == True:
            BccimageId = self.m_textCtrl461.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl461.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "s38888a"

            CdsimageId = self.m_textCtrl46.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl46.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec == "安卓_gs":
                SecId = "g-k8wUmJRs"
            elif Sec == "IOS_gs":
                SecId = "g-u5UoWLlG"
            elif Sec == "越狱_gs":
                SecId = "g-birc2UX2"
            elif Sec == "cross":
                SecId = "g-cvUO4Azr"
            else:
                SecId = "g-BGEHzEIX"
        else:
            BccimageId = self.m_textCtrl4611.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl4611.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "@k9999999999a"

            CdsimageId = self.m_textCtrl463.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl463.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec == "安卓_gs":
                SecId = "g-ponf77kU"
            elif Sec == "IOS_gs":
                SecId = "g-XACjQ0m5"
            elif Sec == "越狱_gs":
                SecId = "g-Z969fwDv"
            elif Sec == "cross":
                SecId = "g-KJpH38Rh"
            else:
                SecId = "g-xDFsHlEy"


        logging.info("BCC创建" + "--" + str(BccName).encode("utf-8"))
        BCC_conde, Bcc_text = self.createInstance(DCC, BccName, BccimageId, passwd)
        self.m_grid1.SetCellValue(2, 1, str(BCC_conde))
        logging.info(str(BCC_conde) + "--" + Bcc_text)
        logging.info("---------------------" +"\n")

        if BCC_conde == 200 :
            assert True
        else:
            self.m_grid1.SetCellValue(2, 1, str("DccID Error"))
            assert False

        BccId = json.loads(str(Bcc_text.encode("utf-8")))["instanceIds"][0]

        logging.info("**项目3***" + xiangmu + "EIP创建" + "--" + str(BccName).encode("utf-8"))
        EIP_conde, EIP_text = self.createEIP(EipName)
        logging.info(str(EIP_conde) + "--" +EIP_text )
        logging.info("---------------------" +"\n")

        EIP = json.loads(str(EIP_text.encode("utf-8")))["eip"]
        self.m_grid1.SetCellValue(2, 3, str(EIP))

        Cds = self.m_comboBox4.GetValue().encode("utf-8")

        if 'yes        ' == Cds:
            logging.info("**项目3***" + xiangmu + "CDS创建" + "--" + str(BccName).encode("utf-8"))
            CDS_conde, CDS_text = self.createDCS(CdsimageId)
            self.m_grid1.SetCellValue(2, 5, str(CDS_conde))
            logging.info(str(CDS_conde) + "--" + CDS_text)
            logging.info("---------------------" + "\n")



        while True:
            Bcc_status_code, BCC_status_text = self.getInstanceDetail(BccId)
            if BCC_status_text == "Running":
                logging.info("**项目3***" + xiangmu + "BCC加入安全组" + "--" + str(BccName).encode("utf-8"))
                Sec_add_conde, Sec_add_text = self.addInstanceSec(SecId, BccId)
                self.m_grid1.SetCellValue(2, 7, str(Sec_add_conde))
                logging.info(str(Sec_add_conde) + "--" + Sec_add_text)
                logging.info("---------------------" +"\n")


                logging.info("**项目3***" + xiangmu + "EIP挂载" + "--" + str(BccName).encode("utf-8"))
                Eip_mount_conde, Eip_mount_text = self.mountEIP(BccId, EIP)
                self.m_grid1.SetCellValue(2, 4, str(Eip_mount_conde))
                logging.info(str(Eip_mount_conde) + "--" + Eip_mount_text)
                logging.info("---------------------" +"\n")
                break

            else:
                time.sleep(30)

        while True:
            CDSID = json.loads(str(CDS_text.encode("utf-8")))["volumeIds"][0]
            CDS_s_conde, CDS_s_text = self.GetCDSinfo(CDSID)
            if CDS_conde == 200 and CDS_s_text == "Available":
                logging.info("**项目3***" + xiangmu + "CDS挂载" + "--" + str(BccName).encode("utf-8"))
                Cds_mount_conde, Cds_mount_text = self.mountCDS(CDSID, BccId)
                self.m_grid1.SetCellValue(2, 6, str(Cds_mount_conde))
                logging.info(str(Cds_mount_conde) + "--" + Cds_mount_text)
                logging.info("---------------------" + "\n")
                break

            else:
                time.sleep(30)

    def ok3(self, event):
        t = Thread(target=self.ok33)
        t.start()

    def ok44(self):

        # 读取配置文件
        config = ConfigParser.ConfigParser()
        config.read("config.cfg")

        if self.m_radioBtn4.GetValue()  == True:
            ak = config.get("sbk_config", "ak")
            sk = config.get("sbk_config", "sk")
            xiangmu = "沙巴克"
        else:
            ak = config.get("y2game_config", "ak")
            sk = config.get("y2game_config", "sk")
            xiangmu = "y2game"

        # 初始化ak,sk类信息
        self.Sign_key(ak, sk)

        logging.info("************项目4**************" + xiangmu)
        DCC = self.m_textCtrl26.GetValue()
        if str(DCC[0]) in '1234567890':
            self.m_textCtrl26.SetValue(u"数字开头！" + DCC)
            assert False

        BccName = self.m_textCtrl30.GetValue()
        if str(BccName[0]) in '1234567890':
            self.m_textCtrl30.SetValue(u"数字开头！" + BccName)
            assert False
        self.m_grid1.SetCellValue(3, 0, BccName)

        EipName = self.m_textCtrl34.GetValue()
        if str(EipName[0]) in '1234567890':
            self.m_textCtrl34.SetValue(u"数字开头！"  +EipName)
            assert False
        self.m_grid1.SetCellValue(3, 2, EipName)

        Sec = self.m_comboBox51.GetValue().encode("utf-8")

        if self.m_radioBtn4.GetValue() == True:
            BccimageId = self.m_textCtrl461.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl461.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "s3@99999999999a"

            CdsimageId = self.m_textCtrl46.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl46.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec == "安卓_gs":
                SecId = "g-k8wUmJRs"
            elif Sec == "IOS_gs":
                SecId = "g-u5UoWLlG"
            elif Sec == "越狱_gs":
                SecId = "g-birc2UX2"
            elif Sec == "cross":
                SecId = "g-cvUO4Azr"
            else:
                SecId = "g-BGEHzEIX"
        else:
            BccimageId = self.m_textCtrl4611.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl4611.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "@999999999a"

            CdsimageId = self.m_textCtrl463.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl463.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec == "安卓_gs":
                SecId = "g-ponf77kU"
            elif Sec == "IOS_gs":
                SecId = "g-XACjQ0m5"
            elif Sec == "越狱_gs":
                SecId = "g-Z969fwDv"
            elif Sec == "cross":
                SecId = "g-KJpH38Rh"
            else:
                SecId = "g-xDFsHlEy"


        logging.info("**项目4***" + xiangmu + "BCC创建" + "--" + str(BccName).encode("utf-8"))
        BCC_conde, Bcc_text = self.createInstance(DCC, BccName, BccimageId, passwd)
        self.m_grid1.SetCellValue(3, 1, str(BCC_conde))
        logging.info(str(BCC_conde) + "--" + Bcc_text)
        logging.info("---------------------" +"\n")

        if BCC_conde == 200 :
            assert True
        else:
            self.m_grid1.SetCellValue(3, 1, str("DccID Error"))
            assert False

        BccId = json.loads(str(Bcc_text.encode("utf-8")))["instanceIds"][0]

        logging.info("**项目4***" + xiangmu + "EIP创建" + "--" + str(BccName).encode("utf-8"))
        EIP_conde, EIP_text = self.createEIP(EipName)
        logging.info(str(EIP_conde) + "--" +EIP_text )
        logging.info("---------------------" +"\n")

        EIP = json.loads(str(EIP_text.encode("utf-8")))["eip"]
        self.m_grid1.SetCellValue(3, 3, str(EIP))

        Cds = self.m_comboBox5.GetValue().encode("utf-8")

        if 'yes        ' == Cds:
            logging.info("**项目4***" + xiangmu + "CDS创建" + "--" + str(BccName).encode("utf-8"))
            CDS_conde, CDS_text = self.createDCS(CdsimageId)
            self.m_grid1.SetCellValue(3, 5, str(CDS_conde))
            logging.info(str(CDS_conde) + "--" + CDS_text)
            logging.info("---------------------" + "\n")



        while True:
            Bcc_status_code, BCC_status_text = self.getInstanceDetail(BccId)
            if BCC_status_text == "Running":
                logging.info("**项目4***" + xiangmu + "BCC加入安全组" + "--" + str(BccName).encode("utf-8"))
                Sec_add_conde, Sec_add_text = self.addInstanceSec(SecId, BccId)
                self.m_grid1.SetCellValue(3, 7, str(Sec_add_conde))
                logging.info(str(Sec_add_conde) + "--" + Sec_add_text)
                logging.info("---------------------" +"\n")


                logging.info("**项目4***" + xiangmu + "EIP挂载" + "--" + str(BccName).encode("utf-8"))
                Eip_mount_conde, Eip_mount_text = self.mountEIP(BccId, EIP)
                self.m_grid1.SetCellValue(3, 4, str(Eip_mount_conde))
                logging.info(str(Eip_mount_conde) + "--" + Eip_mount_text)
                logging.info("---------------------" +"\n")
                break

            else:
                time.sleep(30)

        while True:
            CDSID = json.loads(str(CDS_text.encode("utf-8")))["volumeIds"][0]
            CDS_s_conde, CDS_s_text = self.GetCDSinfo(CDSID)
            if CDS_conde == 200 and CDS_s_text == "Available":
                logging.info("**项目4***" + xiangmu + "CDS挂载" + "--" + str(BccName).encode("utf-8"))
                Cds_mount_conde, Cds_mount_text = self.mountCDS(CDSID, BccId)
                self.m_grid1.SetCellValue(3, 6, str(Cds_mount_conde))
                logging.info(str(Cds_mount_conde) + "--" + Cds_mount_text)
                logging.info("---------------------" + "\n")
                break

            else:
                time.sleep(30)

    def ok4(self, event):
        t = Thread(target=self.ok44)
        t.start()

    def ok55(self):

        # 读取配置文件
        config = ConfigParser.ConfigParser()
        config.read("config.cfg")

        if self.m_radioBtn4.GetValue()  == True:
            ak = config.get("sbk_config", "ak")
            sk = config.get("sbk_config", "sk")
            xiangmu = "沙巴克"
        else:
            ak = config.get("y2game_config", "ak")
            sk = config.get("y2game_config", "sk")
            xiangmu = "y2game"

        # 初始化ak,sk类信息
        self.Sign_key(ak, sk)

        DCC = self.m_textCtrl27.GetValue()
        if str(DCC[0]) in '1234567890':
            self.m_textCtrl27.SetValue(u"数字开头！" + DCC)
            assert False

        BccName = self.m_textCtrl31.GetValue()
        if str(BccName[0]) in '1234567890':
            self.m_textCtrl31.SetValue(u"数字开头！" + BccName)
            assert False
        self.m_grid1.SetCellValue(4, 0, BccName)

        EipName = self.m_textCtrl35.GetValue()
        if str(EipName[0]) in '1234567890':
            self.m_textCtrl35.SetValue(u"数字开头！"  +EipName)
            assert False
        self.m_grid1.SetCellValue(4, 2, EipName)

        Sec = self.m_comboBox61.GetValue().encode("utf-8")

        if self.m_radioBtn4.GetValue() == True:
            BccimageId = self.m_textCtrl461.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl461.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "s322211111Vga"

            CdsimageId = self.m_textCtrl46.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl46.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec == "安卓_gs":
                SecId = "g-k8wUmJRs"
            elif Sec == "IOS_gs":
                SecId = "g-u5UoWLlG"
            elif Sec == "越狱_gs":
                SecId = "g-birc2UX2"
            elif Sec == "cross":
                SecId = "g-cvUO4Azr"
            else:
                SecId = "g-BGEHzEIX"
        else:
            BccimageId = self.m_textCtrl4611.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl4611.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "@kds11111155a"

            CdsimageId = self.m_textCtrl463.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl463.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec == "安卓_gs":
                SecId = "g-ponf77kU"
            elif Sec == "IOS_gs":
                SecId = "g-XACjQ0m5"
            elif Sec == "越狱_gs":
                SecId = "g-Z969fwDv"
            elif Sec == "cross":
                SecId = "g-KJpH38Rh"
            else:
                SecId = "g-xDFsHlEy"


        logging.info("**项目5***" + xiangmu + "BCC创建" + "--" + str(BccName).encode("utf-8"))
        BCC_conde, Bcc_text = self.createInstance(DCC, BccName, BccimageId, passwd)
        self.m_grid1.SetCellValue(4, 1, str(BCC_conde))
        logging.info(str(BCC_conde) + "--" + Bcc_text)
        logging.info("---------------------" +"\n")

        if BCC_conde == 200 :
            assert True
        else:
            self.m_grid1.SetCellValue(4, 1, str("DccID Error"))
            assert False

        BccId = json.loads(str(Bcc_text.encode("utf-8")))["instanceIds"][0]

        logging.info("**项目5***" + xiangmu + "EIP创建" + "--" + str(BccName).encode("utf-8"))
        EIP_conde, EIP_text = self.createEIP(EipName)
        logging.info(str(EIP_conde) + "--" +EIP_text )
        logging.info("---------------------" +"\n")

        EIP = json.loads(str(EIP_text.encode("utf-8")))["eip"]
        self.m_grid1.SetCellValue(4, 3, str(EIP))

        Cds = self.m_comboBox6.GetValue().encode("utf-8")

        if 'yes        ' == Cds:
            logging.info("**项目5***" + xiangmu + "CDS创建" + "--" + str(BccName).encode("utf-8"))
            CDS_conde, CDS_text = self.createDCS(CdsimageId)
            self.m_grid1.SetCellValue(4, 5, str(CDS_conde))
            logging.info(str(CDS_conde) + "--" + CDS_text)
            logging.info("---------------------" + "\n")



        while True:
            Bcc_status_code, BCC_status_text = self.getInstanceDetail(BccId)
            if BCC_status_text == "Running":
                logging.info("**项目5***" + xiangmu + "BCC加入安全组" + "--" + str(BccName).encode("utf-8"))
                Sec_add_conde, Sec_add_text = self.addInstanceSec(SecId, BccId)
                self.m_grid1.SetCellValue(4, 7, str(Sec_add_conde))
                logging.info(str(Sec_add_conde) + "--" + Sec_add_text)
                logging.info("---------------------" +"\n")


                logging.info("**项目5***" + xiangmu + "EIP挂载" + "--" + str(BccName).encode("utf-8"))
                Eip_mount_conde, Eip_mount_text = self.mountEIP(BccId, EIP)
                self.m_grid1.SetCellValue(4, 4, str(Eip_mount_conde))
                logging.info(str(Eip_mount_conde) + "--" + Eip_mount_text)
                logging.info("---------------------" +"\n")
                break

            else:
                time.sleep(30)

        while True:
            CDSID = json.loads(str(CDS_text.encode("utf-8")))["volumeIds"][0]
            CDS_s_conde, CDS_s_text = self.GetCDSinfo(CDSID)
            if CDS_conde == 200 and CDS_s_text == "Available":
                logging.info("**项目5***" + xiangmu + "CDS挂载" + "--" + str(BccName).encode("utf-8"))
                Cds_mount_conde, Cds_mount_text = self.mountCDS(CDSID, BccId)
                self.m_grid1.SetCellValue(4, 6, str(Cds_mount_conde))
                logging.info(str(Cds_mount_conde) + "--" + Cds_mount_text)
                logging.info("---------------------" + "\n")
                break

            else:
                time.sleep(30)

    def ok5(self, event):
        t = Thread(target=self.ok55)
        t.start()

    def ok66(self):

        # 读取配置文件
        config = ConfigParser.ConfigParser()
        config.read("config.cfg")

        if self.m_radioBtn4.GetValue()  == True:
            ak = config.get("sbk_config", "ak")
            sk = config.get("sbk_config", "sk")
            xiangmu = "沙巴克"
        else:
            ak = config.get("y2game_config", "ak")
            sk = config.get("y2game_config", "sk")
            xiangmu = "y2game"

        # 初始化ak,sk类信息
        self.Sign_key(ak, sk)

        DCC = self.m_textCtrl28.GetValue()
        if str(DCC[0]) in '1234567890':
            self.m_textCtrl28.SetValue(u"数字开头！" + DCC)
            assert False

        BccName = self.m_textCtrl32.GetValue()
        if str(BccName[0]) in '1234567890':
            self.m_textCtrl32.SetValue(u"数字开头！" + BccName)
            assert False
        self.m_grid1.SetCellValue(5, 0, BccName)

        EipName = self.m_textCtrl36.GetValue()
        if str(EipName[0]) in '1234567890':
            self.m_textCtrl36.SetValue(u"数字开头！"  +EipName)
            assert False
        self.m_grid1.SetCellValue(5, 2, EipName)

        Sec = self.m_comboBox71.GetValue().encode("utf-8")

        if self.m_radioBtn4.GetValue() == True:
            BccimageId = self.m_textCtrl461.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl461.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "s388888888888a"

            CdsimageId = self.m_textCtrl46.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl46.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec == "安卓_gs":
                SecId = "g-k8wUmJRs"
            elif Sec == "IOS_gs":
                SecId = "g-u5UoWLlG"
            elif Sec == "越狱_gs":
                SecId = "g-birc2UX2"
            elif Sec == "cross":
                SecId = "g-cvUO4Azr"
            else:
                SecId = "g-BGEHzEIX"

        else:
            BccimageId = self.m_textCtrl4611.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl4611.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "@k999999999a"

            CdsimageId = self.m_textCtrl463.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl463.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec == "安卓_gs":
                SecId = "g-ponf77kU"
            elif Sec == "IOS_gs":
                SecId = "g-XACjQ0m5"
            elif Sec == "越狱_gs":
                SecId = "g-Z969fwDv"
            elif Sec == "cross":
                SecId = "g-KJpH38Rh"
            else:
                SecId = "g-xDFsHlEy"


        logging.info("**项目6***" + xiangmu + "BCC创建" + "--" + str(BccName).encode("utf-8"))
        BCC_conde, Bcc_text = self.createInstance(DCC, BccName, BccimageId, passwd)
        self.m_grid1.SetCellValue(5, 1, str(BCC_conde))
        logging.info(str(BCC_conde) + "--" + Bcc_text)
        logging.info("---------------------" +"\n")

        if BCC_conde == 200 :
            assert True
        else:
            self.m_grid1.SetCellValue(5, 1, str("DccID Error"))
            assert False

        BccId = json.loads(str(Bcc_text.encode("utf-8")))["instanceIds"][0]

        logging.info("**项目6***" + xiangmu + "EIP创建" + "--" + str(BccName).encode("utf-8"))
        EIP_conde, EIP_text = self.createEIP(EipName)
        logging.info(str(EIP_conde) + "--" +EIP_text )
        logging.info("---------------------" +"\n")

        EIP = json.loads(str(EIP_text.encode("utf-8")))["eip"]
        self.m_grid1.SetCellValue(5, 3, str(EIP))

        Cds = self.m_comboBox7.GetValue().encode("utf-8")

        if 'yes        ' == Cds:
            logging.info("**项目6***" + xiangmu + "CDS创建" + "--" + str(BccName).encode("utf-8"))
            CDS_conde, CDS_text = self.createDCS(CdsimageId)
            self.m_grid1.SetCellValue(5, 5, str(CDS_conde))
            logging.info(str(CDS_conde) + "--" + CDS_text)
            logging.info("---------------------" + "\n")



        while True:
            Bcc_status_code, BCC_status_text = self.getInstanceDetail(BccId)
            if BCC_status_text == "Running":
                logging.info("**项目6***" + xiangmu + "BCC加入安全组" + "--" + str(BccName).encode("utf-8"))
                Sec_add_conde, Sec_add_text = self.addInstanceSec(SecId, BccId)
                self.m_grid1.SetCellValue(5, 7, str(Sec_add_conde))
                logging.info(str(Sec_add_conde) + "--" + Sec_add_text)
                logging.info("---------------------" +"\n")


                logging.info("**项目6***" + xiangmu + "EIP挂载" + "--" + str(BccName).encode("utf-8"))
                Eip_mount_conde, Eip_mount_text = self.mountEIP(BccId, EIP)
                self.m_grid1.SetCellValue(5, 4, str(Eip_mount_conde))
                logging.info(str(Eip_mount_conde) + "--" + Eip_mount_text)
                logging.info("---------------------" +"\n")
                break

            else:
                time.sleep(30)

        while True:
            CDSID = json.loads(str(CDS_text.encode("utf-8")))["volumeIds"][0]
            CDS_s_conde, CDS_s_text = self.GetCDSinfo(CDSID)
            if CDS_conde == 200 and CDS_s_text == "Available":
                logging.info("**项目6***" + xiangmu + "CDS挂载" + "--" + str(BccName).encode("utf-8"))
                Cds_mount_conde, Cds_mount_text = self.mountCDS(CDSID, BccId)
                self.m_grid1.SetCellValue(5, 6, str(Cds_mount_conde))
                logging.info(str(Cds_mount_conde) + "--" + Cds_mount_text)
                logging.info("---------------------" + "\n")
                break

            else:
                time.sleep(30)

    def ok6(self, event):
        t = Thread(target=self.ok66)
        t.start()

    def OK77(self):

        # 读取配置文件
        config = ConfigParser.ConfigParser()
        config.read("config.cfg")

        if self.m_radioBtn4.GetValue()  == True:
            ak = config.get("sbk_config", "ak")
            sk = config.get("sbk_config", "sk")
            xiangmu = "沙巴克"
        else:
            ak = config.get("y2game_config", "ak")
            sk = config.get("y2game_config", "sk")
            xiangmu = "y2game"

        # 初始化ak,sk类信息
        self.Sign_key(ak, sk)

        DCC = self.m_textCtrl23.GetValue()
        if str(DCC[0]) in '1234567890':
            self.m_textCtrl23.SetValue(u"数字开头！" + DCC)
            assert False

        BccName = self.m_textCtrl24.GetValue()
        if str(BccName[0]) in '1234567890':
            self.m_textCtrl24.SetValue(u"数字开头！" + BccName)
            assert False
        self.m_grid1.SetCellValue(6, 0, BccName)

        EipName = self.m_textCtrl25.GetValue()
        if str(EipName[0]) in '1234567890':
            self.m_textCtrl25.SetValue(u"数字开头！"  +EipName)
            assert False
        self.m_grid1.SetCellValue(6, 2, EipName)

        Sec = self.m_comboBox20.GetValue().encode("utf-8")

        if self.m_radioBtn4.GetValue() == True:
            BccimageId = self.m_textCtrl461.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl461.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "s355555511111111g8Vga"

            CdsimageId = self.m_textCtrl46.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl46.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec == "安卓_gs":
                SecId = "g-k8wUmJRs"
            elif Sec == "IOS_gs":
                SecId = "g-u5UoWLlG"
            elif Sec == "越狱_gs":
                SecId = "g-birc2UX2"
            elif Sec == "cross":
                SecId = "g-cvUO4Azr"
            else:
                SecId = "g-BGEHzEIX"
        else:
            BccimageId = self.m_textCtrl4611.GetValue()
            if str(BccimageId[0]) in '1234567890':
                self.m_textCtrl4611.SetValue(u"数字开头！" + BccimageId)
                assert False

            passwd = "@kds1111K35a"

            CdsimageId = self.m_textCtrl463.GetValue()
            if str(CdsimageId[0]) in '1234567890':
                self.m_textCtrl463.SetValue(u"数字开头！" + CdsimageId)
                assert False

            if Sec == "安卓_gs":
                SecId = "g-ponf77kU"
            elif Sec == "IOS_gs":
                SecId = "g-XACjQ0m5"
            elif Sec == "越狱_gs":
                SecId = "g-Z969fwDv"
            elif Sec == "cross":
                SecId = "g-KJpH38Rh"
            else:
                SecId = "g-xDFsHlEy"


        logging.info("**项目7***" + xiangmu + "BCC创建" + "--" + str(BccName).encode("utf-8"))
        BCC_conde, Bcc_text = self.createInstance(DCC, BccName, BccimageId, passwd)
        self.m_grid1.SetCellValue(6, 1, str(BCC_conde))
        logging.info(str(BCC_conde) + "--" + Bcc_text)
        logging.info("---------------------" +"\n")

        if BCC_conde == 200 :
            assert True
        else:
            self.m_grid1.SetCellValue(6, 1, str("DccID Error"))
            assert False

        BccId = json.loads(str(Bcc_text.encode("utf-8")))["instanceIds"][0]

        logging.info("**项目7***" + xiangmu + "EIP创建" + "--" + str(BccName).encode("utf-8"))
        EIP_conde, EIP_text = self.createEIP(EipName)
        logging.info(str(EIP_conde) + "--" +EIP_text )
        logging.info("---------------------" +"\n")

        EIP = json.loads(str(EIP_text.encode("utf-8")))["eip"]
        self.m_grid1.SetCellValue(6, 3, str(EIP))

        Cds = self.m_comboBox19.GetValue().encode("utf-8")

        if 'yes        ' == Cds:
            logging.info("**项目7***" + xiangmu + "CDS创建" + "--" + str(BccName).encode("utf-8"))
            CDS_conde, CDS_text = self.createDCS(CdsimageId)
            self.m_grid1.SetCellValue(6, 5, str(CDS_conde))
            logging.info(str(CDS_conde) + "--" + CDS_text)
            logging.info("---------------------" + "\n")



        while True:
            Bcc_status_code, BCC_status_text = self.getInstanceDetail(BccId)
            if BCC_status_text == "Running":
                logging.info("**项目7***" + xiangmu + "BCC加入安全组" + "--" + str(BccName).encode("utf-8"))
                Sec_add_conde, Sec_add_text = self.addInstanceSec(SecId, BccId)
                self.m_grid1.SetCellValue(6, 7, str(Sec_add_conde))
                logging.info(str(Sec_add_conde) + "--" + Sec_add_text)
                logging.info("---------------------" +"\n")


                logging.info("**项目7***" + xiangmu + "EIP挂载" + "--" + str(BccName).encode("utf-8"))
                Eip_mount_conde, Eip_mount_text = self.mountEIP(BccId, EIP)
                self.m_grid1.SetCellValue(6, 4, str(Eip_mount_conde))
                logging.info(str(Eip_mount_conde) + "--" + Eip_mount_text)
                logging.info("---------------------" +"\n")
                break

            else:
                time.sleep(30)

        while True:
            CDSID = json.loads(str(CDS_text.encode("utf-8")))["volumeIds"][0]
            CDS_s_conde, CDS_s_text = self.GetCDSinfo(CDSID)
            if CDS_conde == 200 and CDS_s_text == "Available":
                logging.info("**项目7***" + xiangmu + "CDS挂载" + "--" + str(BccName).encode("utf-8"))
                Cds_mount_conde, Cds_mount_text = self.mountCDS(CDSID, BccId)
                self.m_grid1.SetCellValue(6, 6, str(Cds_mount_conde))
                logging.info(str(Cds_mount_conde) + "--" + Cds_mount_text)
                logging.info("---------------------" + "\n")
                break

            else:
                time.sleep(30)

    def OK7(self, event):
        t = Thread(target=self.OK77)
        t.start()


if __name__ == '__main__':
    # app = wx.PySimpleApp()
	app = wx.App()
        MyFrame1(None).Show()
        app.MainLoop()