from machine import I2C, Pin
import time

# Inizializza I2C sull'ESP32
i2c = I2C(scl=Pin(18), sda=Pin(19), freq=100000)

# Scansiona i dispositivi I2C collegati
devices = i2c.scan()
print("Dispositivi I2C trovati:", [hex(device) for device in devices])

if 0x5A not in devices:
    print("Sensore GY-906 non trovato sul bus I2C.")
else:
    print("Sensore GY-906 trovato all'indirizzo 0x5A.")

# Funzione per leggere la temperatura dal registro specificato
def read_temp(reg):
    data = i2c.readfrom_mem(0x5A, reg, 3)
    temp = data[0] + (data[1] << 8)
    temp = temp * 0.02 - 273.15
    return temp

while True:
    # Legge la temperatura ambiente e dell'oggetto
    temp_ambiente = read_temp(0x06)
    temp_oggetto = read_temp(0x07)
    
    # Stampa i valori sul Serial Monitor
    print("Temperatura Ambiente: {:.2f} °C, Temperatura Oggetto: {:.2f} °C".format(temp_ambiente, temp_oggetto))
    
    # Per il Serial Plotter, stampa solo i valori separati da una virgola
    print("{:.2f},{:.2f}".format(temp_ambiente, temp_oggetto))
    
    time.sleep(1)
