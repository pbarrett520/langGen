import pandas as pd
import re
from itertools import product
from random import sample

<<<<<<< HEAD

class Phones:

    def __init__(
        self,
        voiced_cons_csv_file: str,
        voiceless_cons_csv_file: str,
        vowels_csv_file: str,
        syll_struct: str,
    ) -> None:

        self.syll_struct = rf"{syll_struct}"  # define syllable structure with regex

=======
class Syllable_patterns:

    polyneisian = r"[ptkfsbdgvznmʔ]?[ɑeiouə]?[ɑeiouə][ʔnm]?"
    south_sinitic = r"[ptkbdgtsdztʃʔmnŋlɻjw]?[aeiouyɑɛɪʊœɐɚɤøəɨʉɛ̃ɔ̃ãõĩũ][ptkbdgʔmnŋl]?"
    north_sinitic = r"[ptkbdgʈʂʐtsdzɕʑtʃʔmnŋlɻjw]?[aeiouyɑɛɪʊœɐɚɤøəɨʉɛ̃ɔ̃ãõĩũ][ʔnŋ]"

class Phones:
    def __init__(self,voiced_cons_csv_file: str, voiceless_cons_csv_file: str, vowels_csv_file: str, syll_struct: str) -> None:

        self.syll_struct = rf"{syll_struct}" # define syllable structure with regex
        self.syll_inventory = list() # list to be populated later when make_sylls() is called
>>>>>>> e401e23a640e647388b48f0576c952e2d9d4bed5
        # Read consonants csv into dataframe, label columns
        self.phonesVC = pd.read_csv(voiced_cons_csv_file)
        self.phonesVC.columns = [
            "place",
            "bilabial",
            "labiodental",
            "dental",
            "alveolar",
            "postalveolar",
            "retroflex",
            "palatal",
            "velar",
            "uvular",
            "pharyngal",
            "glottal",
        ]

        self.phonesVLESSC = pd.read_csv(voiceless_cons_csv_file)
        self.phonesVLESSC.columns = [
            "place",
            "bilabial",
            "labiodental",
            "dental",
            "alveolar",
            "postalveolar",
            "retroflex",
            "palatal",
            "velar",
            "uvular",
            "pharyngal",
            "glottal",
        ]
        # Convert columns into plain Python arrays, we don't need NP arrays
        self.place_of_articulation = self._clean(self.phonesVC.place.to_list())
        self.bilabial = self._clean(
            self.phonesVC.bilabial.to_list() + self.phonesVLESSC.bilabial.to_list()
        )
        self.labiodental = self._clean(
            self.phonesVC.labiodental.to_list()
            + self.phonesVLESSC.labiodental.to_list()
        )
        self.dental = self._clean(
            self.phonesVC.dental.to_list() + self.phonesVLESSC.dental.to_list()
        )
        self.alveolar = self._clean(
            self.phonesVC.alveolar.to_list() + self.phonesVLESSC.alveolar.to_list()
        )
        self.postalveolar = self._clean(
            self.phonesVC.postalveolar.to_list()
            + self.phonesVLESSC.postalveolar.to_list()
        )
        self.retroflex = self._clean(
            self.phonesVC.retroflex.to_list() + self.phonesVLESSC.retroflex.to_list()
        )
        self.palatal = self._clean(
            self.phonesVC.palatal.to_list() + self.phonesVLESSC.palatal.to_list()
        )
        self.velar = self._clean(
            self.phonesVC.velar.to_list() + self.phonesVLESSC.velar.to_list()
        )
        self.uvular = (
            self.phonesVC.uvular.to_list() + self.phonesVLESSC.uvular.to_list()
        )
        self.pharyngal = self._clean(
            self.phonesVC.pharyngal.to_list() + self.phonesVLESSC.pharyngal.to_list()
        )
        self.glottal = self._clean(
            self.phonesVC.glottal.to_list() + self.phonesVLESSC.glottal.to_list()
        )
        # Do same conversion for rows, process is different because of Pandas weirdness
        self.plosive = self._clean(
            self.phonesVC.iloc[[0]].values.flatten().tolist()
            + self.phonesVLESSC.iloc[[0]].values.flatten().tolist()
        )
        self.nasal = self._clean(
            self.phonesVC.iloc[[1]].values.flatten().tolist()
            + self.phonesVLESSC.iloc[[1]].values.flatten().tolist()
        )
        self.trill = self._clean(
            self.phonesVC.iloc[[2]].values.flatten().tolist()
            + self.phonesVLESSC.iloc[[2]].values.flatten().tolist()
        )
        self.tap = self._clean(
            self.phonesVC.iloc[[3]].values.flatten().tolist()
            + self.phonesVLESSC.iloc[[3]].values.flatten().tolist()
        )
        self.fricative = self._clean(
            self.phonesVC.iloc[[4]].values.flatten().tolist()
            + self.phonesVLESSC.iloc[[4]].values.flatten().tolist()
        )
        self.lateral_fricative = self._clean(
            self.phonesVC.iloc[[5]].values.flatten().tolist()
            + self.phonesVLESSC.iloc[[5]].values.flatten().tolist()
        )
        self.approximant = self._clean(
            self.phonesVC.iloc[[6]].values.flatten().tolist()
            + self.phonesVLESSC.iloc[[6]].values.flatten().tolist()
        )
        self.lateral_approximant = self._clean(
            self.phonesVC.iloc[[7]].values.flatten().tolist()
            + self.phonesVLESSC.iloc[[7]].values.flatten().tolist()
        )

        self.all_consonants = self._clean(
            self.plosive
            + self.nasal
            + self.trill
            + self.tap
            + self.fricative
            + self.lateral_fricative
            + self.approximant
            + self.lateral_approximant
        )

        # Read vowels CSV into dataframe
        self.phonesV = pd.read_csv(vowels_csv_file)
        self.phonesV.columns = ["vowels", "closeness", "frontness", "roundness"]
        self.all_vowels = self._clean(self.phonesV.vowels.to_list())
        self.closeness = self._clean(self.phonesV.closeness.to_list())
        self.frontness = self._clean(self.phonesV.frontness.to_list())
        self.roundness = self._clean(self.phonesV.roundness.to_list())

    # Function clears extra strings leftover by NaN values in the lists,
    # also makes sure other naughty strings don't wind up in here on accident
    def _clean(self, data: iter) -> iter:

        NaN = re.compile(r"^NaN$")
        any_single_char = re.compile(r"^([^\s])$")
        clean_list = [
            str(datum)
            for datum in data
            if not re.match(NaN, str(datum)) and re.match(any_single_char, str(datum))
        ]

        return clean_list

    def make_sylls(self, size: int) -> list[tuple]:
        """
         Takes a list of consonants, a list of vowels, a regex (syll_struct),
         and an integer (size). as arguments. Function will generate the Cartesian product of
         the consonants and vowels lists, then sort through the resulting strings for ones which
         match the regex. Randomly sampled list of matches up to the size of the "size"
        argument is returned.
        """
        cons = [str(c) for c in self.all_consonants]
        vowels = [str(v) for v in self.all_vowels]
        cartesian_product = product(cons, vowels, vowels, cons)

        def join_tuple_strings(list_of_tuples):
            return "".join(
                list_of_tuples
            )  # helper function to make getting the strings from the tuples easier

        sylls = list()

        for combination in cartesian_product:
            syll = join_tuple_strings(combination)

            if re.match(self.syll_struct, syll):
                sylls.append(syll)

        syll_inventory = sorted(sample(sylls,size))
        self.syll_inventory = syll_inventory

        return syll_inventory
