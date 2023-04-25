import csv

class Consonants:
    def __init__(self,csv_row) -> None:
        self.place_of_articulation = csv_row[0]
        self.plosive = csv_row[1]
        self.nasal = csv_row[2]
        self.trill = csv_row[3]
        self.tap = csv_row[4]
        self.fricative = csv_row[5]
        self.lateral_fricative = csv_row[6]
        self.approximant = csv_row[7]
        self.lateral_approximate = csv_row[8]

class Vowels ():
    def __init__(self) -> None:
        pass