import pandas as pd

def main():
    global fire,temperature, day
    df = pd.read_csv('control_fire_risk_data.csv')
    fire_score = 0
    for i in range(31): 
        temp = float(df.loc[i,'temp_avg'])
        if temp < 0:
            temp_score = 0
        elif temp < 15:
            temp_score = temp * 0.5
        elif temp < 25:
            base = (temp - 15) / 10 
            temp_score = 7.5 + (base ** 1.5) * 22.5
        else:
            temp_score = 30 + min((temp - 25) * 3, 30) 

        light = float(df.loc[i,'light_avg_lux'])
        room_light = min((light/100000), 1.0)

        if light < 100:
            light_score = 0
        elif light < 1000: 
            light_score = room_light * 10
        elif light < 10000:
            light_score = 10 + (room_light * 20)
        else:
            light_score = 30 + min((room_light - 10000) / 1000, 10)

        synergy = 0
        if temp_score > 20 and light_score > 20:
            synergy = (temp_score * light_score) / 100
        
        fire_score = temp_score + light_score + synergy
        print(f"Day : {i} fire score: {fire_score}")
        i += 1
main()