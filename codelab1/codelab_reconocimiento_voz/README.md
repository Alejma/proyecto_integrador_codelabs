# 🎤 CODELAB Reconocimiento de voz con Python

Este CODELAB es un asistente de voz sencillo en **Python** que permite reconocer comandos hablados y ejecutar acciones como:

- 👋 Saludo inicial  
- ⏰ Consultar la hora  
- 🌤️ Consultar el clima en una ciudad  
- 🎵 Buscar en YouTube  
- 😂 Contar chistes  
- 🌍 Traducir frases con Google Translate  

---

## 🚀 Requisitos

- Python 3.8 o superior  
- Un micrófono conectado y configurado como predeterminado en tu sistema operativo  
- Librerías de Python (instalación abajo)  

---

## 📦 Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/asistente-voz.git
   cd asistente-voz
   ```

2. Crear un entorno virtual:
   ```bash
   python -m venv .venv
   ```

3. Activar el entorno virtual:
   - **Windows (PowerShell):**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD):**
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **Linux / Mac:**
     ```bash
     source .venv/bin/activate
     ```

4. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Uso

Ejecuta el script:

```bash
python voz_archivo.py
```

Habla después del mensaje **"Grabando... habla ahora!"**.  
El asistente procesará tu voz y ejecutará comandos.

---

## 🎮 Comandos disponibles

- **"hola"** → Responde con un saludo.  
- **"hora"** → Muestra la hora actual.  
- **"clima en [ciudad]"** → Consulta el clima en esa ciudad. Ej: *"clima en Medellín"*.  
- **"abrir youtube [búsqueda]"** → Busca en YouTube. Ej: *"abrir youtube Shakira"*.  
- **"chiste"** → Cuenta un chiste aleatorio.  
- **"traducir [frase] al inglés"** → Traduce al inglés. Ej: *"traducir hola mundo al inglés"*.  
- **"traducir [frase] al español"** → Traduce al español. Ej: *"translate good morning al español"*.  

---

## 📂 Estructura del proyecto

```
asistente-voz/
│── voz_archivo.py       # Script principal
│── requirements.txt     # Dependencias del proyecto
│── README.md            # Documentación
```

---

## 📋 requirements.txt

Este proyecto usa las siguientes dependencias mínimas:

```
sounddevice
scipy
SpeechRecognition
requests
googletrans==4.0.0-rc1
```

---