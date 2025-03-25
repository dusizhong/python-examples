import cv2
import tkinter
from tkinter import *
from datetime import datetime
from time import sleep
from PIL import ImageGrab
import os
import numpy

# 设置输出视频的帧率
fps = 30.0

out = None  # 用于保存录屏结果的 VideoWriter 对象
is_recording = False  # 标记是否正在录制

# 用于记录选定区域的坐标
start_x, start_y = None, None
end_x, end_y = None, None
canvas = None

#用来显示全屏幕截图并响应二次截图的窗口类
class MyCapture:
    def __init__(self, png):
        #变量X和Y用来记录鼠标左键按下的位置
        self.X = tkinter.IntVar(value=0)
        self.Y = tkinter.IntVar(value=0)
        #屏幕尺寸
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        #创建顶级组件容器
        self.top = tkinter.Toplevel(root, width=screenWidth, height=screenHeight)
        #不显示最大化、最小化按钮
        self.top.overrideredirect(True)
        self.canvas = tkinter.Canvas(self.top,bg='white', width=screenWidth, height=screenHeight)
        #显示全屏截图，在全屏截图上进行区域截图
        self.image = tkinter.PhotoImage(file=png)
        self.canvas.create_image(screenWidth//2, screenHeight//2, image=self.image)
        #鼠标左键按下的位置
        def onLeftButtonDown(event):
            self.X.set(event.x)
            self.Y.set(event.y)
            #开始截图
            self.sel = True
        self.canvas.bind('<Button-1>', onLeftButtonDown)
        #鼠标左键移动，显示选取的区域
        def onLeftButtonMove(event):
            if not self.sel:
                return
            global lastDraw
            try:
                #删除刚画完的图形，要不然鼠标移动的时候是黑乎乎的一片矩形
                self.canvas.delete(lastDraw)
            except Exception as e:
                pass
            lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='green')
        self.canvas.bind('<B1-Motion>', onLeftButtonMove)
        #获取鼠标左键抬起的位置，保存区域截图
        def onLeftButtonUp(event):
            global start_x, start_y ,end_x, end_y
            self.sel = False
            try:
                self.canvas.delete(lastDraw)
            except Exception as e:
                pass
            sleep(0.1)
            #考虑鼠标左键从右下方按下而从左上方抬起的截图
            start_x, end_x = sorted([self.X.get(), event.x])
            start_y, end_y = sorted([self.Y.get(), event.y])
            self.top.destroy()
        self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
        #让canvas充满窗口，并随窗口自动适应大小
        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

def start_recording():
    global out, is_recording, start_x, start_y, end_x, end_y
    # 设置屏幕录制的宽度和高度
    screen_width = abs(end_x - start_x)
    screen_height = abs(end_y - start_y)
    # 创建输出文件名（使用当前时间段命名）
    now = datetime.now()
    output_file = now.strftime("%Y%m%d_%H%M%S") + ".mp4"
    # 创建 VideoWriter 对象
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_file, fourcc, fps, (screen_width, screen_height))
    is_recording = True
    # 截图结束，恢复主窗口，并删除临时的全屏幕截图文件
    root.state('normal')
    record_screen()

def stop_recording_and_save():
    global out, is_recording
    is_recording = False

def record_screen():
    global is_recording,start_x, start_y, end_x, end_y
    # 如果正在录制，则写入视频文件
    if is_recording:
        img = ImageGrab.grab((start_x, start_y, end_x, end_y))
        img_np = numpy.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)  # ImageGrab获取的颜色为BGR排序，需转换为RGB
        out.write(frame)
        # 保持循环
        root.after(1, record_screen)
    else:
        out.release()
        cv2.destroyAllWindows()
        
def createcanvas():
    #最小化主窗口
    root.state('icon')
    sleep(0.2)
    filename = 'temp.png'
    #grab()方法默认对全屏幕进行截图
    im = ImageGrab.grab()
    im.save(filename)
    im.close()
    #显示全屏幕截图
    w = MyCapture(filename)
    select_button.wait_window(w.top)
    #截图结束，恢复主窗口，并删除临时的全屏幕截图文件
    root.state('normal')
    os.remove(filename)

# 创建 Tkinter 窗口
root = Tk()
root.geometry("250x50")

select_button = Button(root, text="录制区域", command=createcanvas)
select_button.pack(side=LEFT)

# 创建开始录制按钮
start_button = Button(root, text="开始录制", command=start_recording)
start_button.pack(side=LEFT)

# 创建停止录制并保存按钮
stop_button = Button(root, text="停止录制", command=stop_recording_and_save)
stop_button.pack(side=LEFT)

# 运行 Tkinter 窗口主循环
root.mainloop()