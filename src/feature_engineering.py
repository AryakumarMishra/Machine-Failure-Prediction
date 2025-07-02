import pandas as pd

def encode_and_engineer(data):
    # One-hot encoding
    data_encoded = pd.get_dummies(data, columns=['Type'], prefix="", dtype='int')

    # Drop irrelevant columns
    new_data = data_encoded.drop(['Product ID', 'UDI', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF'], axis=1)

    # Feature Engineering
    new_data['temp_diff'] = new_data['Process temperature [K]'] - new_data['Air temperature [K]']
    new_data['power'] = new_data['Torque [Nm]'] * new_data['Rotational speed [rpm]']
    new_data['torque_per_wear'] = new_data['Torque [Nm]'] / (new_data['Tool wear [min]'] + 1)

    return new_data