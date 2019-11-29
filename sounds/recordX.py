import pyaudio
import wave
chunk = 8192
formats = pyaudio.paInt16
channels = 1
rate = 44100
record_sec = 7
wave_output = "sourceY.wav"
p = pyaudio.PyAudio()
stream = p.open(format = formats, channels = channels, rate = rate, input = True, frames_per_buffer = chunk)
frames = []
print("start")
for i in range(0,int(rate/chunk*record_sec)):
    data = stream.read(chunk)
    frames.append(data)

print("done")
stream.stop_stream()
stream.close()
p.terminate()
wf = wave.open(wave_output,"wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(formats))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()
