
# --------------------------------------
# 1) Le fondamenta in pratica: Variabili, Tipi di Dati e Operatori
# --------------------------------------

# Questo è un commento. Python ignora tutto ciò che inizia con #

# --- VARIABILI E TIPI DI DATI ---

# Assegniamo un numero intero (int) a una variabile chiamata 'eta'
eta = 30
print("L'età è:", eta) # La funzione print() mostra il valore a schermo

# Assegniamo un numero con la virgola (float) a una variabile chiamata 'altezza'
altezza = 1.75
print("L'altezza è:", altezza)

# Assegniamo una stringa (testo, str) a una variabile chiamata 'nome'
# Le stringhe vanno tra apici singoli '' o doppi ""
nome = "Mario Rossi"
print("Il nome è:", nome)

# Assegniamo un valore booleano (True o False, bool) a una variabile
# I booleani rappresentano valori di verità
studente = True
print("È uno studente?", studente)

# --- OPERATORI ARITMETICI DI BASE ---

numero1 = 10
numero2 = 5

somma = numero1 + numero2
print("Somma:", somma) # Output: 15

sottrazione = numero1 - numero2
print("Sottrazione:", sottrazione) # Output: 5

moltiplicazione = numero1 * numero2
print("Moltiplicazione:", moltiplicazione) # Output: 50

divisione = numero1 / numero2 # La divisione produce sempre un float
print("Divisione:", divisione) # Output: 2.0

# --- UN PICCOLO EXTRA: CONCATENAZIONE DI STRINGHE ---
# Puoi "sommare" le stringhe per unirle
saluto = "Ciao"
nome_utente = "Anna"
messaggio_completo = saluto + " " + nome_utente + "!" # Aggiungiamo uno spazio tra le stringhe
print(messaggio_completo) # Output: Ciao Anna!

# Python è un linguaggio "dinamicamente tipizzato", il che significa che non devi
# dichiarare esplicitamente il tipo di una variabile. Python lo capisce da solo!
# Ad esempio, 'eta' è diventato un intero quando gli abbiamo assegnato 30.

# --------------------------------------
# 2) Prendere decisioni e ripetere azioni: Istruzioni Condizionali e Cicli.
# --------------------------------------
# --- ISTRUZIONI CONDIZIONALI: if, elif, else ---

eta_utente = 20 # Prova a cambiare questo valore per vedere come cambia l'output!

print("Controllo l'età dell'utente...")

if eta_utente < 18:
    # Questo blocco di codice viene eseguito SOLO SE eta_utente è minore di 18
    print("L'utente è minorenne.")
    print("Alcune funzionalità potrebbero non essere disponibili.")
elif eta_utente == 18:
    # Questo blocco viene eseguito SOLO SE la prima condizione (eta_utente < 18) è falsa
    # E QUESTA condizione (eta_utente == 18) è vera
    print("L'utente ha esattamente 18 anni. Benvenuto tra i maggiorenni!")
elif eta_utente > 65:
    # Puoi avere quanti elif vuoi
    print("L'utente è un senior.")
else:
    # Questo blocco viene eseguito se NESSUNA delle condizioni precedenti è vera
    print("L'utente è maggiorenne.")

print("...controllo terminato.") # Questa riga è fuori dal blocco if/elif/else, quindi viene sempre eseguita

# --- OPERATORI DI CONFRONTO ---
# Nell'esempio sopra abbiamo usato:
# <   (minore di)
# ==  (uguale a - nota i due segni di uguale!)
# >   (maggiore di)

# Altri operatori di confronto utili:
# <=  (minore o uguale a)
# >=  (maggiore o uguale a)
# !=  (diverso da)

numero_segreto = 7
tentativo = 5

if tentativo != numero_segreto:
    print("Il numero tentato è diverso dal numero segreto.")
    
# --- CICLO FOR con range() ---

print("Inizio del conto alla rovescia:")
# range(5) genera i numeri da 0 a 4 (5 numeri in totale)
# range(start, stop) genera numeri da 'start' fino a 'stop-1'
# range(start, stop, step) genera numeri da 'start' fino a 'stop-1', con un certo 'passo'

for numero in range(5, 0, -1):  # Conta da 5 giù fino a 1 (5, 4, 3, 2, 1)
    # Ad ogni ripetizione (chiamata 'iterazione'), la variabile 'numero'
    # assume il valore successivo nella sequenza generata da range()
    print(numero)
    # Tutto ciò che è indentato qui sotto fa parte del ciclo for
    # e verrà ripetuto.

