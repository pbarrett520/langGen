import pandas as pd

class Consonants:
    def __init__(self,csv_file) -> None:
        # Read csv into dataframe, label columns
        self.phones = pd.read_csv(csv_file)
        self.phones.columns = ['place','bilabial','labiodental','dental','alveolar','postalveolar','retroflex',
                               'palatal','velar','uvular','pharyngal','glottal']
        # Convert columns into plain Python arrays, we don't need NP arrays
        self.place_of_articulation = self.phones.place.to_list()
        self.bilabial = self.phones.bilabial.to_list()
        self.labiodental = self.phones.labiodental.to_list()
        self.dental = self.phones.dental.to_list()
        self.alveolar = self.phones.alveolar.to_list()
        self.postalveolar = self.phones.postalveolar.to_list()
        self.retroflex = self.phones.retroflex.to_list()
        self.palatal = self.phones.palatal.to_list()
        self.velar = self.phones.velar.to_list()
        self.uvular = self.phones.uvular.to_list()
        self.pharyngal = self.phones.pharyngal.to_list()
        self.glottal = self.phones.pharyngal.to_list()
        # Do same conversion for rows, process is different because of Pandas weirdness
        self.plosive = self.phones.iloc[[0]].values.flatten().tolist()
        self.nasal = self.phones.iloc[[1]].values.flatten().tolist()
        self.trill = self.phones.iloc[[2]].values.flatten().tolist()
        self.tap = self.phones.iloc[[3]].values.flatten().tolist()
        self.fricative = self.phones.iloc[[4]].values.flatten().tolist()
        self.lateral_fricative = self.phones.iloc[[5]].values.flatten().tolist()
        self.approximant = self.phones.iloc[[6]].values.flatten().tolist()
        self.lateral_approximant = self.phones.iloc[[7]].values.flatten().tolist()


class Vowels:
    def __init__(self,csv_file) -> None:
        self.phones = pd.read_csv(csv_file)
        self.phones.columns = ['vowels','closeness','frontness','roundness']
        self.vowels = self.phones.vowels.to_list()
        self.closeness = self.phones.closeness.to_list()
        self.frontness = self.phones.frontness.to_list()
        self.roundness = self.phones.roundness.to_list()