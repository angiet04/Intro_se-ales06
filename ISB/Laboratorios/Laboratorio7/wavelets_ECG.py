import numpy as np
import pywt
import matplotlib.pyplot as plt

def load_data(file_path, max_samples=15000):
    try:
        data = np.loadtxt(file_path, skiprows=10, max_rows=max_samples)
        return data[:, 5]
    except Exception as e:
        print(f"Fallo al cargar los datos: {e}")
        return None

def wavelet_denoising(data, wavelet='db4', level=9):
    coeffs = pywt.wavedec(data, wavelet, level=level)
    sigma = np.std(coeffs[-1])
    threshold = sigma * np.sqrt(2 * np.log(len(data))) * 2.0
    coeffs[1:] = [pywt.threshold(i, value=threshold, mode='soft') for i in coeffs[1:]]
    reconstructed_signal = pywt.waverec(coeffs, wavelet)
    return reconstructed_signal

def plot_signals(original, denoised, time, title_suffix):
    min_length = min(len(original), len(denoised), len(time))
    original = original[:min_length]
    denoised = denoised[:min_length]
    time = time[:min_length]

    plt.figure(figsize=(15, 18))
    plt.subplot(311)
    plt.plot(time, original, label='ECG Original', color='darkblue')
    plt.title(f'Señal ECG Original ', fontsize=14)
    plt.xlabel('Tiempo (s)', fontsize=12)
    plt.ylabel('Amplitud', fontsize=12)
    plt.legend(fontsize=10)

    plt.subplot(312)
    plt.plot(time, denoised, label='ECG Filtrada', color='darkgreen')
    plt.title(f'Señal ECG Filtrada ', fontsize=14)
    plt.xlabel('Tiempo (s)', fontsize=12)
    plt.ylabel('Amplitud', fontsize=12)
    plt.legend(fontsize=10)

    plt.subplot(313)
    plt.plot(time, original, label='ECG Original', linestyle='--', alpha=0.5, color='darkblue')
    plt.plot(time, denoised, label='ECG Filtrada', linewidth=2, color='darkred')
    plt.title(f'Comparación de ECG Original y Filtrada ', fontsize=14)
    plt.xlabel('Tiempo (s)', fontsize=12)
    plt.ylabel('Amplitud', fontsize=12)
    plt.legend(fontsize=10)

    plt.tight_layout(pad=3.0)
    plt.show()

sampling_frequency = 250  # Hz, adjust if different
files = ["romi-correcto.txt", "romi-reposo.txt"]
for file in files:
    data_path = f'C:\\Users\\ANGIE\\QW\\{file}'
    ecg_data = load_data(data_path)

    if ecg_data is not None:
        denoised_ecg = wavelet_denoising(ecg_data)
        time_array = np.linspace(0, len(ecg_data) / sampling_frequency, num=len(ecg_data))
        plot_signals(ecg_data, denoised_ecg, time_array, file.split('.')[0])
    else:
        print(f"No hay datos para procesar en el archivo {file}.")