print("... Lancio!") # Questa riga è fuori dal ciclo, quindi viene eseguita solo una volta alla fine.


# --- CICLO FOR per iterare su una STRINGA ---
# Una stringa è una sequenza di caratteri!

parola = "Python"
print("\nCaratteri nella parola '" + parola + "':")
for lettera in parola:
    # Ad ogni iterazione, 'lettera' conterrà un carattere della stringa 'parola'
    print(lettera)


# --- CICLO FOR per iterare su una LISTA ---
# Le liste sono collezioni ordinate di elementi. Le vedremo meglio più avanti,
# ma ecco un'anticipazione per vedere come funziona il for.
# Una lista si crea con le parentesi quadre [].

colori = ["rosso", "verde", "blu", "giallo"]
print("\nI miei colori preferiti sono:")
for colore_corrente in colori:
    print(colore_corrente)

# --------------------------------------    
# 3) Organizzare il codice: Le Funzioni.
# --------------------------------------

# Definiamo una funzione che saluta l'utente
def saluta():
    print("Ciao! Questa è una funzione.")

# Per usare la funzione, basta chiamarla:
saluta()

# Possiamo passare informazioni (parametri) a una funzione
def saluta_utente(nome):
    print("Ciao,", nome + "!")

saluta_utente("Luca")  # Output: Ciao, Luca!

# Una funzione può anche restituire un valore con return
def somma(a, b):
    risultato = a + b
    return risultato

# Possiamo salvare o stampare il risultato
valore = somma(3, 5)
print("La somma è:", valore)  # Output: 8

# Le variabili definite dentro una funzione esistono solo all'interno della funzione (scope locale)
def esempio():
    messaggio = "Ciao dal mondo interno!"
    print(messaggio)

esempio()
# print(messaggio)  # Questo darebbe errore: messaggio non è definito fuori dalla funzione

# --------------------------------------
# EXTRA: Lettura di file in Python 📂
# --------------------------------------
# Python fornisce strumenti per leggere molti tipi di file strutturati.
# Ecco un elenco dei più comuni con le librerie e i metodi consigliati:

# 📄 FILE DI TESTO (.txt)
#   - Metodo: open()
#   - Esempio:
#     with open("file.txt", "r") as f:
#         contenuto = f.read()

# 📊 FILE CSV (.csv)
#   - Libreria: pandas
#   - Esempio:
#     import pandas as pd
#     df = pd.read_csv("file.csv")

# 🧾 FILE JSON (.json)
#   - Libreria: json oppure pandas
#   - Esempio:
#     import json
#     with open("file.json") as f:
#         dati = json.load(f)
#   - Alternativa con pandas:
#     df = pd.read_json("file.json")

# 🗂️ FILE XML (.xml)
#   - Libreria: xml.etree.ElementTree o lxml
#   - Esempio:
#     import xml.etree.ElementTree as ET
#     tree = ET.parse("file.xml")
#     root = tree.getroot()

# 📈 FILE EXCEL (.xlsx)
#   - Libreria: pandas
#   - Esempio:
#     df = pd.read_excel("file.xlsx")

# 🧱 FILE PARQUET (.parquet)
#   - Libreria: pandas
#   - Esempio:
#     df = pd.read_parquet("file.parquet")

# 🛢️ FILE SQL / DATABASE
#   - Libreria: pandas + sqlite3 o SQLAlchemy
#   - Esempio con SQLite:
#     import sqlite3
#     conn = sqlite3.connect("database.sqlite")
#     df = pd.read_sql("SELECT * FROM tabella", conn)

#   - Altri database supportati:
#     PostgreSQL -> libreria: psycopg2
#     MySQL      -> libreria: mysql-connector-python
#     MS SQL     -> libreria: pyodbc

# ⚙️ FILE YAML (.yaml / .yml)
#   - Libreria: PyYAML
#   - Esempio:
#     import yaml
#     with open("file.yaml") as f:
#         configurazione = yaml.safe_load(f)

# 🧩 FILE INI (.ini)
#   - Libreria: configparser
#   - Esempio:
#     import configparser
#     config = configparser.ConfigParser()
#     config.read("config.ini")
#     valore = config["SEZIONE"]["chiave"]

# 📌 Suggerimento:
#   Per ogni formato, verifica sempre l’esistenza del file
#   e gestisci eventuali eccezioni con try/except!
