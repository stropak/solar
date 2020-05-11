cdimport time
import solarcalc
import relays
import calibration
import wind

#minimalni posun
THRESHOLD=5

#instance ostanich trid
solar_calc=solarcalc.SolarCalc()
relays = relays.Relays()
calibration = calibration.Calibration()
wind=wind.Wind()

#kalibrace
print("calibrace azimutu")
one_degree_right=calibration.azimuth()
print("calibrace elevace")
one_degree_up=calibration.elevation()
    
print("stupen do prava ", one_degree_right)
print("stupen nahoru ", one_degree_up)

#hlavni cyklus
while True:
    
    #hlidani vetru
    while True:
        is_strong_wind=wind.is_wind()
        if (is_strong_wind==False):
            break
        else:
            print("sklopeni kvuli vetru")
            calibration.go_to_up_home()
            print("cekam kvuli vetru")
            
    #pocatecni nastaveni
    print("nastaveni do leve vychozi polohy")
    calibration.go_to_left_home()
    actual_azimuth=45

    print("nastaveni do dolni vyhcozi polohy")
    calibration.go_to_down_home()
    actual_elevation=0

    #denni cyklus
    while True:

        #hlidani vetru
        while True:
            is_strong_wind=wind.is_wind()
            if (is_strong_wind==False):
                break
            else:
                print("sklopeni kvuli vetru")
                calibration.go_to_up_home()
                actual_elevation=90
                print("cekam kvuli vetru")
                

        print("dalsi kolo")
        
        #vypocet pozadovanych uhlu
        required_azimuth=solar_calc.get_azimuth()
        required_elevation=solar_calc.get_elevation()
        if (required_elevation<0):
            break
        
        #vypoct o kolik je treba se posunout
        azimuth_shift=required_azimuth-actual_azimuth
        elevation_shift=required_elevation-actual_elevation
        
        #posunuti doprava (azumit)
        if (abs(azimuth_shift)>THRESHOLD):
            azimuth_shift_to_time=azimuth_shift*one_degree_right
            print("go_right_by ",azimuth_shift)
            print("in time= ",azimuth_shift_to_time)
            relays.go_right_by(azimuth_shift_to_time)
            actual_azimuth=required_azimuth
        
        #posunuti nahoru/dolu (elevace)
        if (abs(elevation_shift)>THRESHOLD):
        
            if(elevation_shift>0):
                elevation_shift_to_time=elevation_shift*one_degree_up
                print("go_up_by",elevation_shift)
                print("in time= ",elevation_shift_to_time)
                relays.go_up_by(elevation_shift_to_time)
                actual_elevation=required_elevation
            else:
                elevation_shift_to_time=-elevation_shift*one_degree_up
                print("go_down_by",elevation_shift)
                print("in time= ",elevation_shift_to_time)
                relays.go_down_by(elevation_shift_to_time)
                actual_elevation=required_elevation

        time.sleep(3)

    #sklopeni panelu na vecer
    print("sklopeni na vecer")
    calibration.go_to_up_home()
    
    #nocni cyklus
    while True:
        print("nocni cyklus dalsi kolo")

        required_elevation=solar_calc.get_elevation()
        if (required_elevation>0):
            break
        time.sleep(5)

    
