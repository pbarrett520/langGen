import pandas as pd

class Consonants:
    def __init__(self,csv_file) -> None:
        self.phones = pd.read_csv(csv_file)
        self.phones.columns = ['place','bilabial','labiodental','dental','alveolar','postalveolar','retroflex',
                               'palatal','velar','uvular','pharyngal','glottal']
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


class Vowels:
    def __init__(self,csv_file) -> None:
        self.phones = pd.read_csv(csv_file)
        self.phones.columns = ['vowels','closeness','frontness','roundness']
        self.vowels = self.phones.vowels.to_list()
        self.closeness = self.phones.closeness.to_list()
        self.frontness = self.phones.frontness.to_list()
        self.roundness = self.phones.roundness.to_list()