import config
import pickle
import json
import numpy as np

class SpeciesClass:
    
    def __init__(self,input_data):
        self.input_data = input_data


    def load_data(self):
        with open(config.model_path,"rb") as f:
            self.model = pickle.load(f)
        with open(config.project_data_path,"r") as f:
            self.project_data = json.load(f)

    def predict_species(self):
        self.load_data()
        test_array = np.array(list(map(float,self.input_data)))
        pred = self.model.predict([test_array])[0]

        for specie,EncodedVal in self.project_data["Labeled_data"]["Species"].items():
            if EncodedVal == pred:
                species = specie
        return species