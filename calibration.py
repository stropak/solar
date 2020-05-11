import RPi.GPIO as GPIO
import time
import relays

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#nastaveni vstupu pro koncove spinace
GPIO.setup(17,GPIO.IN,GPIO.PUD_UP) #down
GPIO.setup(22,GPIO.IN,GPIO.PUD_UP) #up
GPIO.setup(23,GPIO.IN,GPIO.PUD_UP) #left
GPIO.setup(24,GPIO.IN,GPIO.PUD_UP) #right


'''trida umoznuje zjistit kolik casu trva ujet stupen do prava, nahoru a nastavit panel do vychozi polohy'''

class Calibration:
        
    relays = relays.Relays()
    
    #zjisteni jak dlouho trva ujet jeden stupen nahoru/dolu
    def elevation(self):

        repeat=True
        repeat2=False

        while (repeat):
            
            Calibration.relays.go_up()
            if (GPIO.input(22)==False):
                print("sepnuty horni koncovy spinac")
                Calibration.relays.stop_up()
                time.sleep(1)
                begin=time.time()
                repeat=False
                repeat2=True

        while (repeat2):
            
            Calibration.relays.go_down()
            if (GPIO.input(17)==False):
                print("sepnuty dolni koncovy spinac")
                Calibration.relays.stop_down()
                end=time.time()
                repeat2=False

        measured_time=end-begin
        one_degree=measured_time/90

        return one_degree
        
        
    #zjisteni jak dlouho trva ujet jeden stupen do prava/doleva
    def azimuth(self):

        repeat=True
        repeat2=False

        while (repeat):
            
            Calibration.relays.go_left()
            if (GPIO.input(23)==False):
                print("sepnuty levy koncovy spinac")
                Calibration.relays.stop_left()
                time.sleep(1)
                begin=time.time()
                repeat=False
                repeat2=True

        while (repeat2):
            
            Calibration.relays.go_right()
            if (GPIO.input(24)==False):
                print("sepnuty pravy koncovy spinac")
                Calibration.relays.stop_right()
                end=time.time()
                repeat2=False

        measured_time=end-begin
        one_degree=measured_time/270

        return one_degree
     
    #nastaveni do leve vychozi polohy
    def go_to_left_home(self):
        
        while (True):
            Calibration.relays.go_left()
            if (GPIO.input(23)==False):
                Calibration.relays.stop_left()
                print("left home")
                break
                
    #nastaveni do prave vychozi polohy
    def go_to_right_home(self):
        
        while (True):
            Calibration.relays.go_right()
            if (GPIO.input(24)==False):
                Calibration.relays.stop_right()
                print("right home")
                break
    
    #nastaveni do dolni vychozi polohy
    def go_to_down_home(self):
                       
        while (True):
            Calibration.relays.go_down()
            if (GPIO.input(17)==False):
                Calibration.relays.stop_down()
                print("down home")
                break
            
    #nastaveni do horni vychozi polohy
    def go_to_up_home(self):
                       
        while (True):
            Calibration.relays.go_up()
            if (GPIO.input(22)==False):
                Calibration.relays.stop_up()
                print("up home")
                break



