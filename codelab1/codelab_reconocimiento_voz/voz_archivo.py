import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import tempfile, os
import datetime
import requests
import webbrowser
import random
from googletrans import Translator


SRATE = 16000     # tasa de muestreo
DUR = 5           # segundos

print("Grabando... habla ahora!")
audio = sd.rec(int(DUR*SRATE), samplerate=SRATE, channels=1, dtype='int16')
sd.wait()
print("Listo, procesando...")

# guarda a WAV temporal
tmp_wav = tempfile.mktemp(suffix=".wav")
write(tmp_wav, SRATE, audio)

# reconoce con SpeechRecognition
r = sr.Recognizer()
with sr.AudioFile(tmp_wav) as source:
    data = r.record(source)

try:
    texto = r.recognize_google(data, language="es-ES")
    print("Dijiste:", texto)
except sr.UnknownValueError:
    print("No se entendió el audio.")
except sr.RequestError as e:
    print("Error:", e)
finally:
    if os.path.exists(tmp_wav):
        os.remove(tmp_wav)

cmd = texto.lower()

# ============================
# Comandos disponibles
# ============================
if "hola" in cmd:
    print("¡Hola, bienvenido al curso!")

elif "abrir google" in cmd:
    webbrowser.open("https://www.google.com")

elif "hora" in cmd:
    print("Hora actual:", datetime.now().strftime("%H:%M"))

# --- NUEVOS COMANDOS ---

# --- CLIMA ---
elif "clima" in cmd:
    ciudad = "tulua"
    url = f"https://wttr.in/{ciudad}?format=3"
    try:
        clima = requests.get(url).text
        print("Clima actual:", clima)
    except:
        print("No pude obtener el clima.")

# --- YOUTUBE ---

elif "youtube" in cmd:
    # Dividimos el comando en palabras
    partes = cmd.split("youtube", 1)  # divide en 2 partes
    if len(partes) > 1 and partes[1].strip():
        busqueda = partes[1].strip()   # lo que viene después de "youtube"
    else:
        busqueda = "canciones populares"  # valor por defecto

    webbrowser.open(f"https://www.youtube.com/results?search_query={busqueda}")
    print(f"Buscando en YouTube: {busqueda}")

# --- CHISTE ---
elif "chiste" in cmd:
    chistes = [
        "¿Por qué los programadores confunden Halloween y Navidad? Porque OCT 31 = DEC 25.",
        "¡Error 404! El chiste no fue encontrado.",
        "¿Qué le dijo un bit al otro? Nos vemos en el bus."
    ]
    print(random.choice(chistes))

# --- TRADUCTOR ---
elif "traducir" in cmd:
    traductor = Translator()
    partes = cmd.split("traducir", 1)
    frase = partes[1].strip() if len(partes) > 1 else ""

    if "al inglés" in frase:
        frase = frase.replace("al inglés", "").strip()
        resultado = traductor.translate(frase, dest="en")
        print(f"Traducción al inglés: {resultado.text}")

    elif "al español" in frase:
        frase = frase.replace("al español", "").strip()
        resultado = traductor.translate(frase, dest="es")
        print(f"Traducción al español: {resultado.text}")

    else:
        resultado = traductor.translate(frase, dest="en")
        print(f"Traducción: {resultado.text}")

else:
    print("Comando no reconocido.")