import tkinter as tk
from tkinter import ttk
import sounddevice as sd

# Grundlegende Audio-Einstellungen
SAMPLE_RATE = 44100  # Standard-Sample-Rate
CHANNELS = 2  # Stereo

# Funktion zur Aufnahme von Audio (noch ohne Speicherung)
def start_recording():
    duration = int(duration_entry.get())  # Dauer der Aufnahme
    sample_rate = int(sample_rate_combo.get())  # Abtastrate
    device = input_device_combo.current()  # Gewähltes Gerät
    
    print(f"Starte Aufnahme: Dauer {duration}s, Abtastrate {sample_rate}, Gerät {device}")
    
    # Audioaufnahme starten (noch ohne Speicherung)
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=CHANNELS)
    sd.wait()  # Aufnahme blockieren
    print("Aufnahme beendet.")

# Funktion zur Auflistung der Eingabegeräte
def list_input_devices():
    devices = sd.query_devices()
    input_devices = [device['name'] for device in devices if device['max_input_channels'] > 0]
    return input_devices

# GUI-Setup
root = tk.Tk()
root.title("Audio Recorder GUI")

# Eingabegerät-Auswahl
input_device_label = ttk.Label(root, text="Eingabegerät:")
input_device_label.grid(row=0, column=0, padx=10, pady=5)

input_device_combo = ttk.Combobox(root, values=list_input_devices())
input_device_combo.grid(row=0, column=1, padx=10, pady=5)
input_device_combo.current(0)

# Abtastraten-Auswahl
sample_rate_label = ttk.Label(root, text="Abtastrate:")
sample_rate_label.grid(row=1, column=0, padx=10, pady=5)

sample_rate_combo = ttk.Combobox(root, values=[44100, 48000, 96000])
sample_rate_combo.grid(row=1, column=1, padx=10, pady=5)
sample_rate_combo.current(0)

# Eingabefeld für Dauer
duration_label = ttk.Label(root, text="Dauer (Sekunden):")
duration_label.grid(row=2, column=0, padx=10, pady=5)

duration_entry = ttk.Entry(root)
duration_entry.grid(row=2, column=1, padx=10, pady=5)
duration_entry.insert(0, "5")

# Aufnahme-Start-Button
record_button = ttk.Button(root, text="Aufnahme starten", command=start_recording)
record_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# GUI starten
root.mainloop()
