import RPi.GPIO as GPIO
import time

ZMĚNA
''' trida umoznuje otacet panel ve vsech smerech pomoci spinani prislusnych ctyrech rele  '''

class Relays:
    
    #inicializace
    def __init__(self,left=5,right=19,up=13,down=6):
        self.left=left
        self.right=right
        self.up=up
        self.down=down
        #print("konstruktor")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.right,GPIO.OUT)
        GPIO.setup(self.left,GPIO.OUT)
        GPIO.setup(self.up,GPIO.OUT)
        GPIO.setup(self.down,GPIO.OUT)

    #pohyby do vsech smeru (spinani rele)
    def go_left(self):
        GPIO.output(self.left,False)
        #print("go_left")
        
    def go_right(self):
        GPIO.output(self.right,False)
        #print("go_right")
        
    def go_up(self):
        GPIO.output(self.up,False)
        #print("go_up")
    
    def go_down(self):
        GPIO.output(self.down,False)
        #print("go_down")
    
    #zastaveni pohybu (vypnuti rele)
    def stop_left(self):
        GPIO.output(self.left,True)
        #print("stop_left")
        
    def stop_right(self):
           GPIO.output(self.right,True)
           #print("stop_right")
           
    def stop_up(self):
           GPIO.output(self.up,True)
           #print("stop_up")
    
    def stop_down(self):
           GPIO.output(self.down,True)
           #print("stop_down")
           
    def stop_all(self):
        GPIO.output(self.left,True)
        GPIO.output(self.right,True)
        GPIO.output(self.up,True)
        GPIO.output(self.down,True)
        #print("stop_all")
    
    #pohyb do vsech smeru o urcity usek
    def go_left_by(self,degrees):
        GPIO.output(self.left,False)
        time.sleep(degrees)
        GPIO.output(self.left,True)
        time.sleep(0.1)
    
    def go_right_by(self,degrees):
        GPIO.output(self.right,False)
        time.sleep(degrees)
        GPIO.output(self.right,True)
        time.sleep(0.1)
    
    def go_up_by(self,degrees):
        GPIO.output(self.up,False)
        time.sleep(degrees)
        GPIO.output(self.up,True)
        time.sleep(0.1)
    
    def go_down_by(self,degrees):
        GPIO.output(self.down,False)
        time.sleep(degrees)
        GPIO.output(self.down,True)
        time.sleep(0.1)
        
    
    
        


