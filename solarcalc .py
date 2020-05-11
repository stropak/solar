import datetime
from datetime import timedelta 
import math

''' trida umoznuje vypocitat v jake poloze se aktualne nachazi slunce   '''

class SolarCalc:
    
    #konstanty
    ECCENT_EARTH_ORBIT =0.0167  #Eccent earth erbit
    OBLIQ_CORR=23.435 #Obliq corr
    VAR_Y=0.043 #var Y


    def get_elevation(self):

        #zemepisne udaje
        latitude = 48.77 #Latitude-zemepisna sirka
        longtitude = 14.98 #Longtitude-zemepisna delka
        time_zone = +1 #Time Zone-casove pasmo

        #casove udaje
        date = datetime.datetime.now() #Date-aktuálni datum
        local_datetime=date+timedelta(hours=1)
        midnight = datetime.datetime.combine(date.date(), datetime.time())#Local midnight-pulnoc
        minutes=((local_datetime - midnight).seconds)/60 #Minutes after midnigh- minuty od půlnoci

        julian_day= 367 * date.year - int((7 * (date.year + int((date.month + 9) / 12.0))) / 4.0) + int((275 * date.month) / 9.0) + date.day + 1721013.5 + (date.hour + date.minute / 60.0 + date.second / math.pow(60, 2)) / 24.0 - 0.5 * math.copysign(1, 100 * date.year + date.month - 190002.5) + 0.5# Julian day-julianske datum
        julian_century= (julian_day-2451545)/36525 #Julian century- Juliánské století

        #vypocty
        geom_mean_long_sun = (280.46646 + julian_century * (36000.76983 + julian_century * 0.0003032)) % 360#Geom mean long Sun (deg)
        geom_mean_anom_sun = 357.52911 + julian_century * (35999.05029 - 0.0001537 * julian_century) #Geom mean anom Sun (deg)
        sun_eq_of_ctr = math.sin(math.radians(geom_mean_anom_sun)) * (1.914602 - julian_century * (0.004817 + 0.000014 * julian_century)) + math.sin(math.radians(2 * geom_mean_anom_sun)) * (0.019993 - 0.000101 * julian_century) + math.sin(math.radians(3 * geom_mean_anom_sun)) * 0.000289 #Sun Eq of Ctr
        sun_true_long = geom_mean_long_sun + sun_eq_of_ctr #Sun true long (deg)
        sun_app_long=sun_true_long-0.00569-0.00478*math.sin(math.radians(125.04-1934.136*julian_century)) #Sun app long (deg)
        sun_declin= math.degrees(math.asin(math.sin(math.radians(SolarCalc.OBLIQ_CORR))*math.sin(math.radians(sun_app_long)))) #Sun declin
        eq_of_time=4*math.degrees(SolarCalc.VAR_Y*math.sin(2*math.radians(geom_mean_long_sun))-2*SolarCalc.ECCENT_EARTH_ORBIT*math.sin(math.radians(geom_mean_anom_sun))+4*SolarCalc.ECCENT_EARTH_ORBIT*SolarCalc.VAR_Y*math.sin(math.radians(geom_mean_anom_sun))*math.cos(2*math.radians(geom_mean_long_sun)-0.5*SolarCalc.VAR_Y*SolarCalc.VAR_Y*math.sin(4*math.radians(geom_mean_long_sun))-1.25*SolarCalc.ECCENT_EARTH_ORBIT*SolarCalc.ECCENT_EARTH_ORBIT*math.sin(2*math.radians(geom_mean_anom_sun)))) #Eq of Time

        true_solar_time=(minutes+eq_of_time+4*longtitude-60*time_zone)%1440 #True solar time
        if ((true_solar_time/4)<0):
                hour_angle=(true_solar_time/4+180)
        else:
                hour_angle=(true_solar_time/4-180) #Hour angle
        solar_zenith_angle=math.degrees(math.acos(math.sin(math.radians(latitude))*math.sin(math.radians(sun_declin))+math.cos(math.radians(latitude))*math.cos(math.radians(sun_declin))*math.cos(math.radians(hour_angle)))) #solar zenith angle

        #vysledna ELEVACE
        elevation=90-solar_zenith_angle 
          
        print("Elevace: ",elevation)
        return elevation



    def get_azimuth(self):
        
        #zemepisne udaje
        latitude = 48.77 #Latitude-zemepisna sirka
        longtitude = 14.98 #Longtitude-zemepisna delka
        time_zone = +1 #Time Zone-casove pasmo

        #casove udaje
        date = datetime.datetime.now() #Date-aktuálni datum
        local_datetime=date+timedelta(hours=1)
        midnight = datetime.datetime.combine(date.date(), datetime.time())#Local midnight-pulnoc
        minutes=((local_datetime - midnight).seconds)/60 #Minutes after midnigh- minuty od půlnoci

        julian_day= 367 * date.year - int((7 * (date.year + int((date.month + 9) / 12.0))) / 4.0) + int((275 * date.month) / 9.0) + date.day + 1721013.5 + (date.hour + date.minute / 60.0 + date.second / math.pow(60, 2)) / 24.0 - 0.5 * math.copysign(1, 100 * date.year + date.month - 190002.5) + 0.5# Julian day-julianske datum
        julian_century= (julian_day-2451545)/36525 #Julian century- Juliánské století

        #vypocty
        geom_mean_long_sun = (280.46646 + julian_century * (36000.76983 + julian_century * 0.0003032)) % 360#Geom mean long Sun (deg)
        geom_mean_anom_sun = 357.52911 + julian_century * (35999.05029 - 0.0001537 * julian_century) #Geom mean anom Sun (deg)
        sun_eq_of_ctr = math.sin(math.radians(geom_mean_anom_sun)) * (1.914602 - julian_century * (0.004817 + 0.000014 * julian_century)) + math.sin(math.radians(2 * geom_mean_anom_sun)) * (0.019993 - 0.000101 * julian_century) + math.sin(math.radians(3 * geom_mean_anom_sun)) * 0.000289 #Sun Eq of Ctr
        sun_true_long = geom_mean_long_sun + sun_eq_of_ctr #Sun true long (deg)
        sun_app_long=sun_true_long-0.00569-0.00478*math.sin(math.radians(125.04-1934.136*julian_century)) #Sun app long (deg)
        sun_declin= math.degrees(math.asin(math.sin(math.radians(SolarCalc.OBLIQ_CORR))*math.sin(math.radians(sun_app_long)))) #Sun declin
        eq_of_time=4*math.degrees(SolarCalc.VAR_Y*math.sin(2*math.radians(geom_mean_long_sun))-2*SolarCalc.ECCENT_EARTH_ORBIT*math.sin(math.radians(geom_mean_anom_sun))+4*SolarCalc.ECCENT_EARTH_ORBIT*SolarCalc.VAR_Y*math.sin(math.radians(geom_mean_anom_sun))*math.cos(2*math.radians(geom_mean_long_sun)-0.5*SolarCalc.VAR_Y*SolarCalc.VAR_Y*math.sin(4*math.radians(geom_mean_long_sun))-1.25*SolarCalc.ECCENT_EARTH_ORBIT*SolarCalc.ECCENT_EARTH_ORBIT*math.sin(2*math.radians(geom_mean_anom_sun)))) #Eq of Time

        true_solar_time=(minutes+eq_of_time+4*longtitude-60*time_zone)%1440 #True solar time
        if ((true_solar_time/4)<0):
                hour_angle=(true_solar_time/4+180)
        else:
                hour_angle=(true_solar_time/4-180) #Hour angle
        solar_zenith_angle=math.degrees(math.acos(math.sin(math.radians(latitude))*math.sin(math.radians(sun_declin))+math.cos(math.radians(latitude))*math.cos(math.radians(sun_declin))*math.cos(math.radians(hour_angle)))) #solar zenith angle

        #vysledny AZIMUTH
        if (hour_angle>0):
                azimuth=(math.degrees(math.acos(((math.sin(math.radians(latitude))*math.cos(math.radians(solar_zenith_angle)))-math.sin(math.radians(sun_declin)))/(math.cos(math.radians(latitude))*math.sin(math.radians(solar_zenith_angle)))))+180) %360
        else:
                azimuth=(540-math.degrees(math.acos(((math.sin(math.radians(latitude))*math.cos(math.radians(solar_zenith_angle)))-math.sin(math.radians(sun_declin)))/(math.cos(math.radians(latitude))*math.sin(math.radians(solar_zenith_angle))))))%360
    
        print("Azimut: ",azimuth)
        return azimuth
