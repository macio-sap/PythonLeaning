#! python3
# -*- coding: UTF-8 -*-
import DirInfo as di
import tkinter as tk
import datetime
from tkinter import constants
from tkinter import StringVar
from tkinter import PhotoImage
from tkinter import IntVar
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askdirectory


# 定义全局变量
root = tk.Tk()
start_tm = datetime.datetime.now()
end_tm = datetime.datetime.now()
mainframe = ttk.Frame(root, padding="3 3 12 12")
srcdir = StringVar()
tgtdir = StringVar()
curstat = StringVar()
pbv = IntVar()


# class Application(tk.Frame):

#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#         self.quit = tk.Button(self, text="QUIT", fg="red", bg="blue",
#                               command=root.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")

def getsrcdir():
    srcdir.set(di.askdir(srcdir, '请选择一个源文件夹'))


def gettgtdir():
    tgtdir.set(di.askdir(tgtdir, '请选择一个目标文件夹'))


def calculate():
    try:
        start_tm = datetime.datetime.now()
        print('开始时间：' + str(start_tm))
        # exec_file_export()
        # for i in range(100):
        #     pb["value"] = i + 1
        #     root.update()
        #     time.sleep(0.1)
        cnt_cur_file = 0
        cnt_all_file = len(di.getlist(srcdir.get()))
        # for index, fil in enumerate(di.getlist(srcdir.get())): 
        #     cnt_cur_file += 1
        #     pbRead1["value"] = (cnt_cur_file / cnt_all_file) * 100
        #     curstat.set('正在处理第' + str(index + 1) + '/' + str(cnt_all_file) + '个文件，文件名：' + get_nam_from_fullpath(fil))
        #     root.update()
        #     wb = open_xls(fil)
        #     print(str(datetime.datetime.now()) + ' ' + fil)
        #     # time.sleep(0.1)
        #     eco_info = get_eco_info(wb)
        #     export_change_bom_lst(wb, tgtdir.get(), eco_info)
        #     export_chg_doc_mat_info(wb, tgtdir.get(), '更改凭证涉及的物料信息', eco_info)
        #     export_chg_doc_mat_info(wb, tgtdir.get(), '删除总成中的自制件和外购件', eco_info)
        #     export_chg_doc_mat_info(wb, tgtdir.get(), '新增总成中的自制件和外购件', eco_info)
        #     print(str(datetime.datetime.now()) + ' ' + fil)
        # print('处理文件数：' + str(cnt_cur_file))
        end_tm = datetime.datetime.now()
        print('结束时间：' + str(end_tm))
        print(str((end_tm - start_tm).seconds))

        curstat.set('数据提取完成，花费时间：' + str((end_tm - start_tm).seconds) + '秒； 总共文件数：' + str(cnt_all_file))
        root.update()
        return cnt_cur_file
    except ValueError:
        pass


