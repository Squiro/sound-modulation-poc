import math
import struct
import wave
import pyaudio
from constants import (
    BEEP_LENGTH_IN_MS,
    FORMAT,
    FRAMES_PER_BEEP,
    FREQUENCY,
    PATTERN,
    SAMPLE_RATE,
)
from utils import string_to_binary


def get_length_in_seconds(data: str):
    return (len(data) * BEEP_LENGTH_IN_MS) / 1000


def generate_encoding_pattern():
    number_of_frames = math.ceil(len(PATTERN) * FRAMES_PER_BEEP)
    print("Pattern frame lenght: ", number_of_frames)

    data = []
    for i in range(number_of_frames):
        index = math.floor((i / (FRAMES_PER_BEEP)))
        r = int(PATTERN[index]) * math.sin(2 * math.pi * FREQUENCY * (i / SAMPLE_RATE))
        data.append(struct.pack("h", int(r * 32767.0)))
    return data


TEXT_DATA = "hola mundo!"

binary_output = string_to_binary(TEXT_DATA)
length_in_seconds = get_length_in_seconds(binary_output)
number_of_frames = int(SAMPLE_RATE * length_in_seconds)

print("Text ouput in binary: ", binary_output)
print("Number of frames (w/o encoding pattern)", number_of_frames)

wavedata = generate_encoding_pattern()

for frame in range(number_of_frames):
    index = math.floor((frame / (FRAMES_PER_BEEP)))
    volume = int(binary_output[index])
    frame_result = volume * math.sin(2 * math.pi * FREQUENCY * (frame / SAMPLE_RATE))
    wavedata.append(struct.pack("h", int(frame_result * 32767.0)))

wavedata = wavedata + generate_encoding_pattern()

end_result = b"".join(wavedata)

audio = pyaudio.PyAudio()

# Uncomment this if you want to hear it play before generating the WAV file
# stream = audio.open(format=FORMAT, channels=1, rate=SAMPLE_RATE, output=True)
# stream.write(end_result)
# stream.stop_stream()
# stream.close()
# audio.terminate()

waveFile = wave.open("test.wav", "wb")
waveFile.setnchannels(1)
waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
waveFile.setframerate(SAMPLE_RATE)
waveFile.writeframes(end_result)
waveFile.close()
