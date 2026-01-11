import pyttsx3
import time

# Inisialisasi engine suara
engine = pyttsx3.init()

# Atur kecepatan bicara (semakin kecil, semakin lambat)
engine.setProperty('rate', 130)  # default 200
engine.setProperty('volume', 1.0)

# Pilih suara Bahasa Indonesia (jika tersedia di sistem)
voices = engine.getProperty('voices')
for voice in voices:
    if "id" in voice.id.lower() or "indonesia" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

print("=== Pembaca TOKEN Otomatis ===")
token = input("Masukkan TOKEN ujian: ").strip()

print("\nMembacakan TOKEN...")
for huruf in token:
    print(huruf)
    engine.say(huruf)
    engine.runAndWait()
    time.sleep(0.8)  # jeda antar huruf (dapat diubah)

print("\nTOKEN selesai dibacakan.")
