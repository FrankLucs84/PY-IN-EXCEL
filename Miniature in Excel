# Guida Dettagliata: Creazione di Miniature con Python in Excel

Questa guida spiega passo passo come creare miniature di immagini utilizzando Python integrato in Microsoft Excel e la libreria Pillow.

---

## **1. Preparazione: Requisiti e Configurazione**

### **Software Necessario**
- **Microsoft Excel** con supporto per **Python** integrato (richiede Microsoft 365).
- **Python Environment** (se necessario, al di fuori di Excel).

### **Librerie Utilizzate**
- **`Pillow` (PIL)**: Una libreria Python per manipolare immagini.

Per installare Pillow, usa il seguente comando:
```bash
pip install pillow
```

---

## **2. Caricamento delle Immagini**

Le immagini possono essere caricate in due modi:

### **Opzione 1: Dati in Excel**
1. Usa **Power Query** o importa i dati immagine in una colonna di Excel (ad esempio, codificati in `Base64`).
2. Decodifica i dati immagine in Python.

**Codice di esempio per decodificare immagini in Base64:**
```python
from PIL import Image
import io
import base64

# Supponendo che le immagini siano in una colonna di Excel
image_data_base64 = Excel.Range("ImageColumn").Value  # Specifica la colonna esatta

# Decodifica in un array di immagini Pillow
images = [Image.open(io.BytesIO(base64.b64decode(data))) for data in image_data_base64]
```

### **Opzione 2: File Locali**
1. Salva le immagini in una directory locale.
2. Caricale in Python con Pillow:
```python
from PIL import Image
import os

# Directory contenente le immagini
image_folder = "path/to/images"

# Carica le immagini
images = [Image.open(os.path.join(image_folder, file)) for file in os.listdir(image_folder)]
```

---

## **3. Definizione delle Dimensioni delle Miniature**

1. **Inserisci i valori di larghezza e altezza desiderati in due celle di Excel.**
   - Ad esempio, inserisci **150** in una cella per la larghezza e **200** per l'altezza.

2. Recupera queste dimensioni con Python:
```python
# Supponendo che le dimensioni siano definite in due celle di Excel
target_resolution = Excel.Range("WidthCell:HeightCell").Value

# Converte l'array 2D in un array 1D
target_resolution = target_resolution.flatten()
```

---

## **4. Creazione delle Copie delle Immagini**

Per preservare le immagini originali, è importante creare copie profonde:
```python
thumbnails = [image.copy() for image in images]  # Copia delle immagini originali
```

---

## **5. Ridimensionamento delle Immagini (Thumbnail Creation)**

Ridimensiona le immagini utilizzando il metodo `thumbnail` di Pillow:
- Mantiene il rapporto d'aspetto.
- Usa il filtro **LANCZOS** per una qualità migliore.

**Codice per ridimensionare le immagini:**
```python
for image in thumbnails:
    image.thumbnail(target_resolution, Image.LANCZOS)  # Ridimensionamento con filtro di alta qualità
```

---

## **6. Salvataggio delle Miniature**

### **Opzione 1: Salva su Disco**
Puoi salvare le miniature come file:
```python
for idx, image in enumerate(thumbnails):
    image.save(f"thumbnail_{idx}.jpg", "JPEG")
```

### **Opzione 2: Salva in Excel**
Se vuoi salvare le miniature come dati in Excel (ad esempio in formato Base64):
```python
from io import BytesIO
import base64

thumbnail_data = []

# Converti ogni immagine in Base64
for image in thumbnails:
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    thumbnail_data.append(base64.b64encode(buffer.getvalue()).decode())

# Scrivi i dati in Excel
Excel.Range("ThumbnailColumn").Value = thumbnail_data  # Specifica la colonna
```

---

## **7. Visualizzazione del Risultato**

Puoi verificare le dimensioni delle miniature con:
```python
for image in thumbnails:
    print(image.size)  # Stampa le dimensioni
```

Se hai salvato le miniature in Excel, puoi visualizzarle direttamente.

---

## **Schema Completo del Codice**

Ecco il codice completo da eseguire:

```python
from PIL import Image
import io
import base64

# Step 1: Caricamento delle immagini
data_base64 = Excel.Range("ImageColumn").Value
images = [Image.open(io.BytesIO(base64.b64decode(data))) for data in data_base64]

# Step 2: Definizione della risoluzione
target_resolution = Excel.Range("WidthCell:HeightCell").Value.flatten()

# Step 3: Creazione di copie delle immagini
thumbnails = [image.copy() for image in images]

# Step 4: Ridimensionamento delle immagini
for image in thumbnails:
    image.thumbnail(target_resolution, Image.LANCZOS)

# Step 5: Salvataggio dei risultati
thumbnail_data = []
for image in thumbnails:
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    thumbnail_data.append(base64.b64encode(buffer.getvalue()).decode())

Excel.Range("ThumbnailColumn").Value = thumbnail_data
```

---

## **Note Finali**
- Assicurati di configurare correttamente i riferimenti alle celle di Excel.
- Se lavori al di fuori di Excel, puoi sostituire i riferimenti a `Excel.Range` con input manuali.
- Usa il filtro LANCZOS per una qualità superiore, ma considera che potrebbe essere più lento per grandi quantità di immagini.
