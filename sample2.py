import tkinter as tk
from tkinter import filedialog,messagebox
import os
import shutil
import can
import time
from win32com.client import Dispatch
from tqdm import tqdm #進捗が見える化

#Cancelボタンの処理
def Cancel():
    if messagebox.askokcancel("Confirmation", "Do you really want to cancel?"):
        #現在変換中の処理だけ中止したい(要修正)
        root.destroy()

#Folder選択
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        txtFolderPath.delete(0, tk.END)  # テキストボックスをクリア
        txtFolderPath.insert(0, folder_path)  # テキストボックスにフォルダパスを挿入
        #print(folder_path)
        return folder_path

def OK():
    #ここはエラー処理を書いて、メイン処理は別に置きたい

    #cfgFilePathとFoldePathをテキストボックスから取得
    #cfgFilePath = str(txtCfgPath.get())
    folderPath = str(txtFolderPath.get())
    #print(cfgFilePath)
    #print(folderPath)
    #fileConvert(cfgFilePath,folderPath)

#整数しか入力できないようにする
def validate_input(new_value):
    if new_value == "":
        return True  # Allow empty input
    return new_value.isdigit()

root = tk.Tk()

# %%
# 間引きのテキストボックス
vcmd = (root.register(validate_input), '%P')
# 初期値を設定
entry_var = tk.IntVar(value=0)
txtThinOut = tk.Entry(root, validate='key', validatecommand=vcmd,textvariable=entry_var,width=6, justify='right',font=("Meiryo UI", 12))
txtThinOut.place(x=255,y=5,height=25)
#FolderPath
#テキストボックスの幅を設定
txtFolderPath = tk.Entry(root,width=40,justify='right',font=("Meiryo UI",8))
#位置と高さ
txtFolderPath.place(x=5,y=70,height=25)

# %%
#FolderPath選択ボタン
btnFolderSelect = tk.Button(root, text="...", command=select_folder,height=1,width=3)
#位置
btnFolderSelect.place(x=290,y=70)

# %%
#ラベルを作成して配置
label_font = ("Meiryo UI", 12, "bold")
label_1 = tk.Label(root, text="間引きカウント(しない場合は[0])",font=label_font)
label_2 = tk.Label(root, text="Folder Path",font=label_font)
#ラベル位置
label_1.place(x=3,y=5)
label_2.place(x=3,y=40)

# %%
#Cancelボタン
#btnCancel = tk.Button(root, text="Cancel", command=Cancel,font=label_font,bg="red")
#位置
#btnCancel.place(x=410,y=80)

# %%
#OKボタン
btnOK = tk.Button(root, text="GO", command=OK,height=1,width=6,font=label_font,bg="blue")
btnOK.place(x=245,y=105)

# %%
#ウィンドウのタイトルを指定する
root.title("Ext→Concat→ThinOut")
#ウィンドウサイズを指定する。横×縦
root.geometry("328x150")

# %%
#メインループの開始
root.mainloop()