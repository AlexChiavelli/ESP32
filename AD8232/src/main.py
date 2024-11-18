from machine import ADC, Pin
import time

# Inizializza l'ADC sul GPIO36
ecg_pin = ADC(Pin(36))
ecg_pin.atten(ADC.ATTN_11DB)  # Imposta l'attenuazione per leggere fino a 3.6V

# Inizializza i pin digitali per LO+ e LO-
lo_plus = Pin(32, Pin.IN)
lo_minus = Pin(33, Pin.IN)

while True:
    ecg_value = ecg_pin.read()  # Legge il valore analogico
    lo_plus_state = lo_plus.value()
    lo_minus_state = lo_minus.value()
    
    # Controlla se gli elettrodi sono scollegati
    if lo_plus_state == 1 or lo_minus_state == 1:
        print(0)  # Se gli elettrodi sono scollegati, stampa 0
    else:
        print(ecg_value)  # Stampa il valore ECG letto
    
    time.sleep_ms(5)  # Regola il tasso di campionamento a 200Hz
