import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    global __data_columns, __model
    
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    
    if loc_index >= 0:
        x[loc_index] = 1  # Set location feature to 1 instead of -1
    
    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts..start")
    global __data_columns
    global __locations
    global __model 
    with open('C:\\Users\\Aayushaghera\\Desktop\\BHP\\server\\artifacts\\columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    with open('C:\\Users\\Aayushaghera\\Desktop\\BHP\\server\\artifacts\\banglore_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print("loading the artifacts is done..")

if __name__ == "__main__":
    load_saved_artifacts()
    