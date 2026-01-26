import pandas as pd

#Divide the csv into lists (1 day each) and then use those valuesi n the list to calculate fire score
def file():
    global fire, temp, fire_score
    fire = []
    temp = []
    fire_score = []
    df = pd.read_csv('control_fire_risk_data.csv')
    print(df.loc[0])

file()

def main():
    global fire, temp, fire_score

    temp = input.temperature()
    if temp < 0:
        temp_score = 0
    elif temp < 15:
        temp_score = temp * 0.5
    elif temp < 25:
        base = (temp - 15) / 10 
        temp_score = 7.5 + (base ** 1.5) * 22.5
    else:
        temp_score = 30 + min((temp - 25) * 3, 30) 

    fire = 0
    room_light = min((fire/100000), 1.0)

    if fire < 100:
        light_score = 0
    elif fire < 1000: 
        light_score = room_light * 10
    elif fire < 10000:
        light_score = 10 + (room_light * 20)
    else:
        light_score = 30 + min((room_light - 10000) / 1000, 10)

    synergy = 0
    if temp_score > 20 and light_score > 20:
        synergy = (temp_score * light_score) / 100
    
    fire_score = temp_score + light_score + synergy
    