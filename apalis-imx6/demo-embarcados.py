import snowboydecoder
import sys
import signal
import numpy as np

# Demo code for listening to two hotwords at the same time

interrupted = False

led = 0
path = "/sys/class/gpio/gpio"
addr_leds = np.array(["36", "37", "38", "39", "170"])
val = "/value"


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted



def detect_acende():
    global led
    if led > 4:
        led = 0
    f = open(path + addr_leds[led] + val, "w")
    f.write("1")
    led += 1

def detect_apaga():
    global led
    led -= 1
    if led < 0:
        led = 4
    f = open(path + addr_leds[led] + val, "w")
    f.write("0")


if len(sys.argv) != 3:
    print("Error: need to specify 2 model names")
    print("Usage: python demo.py 1st.model 2nd.model ")
    sys.exit(-1)



models = sys.argv[1:]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

sensitivity = [0.5]*len(models)

detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)

callbacks = [lambda: detect_acende(), 
             lambda: detect_apaga()] 

print('Listening... Press Ctrl+C to exit')

# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
