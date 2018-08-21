import pyaudio
import numpy as np
import time


class CountIn():
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.volume = 1
        self.sampling_rate = 44100
        self.duration = 1.0
        self.f = 440.0
        # Replace self.sampling_rate with 440 in (self.sampling_rate*self.duration) for 'Click'
        self.wave = (np.sin(2 * np.pi * np.arange(self.sampling_rate * self.duration) * self.f / self.sampling_rate)).astype(np.float32)


    def count(self, count_val):
        for count in range(count_val):
            stream = self.p.open(format=pyaudio.paFloat32,
                            channels=1,
                            rate= self.sampling_rate,
                            output=True)

            stream.write(self.volume * self.wave)
            stream.stop_stream()
            # hardcoded BPM
            time.sleep(0.4)
            stream.close()
