import RPi.GPIO as GPIO
import time
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#nastaveni vystupu
GPIO.setup(21,GPIO.IN,GPIO.PUD_UP)

'''trida umoznuje rozpoznat zda fouka prilis silny vitr'''

class Wind:
    
    #pocet otacek anemometru ktery nesmi byt prekrocen
    THRESHOLD=10
    #doba mereni
    MEASURING_TIME=10
    
    #vrati true/false podle toho zda je prekrocen pocet otacek za dany casovy usek
    def is_wind(self):
        impulse = int(0)
        recorded=0
        timeout=time.time()+Wind.MEASURING_TIME
        strong_wind=False
        
        print("hlidam vitr")
        
        while(time.time()<timeout):
        
            if(GPIO.input(21) == False):
                if(recorded == 0):
                    impulse = impulse + 1
                    print("wind ",impulse)
                    recorded = 1
            else:
                recorded=0
                
        if (impulse>Wind.THRESHOLD):
            strong_wind=True
        else:
            strong_wind=False
            
        return strong_wind

