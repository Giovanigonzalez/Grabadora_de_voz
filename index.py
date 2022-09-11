import sounddevice

from scipy.io.wavfile import write

fs=44100

second=int(input("ingrese duracion en segundos: "))
print("recording...\n")

recor_voice=sounddevice.rec(int(second+fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fas,recor_voice)
print("finished..\nplease check it...")