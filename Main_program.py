#Importing pandas for csv reading
import pandas as pd

def main():
    global fire,temperature, day
    
    #Creating a data frame to read data from csv file
    df = pd.read_csv('control_fire_risk_data.csv')
    
    #The fire risk is calculated as fire_score
    fire_score = 0
    
    for i in range(31):
        #Temperature value declared as temp
        temp = float(df.loc[i,'temp_avg'])
        
        #Temperature score is calculated via algorithm as temp_score
        if temp < 0: # 0 degrees celsius is the temperature at which water freezes into ice
            temp_score = 0
        elif temp < 15: # Under 15 degrees celsius is the usual temperature in ireland in winter
            temp_score = temp * 0.5
        elif temp < 25: # u=Under 25 degrees celsius is the usual temperature in Ireland in summer
            base = (temp - 15) / 10 
            temp_score = 7.5 + (base ** 1.5) * 22.5
        else: # Higher then 25 is considered a heat wave in Ireland
            temp_score = 30 + min((temp - 25) * 3, 30) 

        #Light value declared as light
        light = float(df.loc[i,'light_avg_lux'])
        #Room light declared (due to the fact that direct sunlight is 100k lux
        room_light = min((light/100000), 1.0)

        #Light score is calculated via algorithm as light_score
        if light < 100: # 100 Lux and lower is considered a dark room
            light_score = 0
        elif light < 1000: # 100 Lux and below is the usual office light and/or an overcast day
            light_score = room_light * 10
        elif light < 10000:# 10k Lux and below is considered a sunny day (when sun is not direct)
            light_score = 10 + (room_light * 20)
        else:# Direct sunlight
            light_score = 30 + min((room_light - 10000) / 1000, 10)

        #Synergy is calculated (due to the fact that at a high enough lux and celsius, the effects become multiplicative)
        synergy = 0
        if temp_score > 20 and light_score > 20:
            synergy = (temp_score * light_score) / 100
        
        #Fire score is displayed according to day
        fire_score = temp_score + light_score + synergy
        print(f"Day : {i} fire score: {fire_score}")
        
        #The cycle repeats
        i += 1
main()