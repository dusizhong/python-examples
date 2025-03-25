import cv2
import numpy as np
from PIL import ImageGrab
from tkinter import *
from datetime import datetime

is_recording = False
out = None

def record_screen():
	global is_recording, out
	if out is None:
		output_file = datetime.now().strftime("%Y%m%d_%H%M%S") + ".mp4"
		fourcc = cv2.VideoWriter_fourcc(*"mp4v")
		screenshot = ImageGrab.grab()
		out = cv2.VideoWriter(output_file, fourcc, 30, screenshot.size)
	if is_recording:
		screenshot = ImageGrab.grab()
		frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
		out.write(frame)
		win.after(1, record_screen)
	else:
		out.release()
		out = None
		cv2.destroyAllWindows()

def record_audio():
	global is_recording, out
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 11025
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
	wf = wave.open("temp.wav", "wb")
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	if is_recording:
		wf.writeframes(stream.read(CHUNK))
	else:
		stream.stop_stream()
		stream.close()
		p.terminate()
		wf.close()

def compose_video():
	print("正在合成音视频文件...")
	print("合成完毕")


def start_record():
	global is_recording, out
	is_recording = True
	record_screen()
	print('开始录制...')
	
def stop_record():
	global is_recording, out
	is_recording = False
	print('停止录制')

win = Tk()
win.title('Screener录屏小工具')
start_button = Button(win, text="开始录制", command=start_record)
start_button.pack(side=LEFT)
start_button = Button(win, text="停止录制", command=stop_record)
start_button.pack(side=LEFT)
win.mainloop()