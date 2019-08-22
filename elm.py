# -*- coding: utf8 -*-

# 0123456789012345678901234567890123456789012345678901234567890123456789012345678
# 上边一行用来对比一行代码是否超过80个字符，超过换行
import tkinter as tk

import random

import codecs

root = tk.Tk(className = '范例循环模型')
root.geometry('800x400')

count = 0  # 因为点击两次show按钮才完成一个完整的英译汉或者汉译英过程，这里通过count为0或1来判断
e_or_c = 0     # e_or_c标志是英译汉还是汉译英，英译汉为0，汉译英为1
keys = list()  # 存储所有的英语句子
key_num = 0  # 英语句子在key中的下标
example = {}  # 通过字典这种键值对的方式存储英汉对照句子

## 每次打开程序时在文件中读出数据，通过字符串处理，存储到字典example中
f = codecs.open("elm.txt", encoding="utf8")  
data = f.read()
f.close()
data = data.rstrip('\n')  # 为下面的切分做准备
datas = data.split('\n')
for elm in datas:
    elm_element = elm.split('%')
    example[elm_element[0]] = elm_element[1]
    
## 点击第一次show按钮，判断是英译汉还是汉译英，在字典elmDict中随机取一对值，先显示英语或汉语；第二次点击
## 时显示答案。
def show_call_back():
    """点击show按钮时执行的函数，每点击一次显示一条英语或汉语 """
    global count, keys, key_num, e_or_c
    if count == 0:
        keys = list(example.keys())
        key_num = random.randint(0, len(keys)-1)
        count += 1
        if e_or_c == 0:
            var_chinese.set('')
        else:
            var_english.set('')
    else:
        count -= 1
    if e_or_c == 0:
        var_english.set(keys[key_num])
        e_or_c += 1
    elif e_or_c == 1:
        var_chinese.set(example[keys[key_num]])
        e_or_c -= 1

## 通过改变EC的值，在英译汉与汉译英之间切换
def change_call_back():
    """点击change按钮调用的函数，在英译汉与汉译英模式直接切换"""
    global e_or_c
    var_english.set("English")
    var_chinese.set("Chinese")
    if e_or_c == 0:
        e_or_c = 1
    else:
        e_or_c = 0
        
## 把文本框中的数据存入文件中
def insert_call_back():
    """点击insert按钮调用的函数，将输入的范例插入文件"""
    global elmdict
    entry_english_str = entry_english.get()
    entry_chinese_stry = entry_chinese.get()
    example[entry_english_str] = entry_chinese_stry
    f = codecs.open("elm.txt", "a", encoding = "utf8")
    f.write(entry_english_str + '%' + entry_chinese_stry + '\n')
    f.close()
    entry_english.delete(0, 'end')
    entry_chinese.delete(0, 'end')
    
## 英文和中文显示的内容变量，调用他们的set方法就可以改变显示的内容
var_english = tk.StringVar()
var_chinese = tk.StringVar()

## 定义并放置用于显示英语汉语的标签
english_label = tk.Label(textvar = var_english, font = ("黑体",24))
english_label.pack()
chinese_label = tk.Label(textvar = var_chinese, font = ("宋体",14))
chinese_label.pack()

## 定义并放置show和change按钮
show_button = tk.Button(root, text = 'show', command = show_call_back,
                   background = '#00ff00')
change_button = tk.Button(root, text = 'change', command = change_call_back,
                     background = '#0000ff')
show_button.pack()
change_button.pack()

## 定义并放置输入英语和汉语的文本框
entry_english = tk.Entry(root, width = 80, font = ("黑体",24))
entry_english.pack()
entry_chinese = tk.Entry(root, width = 50, font = ("宋体",14))
entry_chinese.pack()

insert_button = tk.Button(root, text = 'insert', command = insert_call_back,
                     bg = "#ff0000")      # 定义并放置insert按钮
insert_button.pack()

root.mainloop()  # 启动主程序


## problem:
## 1.可能插入空白到文件中
## 2.前后点击的题目重复，体验不好
## 3.change按钮最好在点完两次show按钮后再点，否则体验不好
######################################################################
## idea:
## 1.每个合作人有自己的文件，在界面上可以通过一个下拉菜单选择或单选框