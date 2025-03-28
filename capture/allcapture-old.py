import pyaudio
import wave
from PIL import ImageGrab
import cv2
import threading
import time
from numpy import array
from moviepy.editor import *
import os
'''
pyaudio录制音频
openCV录制屏幕及对个人录像
moviepy对录制的音频、录屏及录像文件同步合成。
'''

class PyRecord:
    def __init__(self, file_path="test"):
        self.allow_record = True
        self.file_path = file_path

    def record_audio(self):
        # 如无法正常录音 请启用计算机的"立体声混音"输入设备
        #每个缓冲区的帧数
        CHUNK = 1024
        #采样位数
        FORMAT = pyaudio.paInt16
        #立体声道
        CHANNELS = 2
        #采样频率
        RATE = 11025
        p = pyaudio.PyAudio()
        #录制音频
        stream = p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK,
        )
        wf = wave.open(self.file_path + ".wav", "wb")
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        while self.allow_record:
            data = stream.read(CHUNK)
            wf.writeframes(data)

        stream.stop_stream()
        stream.close()
        p.terminate()
        wf.close()

    def record_screen(self):
        #屏幕抓取
        im = ImageGrab.grab()
        #cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')，视频编码，标识帧中每个像素的存储格式
        #10：表示保存视频文件所使用的帧速率，通常30或更高
        video = cv2.VideoWriter(
            self.file_path + ".avi", cv2.VideoWriter_fourcc(*"XVID"), 10, im.size
        )
        while self.allow_record:
            im = ImageGrab.grab()
            #图片颜色处理
            im = cv2.cvtColor(array(im), cv2.COLOR_RGB2BGR)
            video.write(im)
        video.release()

    def compose_file(self):
        print("合并视频&音频文件")
        audio = AudioFileClip(self.file_path + ".wav")
        video = VideoFileClip(self.file_path + ".avi")
        ratio = audio.duration / video.duration
        video = video.fl_time(lambda t: t / ratio, apply_to=["video"]).set_end(
            audio.duration
        )
        video = video.set_audio(audio)
        video = video.volumex(5)
        video.write_videofile(
            self.file_path + "_out.avi", codec="libx264", fps=10, logger=None
        )
        video.close()
        print("合并完成")

    def remove_temp_file(self):
        print("删除缓存文件")
        os.remove(self.file_path + ".wav")
        os.remove(self.file_path + ".avi")

    def stop(self):
        print("停止录制")
        self.allow_record = False
        time.sleep(1)
        self.compose_file()
        #self.remove_temp_file()

    def run(self):
        t = threading.Thread(target=self.record_screen)
        t1 = threading.Thread(target=self.record_audio)
        t.start()
        t1.start()
        print("开始录制")


pr = PyRecord()
pr.run()
time.sleep(50)
pr.stop()

