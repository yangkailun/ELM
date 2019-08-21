import tkinter as tk
import random
import codecs

root = tk.Tk(className='范例循环模型')
root.geometry('800x400')

count = 0  #因为点击两次show按钮才完成一个完整的英译汉或者汉译英过程，这里通过count为0或1来判断
EC = 0     #EC标志是英译汉还是汉译英，英译汉为0，汉译英为1
keyList = list()  #存储所有的英语句子
keyNum = 0  #英语句子在keyList中的下标

elmDict = {}  #通过字典这种键值对的方式存储英汉对照句子

##每次打开程序时在文件中读出数据，通过字符串处理，存储到字典elmDict中
f=codecs.open("elm.txt",encoding="utf8")  
data=f.read()
f.close()
data=data.rstrip('\n')  #为下面的切分做准备
dataList=data.split('\n')
for elm in dataList:
    elmEle=elm.split('%')
    elmDict[elmEle[0]]=elmEle[1]

##点击第一次show按钮，判断是英译汉还是汉译英，在字典elmDict中随机取一对值，先显示英语或汉语；第二次点击
##时显示答案。
def showCallBack():
    """点击show按钮时执行的函数 """
    global count,keyList,keyNum,EC
    if count==0:
        keyList = list(elmDict.keys())
        keyNum = random.randint(0,len(keyList)-1)
        count +=1
        if EC == 0:
            varChinese.set('')
        else :
            varEnglish.set('')
    else:
        count -=1
    if EC==0:
        varEnglish.set(keyList[keyNum])
        EC +=1
    elif EC==1:
        varChinese.set(elmDict[keyList[keyNum]])
        EC -=1

##通过改变EC的值，在英译汉与汉译英之间切换
def changeCallBack():
    """点击change按钮调用的函数"""
    global EC
    varEnglish.set("English")
    varChinese.set("Chinese")
    if EC==0:
        EC=1
    else:
        EC=0

##英文和中文显示的内容变量，调用他们的set方法就可以改变显示的内容
varEnglish = tk.StringVar()
varChinese = tk.StringVar()

##定义并放置用于显示英语汉语的标签
enL=tk.Label(textvar=varEnglish,font=("黑体",24))
enL.pack()
enC=tk.Label(textvar=varChinese,font=("宋体",14))
enC.pack()

##定义并放置show和change按钮
showBu = tk.Button(root,text='show',command=showCallBack,background='#00ff00')
changeBu = tk.Button(root,text='change',command=changeCallBack,background='#0000ff')
showBu.pack()
changeBu.pack()

##定义并放置输入英语和汉语的文本框
enE=tk.Entry(root,width=80,font=("黑体",24))
enE.pack()
enC=tk.Entry(root,width=50,font=("宋体",14))
enC.pack()

##把文本框中的数据存入文件中
def insertCallBack():
    """点击insert按钮调用的函数"""
    global elmdict
    enEStr=enE.get()
    enCStr=enC.get()
    elmDict[enEStr]=enCStr
    f=codecs.open("elm.txt","a",encoding="utf8")
    f.write(enEStr+'%'+enCStr+'\n')
    f.close()
    enE.delete(0,'end')
    enC.delete(0,'end')

##定义并放置insert按钮
insertBu = tk.Button(root,text='insert',command=insertCallBack,bg="#ff0000")
insertBu.pack()

#启动主程序
root.mainloop()


##problem:
#1.可能插入空白到文件中
#2.前后点击的题目重复，体验不好
#3.change按钮最好在点完两次show按钮后再点，否则体验不好

##idea:
#1.每个合作人有自己的文件，在界面上可以通过一个下拉菜单选择或单选框