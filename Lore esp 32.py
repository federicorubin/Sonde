import serial
import time

# Configurazione della porta seriale (ad esempio, COM3 su Windows o /dev/ttyUSB0 su Linux)
# Assicurarsi che la porta seriale sia corretta e che i parametri di comunicazione (baud rate, parity, etc.)
# corrispondano a quelli configurati sul trasmettitore LoRa Ebyte E32
PORTA_SERIALE = 'COM3'  # Sostituire con la porta seriale corretta
BAUD_RATE = 9600
# ... altre impostazioni seriali (parity, stopbits, etc.) ...

# Nome del file in cui salvare l'immagine decodificata
NOME_FILE_IMMAGINE = "immagine_ricevuta.png"

try:
    # Apri la connessione seriale
    ser = serial.Serial(PORTA_SERIALE, BAUD_RATE, timeout=1)
    time.sleep(2)  # Attendi che la connessione seriale si stabilizzi

    print(f"Connesso alla porta seriale {PORTA_SERIALE}")

    # Array per memorizzare i dati grezzi dell'immagine ricevuti
    dati_immagine = bytearray()
    dimensione_immagine_prevista = 640 * 320 # Esempio: 1MB. Modificare in base alla dimensione effettiva dell'immagine

    print("Inizio ricezione dati immagine...")
    while True:
        # Leggi i dati dalla porta seriale
        dati_ricevuti = ser.read(640) # Leggi un blocco di dati alla volta
        if dati_ricevuti:
            dati_immagine.extend(dati_ricevuti)
            print(f"Ricevuti {len(dati_ricevuti)} byte...")
            
            # Inserisci qui la logica per decidere quando terminare la ricezione,
            # ad esempio:
            # 1. Se la dimensione prevista è raggiunta:
            #    if len(dati_immagine) >= dimensione_immagine_prevista:
            #        break
            # 2. Se il trasmettitore invia un segnale di fine trasmissione (es. un byte speciale)

            # In questo esempio, attendiamo semplicemente un po' prima di inviare una nuova lettura,
            # ma è consigliabile implementare una gestione più robusta per terminare la ricezione.

    print("Ricezione dati completata.")

    # Salva i dati ricevuti in un file immagine
    with open(NOME_FILE_IMMAGINE, 'wb') as f:
        f.write(dati_immagine)

    print(f"Immagine salvata come {NOME_FILE_IMMAGINE}")

except serial.SerialException as e:
    print(f"Errore seriale: {e}")
except Exception as e:
    print(f"Si è verificato un errore: {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Porta seriale chiusa.")