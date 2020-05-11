import RPi.GPIO as GPIO
import time

''' trida umoznuje otacet panel ve vsech smerech pomoci spinani prislusnych ctyrech rele  '''

class Relays:
    
    #inicializace
    def __init__(self,left=5,right=19,up=13,down=6):
        self.left=left
        self.right=right
        self.up=up
        self.down=down
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.right,GPIO.OUT)
        GPIO.setup(self.left,GPIO.OUT)
        GPIO.setup(self.up,GPIO.OUT)
        GPIO.setup(self.down,GPIO.OUT)

    #pohyby do vsech smeru (spinani rele)
    def go_left(self):
        GPIO.output(self.left,False)
                
    def go_right(self):
        GPIO.output(self.right,False)
                
    def go_up(self):
        GPIO.output(self.up,False)
            
    def go_down(self):
        GPIO.output(self.down,False)
            
    #zastaveni pohybu (vypnuti rele)
    def stop_left(self):
        GPIO.output(self.left,True)
                
    def stop_right(self):
           GPIO.output(self.right,True)
                      
    def stop_up(self):
           GPIO.output(self.up,True)
               
    def stop_down(self):
           GPIO.output(self.down,True)
                      
    def stop_all(self):
        GPIO.output(self.left,True)
        GPIO.output(self.right,True)
        GPIO.output(self.up,True)
        GPIO.output(self.down,True)
            
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
    
          

