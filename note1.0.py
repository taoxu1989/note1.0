#!/usr/bin/env python3
#-*-encoding:utf8

__author__= "taoxu"

from tkinter import *
#初始化Tk

root = Tk()
root.title('XT Node')
root.geometry("800x500+100+100")
#三个主模块的建立

#create menu
menubar = Menu(root)
root.config(menu = menubar)


#文件
filemenu = Menu(menubar)
def new():
  root.title('未命名文件')
  filename = None
  textpad.delete(1.0,END)

filemenu.add_command(label = '新建',accelerator ='ctrl + N',command = new)
#打开
from tkinter.filedialog import *
def openfile():
  global filename
  filename = askopenfilename(defaultextension = '.txt')
  if filename == '':
    filename = None
  else:
    root.title('FileName:'+os.path.basename(filename))
    textpad.delete(1.0,END)
    f = open(filename,'r')
    textpad.insert(1.0,f.read())
    f.close()

filemenu.add_command(label = '打开',accelerator ='ctrl + O',command = openfile)

#保存
def save():
  global filename
  try:
    f = open(filename,'w')
    msg = textpad.get(1.0,END)
    f.write(msg)
    f.close()
  except:
    saveas()

filemenu.add_command(label = '保存',accelerator ='ctrl + S', command = save)

#另存为
def saveas():
  f = asksaveasfilename(initialfile= '未命名.txt', defaultextension='.txt')
  global filename
  filename = f
  fh = open(f,'w')
  msg = textpad.get(1.0,END)
  fh.write(msg)
  fh.close()
  root.title('FileName:'+os.path.basename(f))

filemenu.add_command(label = '另存为',accelerator ='ctrl + Shift + s', command = saveas)

menubar.add_cascade(label = '文件',menu = filemenu)

#编辑
editmenu = Menu(menubar)
def undo():
  textpad.event_generate('<<Undo>>')
editmenu.add_command(label = '撤销',accelerator = 'ctrl + z', command = undo)
def redo():
  textpad.event_generate('<<Redo>>')
editmenu.add_command(label = '重做',accelerator = 'ctrl + y', command = redo)
def copy():
  textpad.event_generate('<<Copy>>')
editmenu.add_command(label = '复制',accelerator = 'ctrl + c', command = copy)
def cut():
  textpad.event_generate('<<Cut>>')
editmenu.add_command(label = '剪切',accelerator = 'ctrl + x', command = cut)
def paste():
  textpad.event_generate('<<Paste>>')
editmenu.add_command(label = '粘贴',accelerator = 'ctrl + v', command = paste)
def search():
  topsearch = Toplevel(root)
  topsearch.geometry('300x30+200+250')
  label1 = Label(topsearch,text='Find')
  label1.grid(row=0, column=0,padx=5)
  entry1 = Entry(topsearch,width=20)
  entry1.grid(row=0, column=1,padx=5)
  button1 = Button(topsearch,text='查找')
  button1.grid(row=0, column=2)
editmenu.add_command(label = '查找',accelerator = 'ctrl + F', command = search)
def selectAll():
  textpad.tag_add('sel','1.0',END)
editmenu.add_command(label = '全选',accelerator = 'ctrl + A', command = selectAll)

menubar.add_cascade(label = '编辑',menu = editmenu)

#关于
from tkinter.messagebox import *
def author():
  showinfo('作者信息','本软件由taoxu1989@gmail.com完成')
def about():
  showinfo('版权信息.copyright','版权属于taoxu1989@gmail.com')
aboutmenu = Menu(menubar)
aboutmenu.add_command(label = '作者',command = author)
aboutmenu.add_command(label = '版权',command = about)
menubar.add_cascade(label = '关于',menu = aboutmenu)

#在记事本中添加toolbar,添加对应的button并设定合适的间距

toolbar = Frame(root,height = 15,bg = 'SkyBlue')

shortButton = Button(toolbar,text = '新建',command = new)
shortButton.pack(side = LEFT)

shortButton = Button(toolbar,text = '打开',command = openfile)
shortButton.pack(side = LEFT,padx = 5,pady = 5)

shortButton = Button(toolbar,text = '保存',command = save)
shortButton.pack(side = RIGHT)

shortButton = Button(toolbar,text = '撤销',command = undo)
shortButton.pack(side = RIGHT,padx = 5,pady = 5)
toolbar.pack(expand = NO,fill = X)

#创建状态栏(statusbar)和正文编辑区域

#编辑状态栏（statusbar）
status = Label(root,text = 'Ln20',bd = 1,relief = SUNKEN,anchor = 'w')
status.pack(side = BOTTOM,fill = X)
#正文编辑区域和滚动条
lnlabel = Label(root,width = 1)
lnlabel.pack(side = LEFT,fill = Y)

textpad = Text(root,undo = True)
textpad.pack(expand = YES,fill = BOTH)

scroll = Scrollbar(textpad)
textpad.config(yscrollcommand = scroll.set)
scroll.config(command = textpad.yview)
scroll.pack(side = RIGHT,fill = Y)

#模块的实现


mainloop()