#! python3
# -*- coding: UTF-8 -*-
import os
import os.path
import datetime
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pathlib import PureWindowsPath as pwt
from pathlib import PurePosixPath as Pxp

# 读取文件信息清单


class FileLst(object):

    @staticmethod
    def getlist(pt):
        FilList = []
        for parent, DirNm, FileNm in os.walk(pt):
            for filename in FileNm:
                suf = Pxp(filename).suffix
                if suf == '.xls':  # or suf == '.xlsx':
                    # FilList.append(DirNm )
                    FilList.append(os.path.join(parent, filename))
        return FilList


def getlist(src_dir):
    fl = FileLst()
    if len(src_dir) == 0:
        base_dir = get_cur_dir()
    else:
        base_dir = src_dir
    list_file = fl.getlist(base_dir)
    return list_file


def askdir(in_dir,in_txt):
    if len(in_dir.get()) > 0:
        base_dir = in_dir.get()
    else:
        base_dir = os.getcwd()
    options = {}
    options['initialdir'] = base_dir
    options['title'] = in_txt
    options['mustexist'] = False
    dir_value = ""
    cnt_try = 0
    while len(dir_value) == 0:
        cnt_try += 1
        if cnt_try > 1:
            break
        dir_value = askdirectory(**options)
        if len(dir_value) == 0:
            messagebox.showinfo('提示', in_txt)
        else:
            break
    return dir_value

def get_cur_dir():
    return os.getcwd()


def get_par_dir():
    return pwt(os.getcwd()).parents[0]


def get_tgt_dir():
    return pwt(os.getcwd()).parents[0].joinpath('EXPORT')


def get_nam_from_fullpath(path):
    return pwt(path).name


def main():
    # print('当前目录' + get_cur_dir())
    curstr = str(get_cur_dir())
    print(curstr)
    print(str(get_par_dir()))
    print(str(get_tgt_dir()))
    # print(getlist(r'D:/Users/huazy.ZZYT/PycharmProjects/ExcelRead/ABI008'))
    for index, fil in enumerate(getlist(r'D:/Users/huazy.ZZYT/PycharmProjects/ExcelRead/ABI008')):  # fil in getlist():

        print(get_nam_from_fullpath(fil))

    print(str(pwt(fil).parents[0]))

# 主要处理
if __name__ == '__main__':
    main()