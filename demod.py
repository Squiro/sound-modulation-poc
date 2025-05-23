from scipy.io import wavfile
import numpy as np
from scipy import stats
from constants import FRAMES_PER_BEEP, PATTERN
from utils import plot_signal

AMPLITUDE_THRESHOLD = 200


# Find first amplitude peak
def find_peak(data):
    it = np.nditer(data, flags=["f_index"])
    for x in it:
        if abs(x) >= AMPLITUDE_THRESHOLD:
            print(f"Amplitude peak {x} at idx {it.index}")
            return it.index


def demod(filename: str):
    sr, data = wavfile.read(filename)
    peak_index = find_peak(data)
    if peak_index == -1:
        print("No peak amplitude found")
        return

    array_to_process = data[peak_index:]
    process_frames(array_to_process)
    plot_signal(data)


def process_frames(data):
    arr_length = data.shape[0]
    bit_list = []

    fpr = int(FRAMES_PER_BEEP)
    start = 0
    end = fpr
    while end < arr_length:
        temp_arr = data[start:end]
        np.abs(temp_arr, out=temp_arr)
        # Count number of times amplitude is bigger than threshold
        val = (temp_arr >= AMPLITUDE_THRESHOLD).sum()
        # print(val)

        # Previous experiments that used mean / mode
        # m = stats.mode(temp_arr)
        # val = abs(np.mean(temp_arr))
        # print("mean: ", val)
        # mode = abs(m[0][0])
        # print("mode: ", mode)
        bit_list.append("1" if val >= 200 else "0")
        start += fpr
        end += fpr

    bit_string = "".join(bit_list)
    print(bit_string)
    decode_bits(bit_string)


def decode_bits(bit_string: str):
    pattern_length = len(PATTERN)
    start = bit_string.find(PATTERN)

    if start == -1:
        print("Start pattern not found :(")
        return

    # remove starting pattern
    bit_string = bit_string[start + pattern_length :]
    print(bit_string)
    # remove end pattern
    end = bit_string.find(PATTERN)

    if end == -1:
        print("End pattern not found :(")
        return

    bit_string = bit_string[0:end]
    print(bit_string)

    decoded = ""
    bits_to_decode = ""

    for i in range(len(bit_string)):
        bits_to_decode = bits_to_decode + bit_string[i]
        if (i + 1) % 8 == 0:
            decoded = decoded + chr(int(bits_to_decode, 2))
            bits_to_decode = ""

    print(decoded)
