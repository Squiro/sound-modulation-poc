from constants import SAMPLE_RATE
import numpy as np
import matplotlib.pyplot as plt


def string_to_binary(text: str):
    binary_output = []
    for char in text:
        binary = format(ord(char), "08b")
        binary_output.append(binary)
    return "".join(binary_output)


def plot_signal(data):
    length = data.shape[0] / SAMPLE_RATE
    time = np.linspace(0.0, length, data.shape[0])

    plt.plot(time, data, label="channel")

    plt.legend()

    plt.xlabel("Time [s]")

    plt.ylabel("Amplitude")

    plt.show()
