import serial
import serial.tools.list_ports

# 1. Trova la porta seriale (se non la conosci)
# `serial.tools.list_ports.comports()` restituisce una lista di porte disponibili
ports = serial.tools.list_ports.comports()
print("Porte seriali disponibili:")
for port in ports:
    print(f"- {port.device} ({port.description})")

# 2. Sostituisci 'COM3' con la porta seriale corretta del tuo Ebyte E32
# Potrebbe essere `/dev/ttyUSB0` o simile su Linux/macOS
# Sostituisci '9600' con il baud rate corretto (es. 9600, 115200)
port_seriale = 'COM3'
baud_rate = 9600

try:
    # 3. Apri la connessione seriale
    # `timeout` imposta il tempo massimo di attesa per la lettura
    ser = serial.Serial(port_seriale, baud_rate, timeout=1)
    print(f"Connessione aperta su {port_seriale} a {baud_rate} baud")

    while True:
        # 4. Leggi i dati dalla porta seriale
        # `ser.readline()` legge una riga fino al carattere di nuova linea('\n')
        # Restituisce byte, quindi usa .decode() per convertirli in stringa
        if ser.in_waiting > 0:
            linea_byte = ser.readline()
            try:
                linea_stringa = linea_byte.decode('utf-8').strip()
                print(f"Dato ricevuto: {linea_stringa}")

                # 5. Decodifica i dati (es. se sono stringhe, numeri o altri formati)
                # Esempio: se i dati sono `{"temperatura": 25.5, "umidita": 60}`
                # json.loads(linea_stringa)
                
                # Esempio: se i dati sono solo un numero intero
                # valore_numerico = int(linea_stringa)

            except UnicodeDecodeError:
                print(f"Errore di decodifica: {linea_byte}")
            except Exception as e:
                print(f"Errore durante l'elaborazione: {e}")

except serial.SerialException as e:
    print(f"Errore nella porta seriale: {e}")
except Exception as e:
    print(f"Si è verificato un errore: {e}")

finally:
    # 6. Chiudi la connessione seriale quando termini
    if 'ser' in locals() and ser.isOpen():
        ser.close()
        print("Porta seriale chiusa.")
