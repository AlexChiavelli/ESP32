import machine
import time

# Configura l'ADC sul pin GPIO34
adc_pin = machine.ADC(machine.Pin(34))
adc_pin.atten(machine.ADC.ATTN_11DB)    # Imposta l'attenuazione a 11dB (per leggere fino a 3.3V)
adc_pin.width(machine.ADC.WIDTH_12BIT)  # Imposta la risoluzione a 12 bit

while True:
    adc_value = adc_pin.read()  # Legge il valore analogico
    print(adc_value)            # Stampa il valore sul monitor seriale
    time.sleep(0.1)             # Attende 100 millisecondi prima della prossima lettura
