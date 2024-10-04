import unittest
from unittest.mock import patch, MagicMock
import sounddevice as sd
import wave
import os

# Importiere die zu testenden Funktionen aus main.py
from main import list_devices, record_audio

class TestAudioRecording(unittest.TestCase):
    
    @patch('sounddevice.query_devices')
    def test_list_devices(self, mock_query_devices):
        """Testet, ob list_devices korrekt arbeitet"""
        mock_query_devices.return_value = [
            {"name": "Device 1", "max_input_channels": 2, "max_output_channels": 0},
            {"name": "Device 2", "max_input_channels": 1, "max_output_channels": 2},
        ]
        
        # Aufrufen der Funktion list_devices
        list_devices()
        mock_query_devices.assert_called_once()

    @patch('sounddevice.rec')
    @patch('sounddevice.wait')
    @patch('wave.open')
    def test_record_audio(self, mock_wave_open, mock_sd_wait, mock_sd_rec):
        """Testet, ob die Aufnahme korrekt arbeitet und eine WAV-Datei erstellt"""
        mock_wave = MagicMock()
        mock_wave_open.return_value.__enter__.return_value = mock_wave
        
        # Aufruf der Funktion record_audio
        record_audio("test_output.wav", sample_rate=44100, channels=2, duration=5)
        
        # Verifiziere, ob sounddevice.rec korrekt aufgerufen wurde
        mock_sd_rec.assert_called_with(int(5 * 44100), samplerate=44100, channels=2)
        
        # Verifiziere, ob wave Datei geschrieben wurde
        mock_wave.writeframes.assert_called_once()
        
        # Prüfe, ob die Datei korrekt gespeichert wurde
        mock_wave_open.assert_called_with("test_output.wav", 'wb')
    
    def test_recording_creates_file(self):
        """Testet, ob die Datei korrekt erstellt wurde"""
        filename = "test_output.wav"
        if os.path.exists(filename):
            os.remove(filename)
        
        # Tatsächliche Aufnahme testen (5 Sekunden)
        record_audio(filename, sample_rate=44100, channels=2, duration=1)
        
        # Überprüfe, ob die Datei erstellt wurde
        self.assertTrue(os.path.exists(filename))
        
        # Bereinigen (Datei löschen)
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
