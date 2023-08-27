import pandas as pd
import re
from itertools import product
from random import sample

class Consonants:
    def __init__(self,csv_file) -> None:
        # Read consonants csv into dataframe, label columns
        self.phonesC = pd.read_csv(csv_file)
        self.phonesC.columns = ['place','bilabial','labiodental','dental','alveolar','postalveolar','retroflex',
                               'palatal','velar','uvular','pharyngal','glottal']
        # Convert columns into plain Python arrays, we don't need NP arrays
        self.place_of_articulation = self.phonesC.place.to_list()
        self.bilabial = self.phonesC.bilabial.to_list()
        self.labiodental = self.phonesC.labiodental.to_list()
        self.dental = self.phonesC.dental.to_list()
        self.alveolar = self.phonesC.alveolar.to_list()
        self.postalveolar = self.phonesC.postalveolar.to_list()
        self.retroflex = self.phonesC.retroflex.to_list()
        self.palatal = self.phonesC.palatal.to_list()
        self.velar = self.phonesC.velar.to_list()
        self.uvular = self.phonesC.uvular.to_list()
        self.pharyngal = self.phonesC.pharyngal.to_list()
        self.glottal = self.phonesC.pharyngal.to_list()
        # Do same conversion for rows, process is different because of Pandas weirdness
        self.plosive = self.phonesC.iloc[[0]].values.flatten().tolist()
        self.nasal = self.phonesC.iloc[[1]].values.flatten().tolist()
        self.trill = self.phonesC.iloc[[2]].values.flatten().tolist()
        self.tap = self.phonesC.iloc[[3]].values.flatten().tolist()
        self.fricative = self.phonesC.iloc[[4]].values.flatten().tolist()
        self.lateral_fricative = self.phonesC.iloc[[5]].values.flatten().tolist()
        self.approximant = self.phonesC.iloc[[6]].values.flatten().tolist()
        self.lateral_approximant = self.phonesC.iloc[[7]].values.flatten().tolist()


        # Read vowels CSV into seperate dataframe
        self.phonesV = pd.read_csv(csv_file)
        self.phonesV.columns = ['vowels','closeness','frontness','roundness']
        self.vowels = self.phonesV.vowels.to_list()
        self.closeness = self.phonesV.closeness.to_list()
        self.frontness = self.phonesV.frontness.to_list()
        self.roundness = self.phonesV.roundness.to_list()