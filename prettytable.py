import queue 安装失败，用from multiprocessing import Queue代替

get 返回dict对象中的指定值
dict = {'Name': 'Zara', 'Age': 27}

print "Value : %s" %  dict.get('Age')
print "Value : %s" %  dict.get('Sex', "Never")

Python find() 方法检测字符串中是否包含子字符串 str
str.find(str, beg=0, end=len(string))

Python Signal 信号
signal.signal(signal.SIGINT, handler)

转载 2014年04月25日 09:55:19 标签：python /编程 /通讯 20443
信号的概念
信号（signal）--     进程之间通讯的方式，是一种软件中断。一个进程一旦接收到信号就会打断原来的程序执行流程来处理信号。
几个常用信号:
SIGINT     终止进程  中断进程  (control+c)
SIGTERM   终止进程     软件终止信号
SIGKILL   终止进程     杀死进程
SIGALRM 闹钟信号
