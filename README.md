# Proyecto Integrador Codelabs

Este repositorio contiene una colección de codelabs prácticos de inteligencia artificial, visión por computadora y procesamiento de voz. Cada codelab es independiente y aborda un problema o técnica diferente, ideal para aprendizaje y experimentación.

## Estructura de carpetas

- **codelab1/codelab_reconocimiento_voz/**
  - Reconocimiento de voz y comandos hablados en español. Permite grabar audio, transcribirlo y ejecutar comandos como abrir Google, consultar la hora, buscar en YouTube, contar chistes y traducir frases.
  - Script principal: `voz_archivo.py`

- **codelab2/codelab_reconocimiento_imagenes/**
  - Reconocimiento de rostros en imágenes y videos. Incluye ejemplos de detección automática y manual.
  - Scripts: `rostros.py`, `rostros-manual.py`, notebook de ejemplo: `codelab.ipynb`

- **codelab3/codelab_video/**
  - Captura y procesamiento de video en tiempo real desde cámara web.
  - Script: `cam.py`

- **codelab4/codelab_compuerta_xor/**
  - Implementación de una compuerta lógica XOR usando redes neuronales.
  - Script: `compuerta_xor.py`

- **codelab5/codelab_yolo_lite/**
  - Detección de objetos en imágenes y video usando YOLO Lite.
  - Scripts: `yolo_lite.py`, `yolo_cam.py`
  - Incluye modelos y ejemplos de imágenes.

- **codelab6/codelab_deteccion_ssd/**
  - Detección de objetos con el modelo SSD (Single Shot Detector).
  - Scripts: `visualizacion_ssd.py`, `imagen_ssd.py`

- **codelab7/codelab_clasificador_comentarios/**
  - Clasificación de comentarios usando modelos de machine learning.
  - Script: `clasificador-comentarios-negocio.py`
  - Incluye modelos preentrenados (`modelo.joblib`, `tfidf.joblib`).

## Requisitos generales

- Python 3.8+
- Instalar dependencias específicas en cada carpeta (ver `requirements.txt` si existe)
- Recomendado: crear un entorno virtual para cada codelab

## Ejemplo de uso (reconocimiento de voz)

```bash
cd codelab1/codelab_reconocimiento_voz
pip install -r requirements.txt
python voz_archivo.py
```

## Créditos

Desarrollados para la materia Proyecto Integrador II

### Alejandro Marin Hoyos
### 2259353
