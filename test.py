import snowboydecoder
import signal

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

# 语音唤醒之后播放的应答
model = 'resources/models/snowboy.umdl'

# 终止方法为ctrl+c
signal.signal(signal.SIGINT, signal_handler)

# 这里可以设置识别灵敏度
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

def callback():
    print("唤醒之后的回调函数")
    print("在这里实现唤醒之后需要进行的操作")

detector.start(detected_callback=callback, # 自定义回调函数
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

# 释放资源
detector.terminate()