def iniScreen():
    root.iconbitmap(
        'D:\\Users\\huazy.ZZYT\\PycharmProjects\\ExcelReader\\Ver001\\img\\icon32.ico')
    root.geometry('1050x380')
    root.title('测试页面程序运行情况')
    mainframe.grid(column=0, row=0, sticky=(
        constants.N, constants.W, constants.E, constants.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    pbRead1 = ttk.Progressbar(
        mainframe, length=800, mode="determinate", orient=constants.HORIZONTAL)
    pbRead1.grid(column=2, row=4, sticky=constants.W)
    pbRead1["maximum"] = 100
    pbRead1["value"] = 0

    pbRead2 = ttk.Progressbar(
        mainframe, length=800, mode="determinate", orient=constants.HORIZONTAL)
    pbRead2.grid(column=2, row=5, sticky=constants.W)
    pbRead2["maximum"] = 100
    pbRead2["value"] = 0

    pbRead3 = ttk.Progressbar(
        mainframe, length=800, mode="determinate", orient=constants.HORIZONTAL)
    pbRead3.grid(column=2, row=6, sticky=constants.W)
    pbRead3["maximum"] = 100
    pbRead3["value"] = 0

    pbRead4 = ttk.Progressbar(
        mainframe, length=800, mode="determinate", orient=constants.HORIZONTAL)
    pbRead4.grid(column=2, row=7, sticky=constants.W)
    pbRead4["maximum"] = 100
    pbRead4["value"] = 0

    pbWrite1 = ttk.Progressbar(
        mainframe, length=800, mode="determinate", orient=constants.HORIZONTAL)
    pbWrite1.grid(column=2, row=8, sticky=constants.W)
    pbWrite1["maximum"] = 100
    pbWrite1["value"] = 0

    pbWrite2 = ttk.Progressbar(
        mainframe, length=800, mode="determinate", orient=constants.HORIZONTAL)
    pbWrite2.grid(column=2, row=9, sticky=constants.W)
    pbWrite2["maximum"] = 100
    pbWrite2["value"] = 0

    pbWrite3 = ttk.Progressbar(
        mainframe, length=800, mode="determinate", orient=constants.HORIZONTAL)
    pbWrite3.grid(column=2, row=10, sticky=constants.W)
    pbWrite3["maximum"] = 100
    pbWrite3["value"] = 0

    pbWrite4 = ttk.Progressbar(
        mainframe, length=800, mode="determinate", orient=constants.HORIZONTAL)
    pbWrite4.grid(column=2, row=11, sticky=constants.W)
    pbWrite4["maximum"] = 100
    pbWrite4["value"] = 0

    ttk.Label(mainframe, text="读取进程1：").grid(
        column=1, row=4, sticky=(constants.W))
    ttk.Label(mainframe, text="读取进程2：").grid(
        column=1, row=5, sticky=(constants.W))
    ttk.Label(mainframe, text="读取进程3：").grid(
        column=1, row=6, sticky=(constants.W))
    ttk.Label(mainframe, text="读取进程4：").grid(
        column=1, row=7, sticky=(constants.W))
    ttk.Label(mainframe, text="写入进程1：").grid(
        column=1, row=8, sticky=(constants.W))
    ttk.Label(mainframe, text="写入进程2：").grid(
        column=1, row=9, sticky=(constants.W))
    ttk.Label(mainframe, text="写入进程3：").grid(
        column=1, row=10, sticky=(constants.W))
    ttk.Label(mainframe, text="写入进程4：").grid(
        column=1, row=11, sticky=(constants.W))

    ttk.Label(mainframe, text="源数据文件目录：").grid(
        column=1, row=1, sticky=(constants.W, constants.E))
    srcdir_entry = ttk.Entry(mainframe, width=60, textvariable=srcdir)
    srcdir_entry.grid(column=2, row=1, sticky=(
        constants.W, constants.E))
    img_folder = PhotoImage(file='../img/data_source_folder.gif')
    ttk.Button(mainframe, text="搜", command=getsrcdir, image = img_folder).grid(
        column=3, row=1, sticky=constants.W)
    srcdir.set(di.get_par_dir())
    tgtdir.set(di.get_tgt_dir())
    ttk.Label(mainframe, text="目标文件目录：").grid(
        column=1, row=2, sticky=(constants.W, constants.E))
    tgtdir_entry = ttk.Entry(mainframe, width=60, textvariable=tgtdir)
    tgtdir_entry.grid(column=2, row=2, sticky=(
        constants.W, constants.E))
    ttk.Button(mainframe, text="搜", command=gettgtdir, image = img_folder).grid(
        column=3, row=2, sticky=constants.W)
    ttk.Button(mainframe, text="提取", command=calculate).grid(
        column=3, row=3, sticky=constants.W)
    ttk.Button(mainframe, text="退出", command=root.quit).grid(
        column=3, row=4, sticky=constants.W)
    ttk.Label(mainframe, textvariable=curstat).grid(
        column=2, row=12, sticky=(constants.W, constants.E))
    curstat.set('请选择正确的源文件夹和目标文件夹，然后选择【提取】按钮...')
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    srcdir_entry.focus()
    root.bind('<Return>', calculate)
    root.mainloop()


# 主要处理
if __name__ == '__main__':
    iniScreen()
