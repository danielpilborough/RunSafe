import requests, json
from config import latitude, longitude # type: ignore
res = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,uv_index,rain,precipitation_probability,cloud_cover&forecast_days=1')

data = res.json()



times = data['hourly']['time']
temperature = data['hourly']['temperature_2m']
uv_index = data['hourly']['uv_index']

best_run_times = []


def main():
    max_temp_input = float(input("Please enter your max temp: "))
    find_best_time_to_run(max_temp_input)


def find_best_time_to_run(max_temp):
    for i in range(6, len(times)-2):
        current_temp = temperature[i]
        previous_temp = temperature[i - 1]
        current_uv = uv_index[i]

        if current_uv < 3 and current_temp < previous_temp and current_temp < max_temp:
            best_run_times.append({
                'time': times[i],
                'temp': current_temp,
                'uv': current_uv
            })        

    if best_run_times:
        for entry in best_run_times:
            print(f'{entry["time"]} -- Temp: {entry["temp"]} -- UV: {entry["uv"]}')
    else:
        print("No ideal running times found based on UV and Temperature")







main()