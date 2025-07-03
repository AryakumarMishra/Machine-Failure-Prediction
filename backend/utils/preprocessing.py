import pandas as pd

def preprocess_input(data_dict, background_cols):
    air_temp = data_dict['air_temp']
    process_temp = data_dict['process_temp']
    speed = data_dict['speed']
    torque = data_dict['torque']
    tool_wear = data_dict['tool_wear']
    quality = data_dict['product_quality']

    _L, _M, _H = 0, 0, 0
    if quality == 'L':
        _L = 1
    elif quality == 'M':
        _M = 1
    else:
        _H = 1

    temp_diff = process_temp - air_temp
    power = torque * speed
    torque_per_wear = torque / (tool_wear + 1)

    return pd.DataFrame([[ 
        air_temp, process_temp, speed, torque, tool_wear,
        _H, _L, _M, temp_diff, power, torque_per_wear
    ]], columns=background_cols)
