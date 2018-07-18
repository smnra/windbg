#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: CALL_MessgeBoxW.py 
@time: 2018/07/{DAY} 
描述:  调用 win32  api函数    Messagebox 弹出对话框

"""






import ctypes
user = ctypes.windll.LoadLibrary("user32.dll")
user.MessageBoxW(None, '调用C函数例子', '提示信息',0)
