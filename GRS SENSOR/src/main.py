import machine
import time

# Configura il pin GPIO25 come ingresso ADC
adc = machine.ADC(machine.Pin(25))
adc.atten(machine.ADC.ATTN_11DB)  # Imposta l'attenuazione a 11dB per leggere fino a 3.3V
adc.width(machine.ADC.WIDTH_12BIT)  # Imposta la risoluzione a 12 bit (valori da 0 a 4095)

while True:
    valore = adc.read()  # Legge il valore analogico dal sensore
    print(valore)  # Stampa il valore sul Serial Monitor e Plotter
    time.sleep(0.1)  # Attende 100 millisecondi prima della prossima lettura
