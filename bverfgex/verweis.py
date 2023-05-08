'''
verweis.py
---------------------
Kilian Lüders & Bent Stohlmann
Contact: kilian.lueders@hu-berlin.de
02.05.2023

This file contains the classes Verweis & Verweiskette and the functions for extracting the BVerfGE references from text.
'''



import re

# creat classes
######################

class Verweis:
    '''
    A class used to represent BVerfGE References.

    Attributes
    ----------
    band:
        Volume of the decision referred to.
    anfang:
        First page of the decision referred to.
    ref:
        Precise reference (optional).
    ref_clean:
        Cleaned precise reference (optional). Only the first digits of ref are included.
    _ref_print:
        String for output (better readability.): Precise reference in square brackets if available. Otherwise empty string.

    Methods:
    ----------
    to_short_str:
        Returns reference as a string in the following notation: "BVerfGE58_300" (exact reference omitted)
    to_info_str:
        Returns only reference information as a string in the following notation "58, 300 [351]" ('BVerfGE' is omitted). 

    _set_clean_ref: internal method to set ref_clean
    _set_print_ref: internal method to set _ref_print
    
    Usage:
    ----------
    example "BVerfGE 58, 300 [336]":
    obj = Verweis(band="58", anfang="300", ref="336")
    obj

    Explanation:
    ----------
    BVerfGE references have the following notation: BVerfGE 58, 300 [336]
    'BVerfGE' is the name of the official collection of decisions.
    The first number indicates the volume (58), followed by the first page of the decision (300) and an optional pricise reference (336). 
    '''
    def __init__(self, band='', anfang='', ref=''):
        self.band = str(band).strip()
        self.anfang = str(anfang).strip()
        self.ref = ref
        self._set_clean_ref(ref)
        self._set_print_ref(ref)

    def __repr__(self) -> str:
        return 'BVerfGE ' + str(self.band) + ', ' + str(self.anfang) + self._ref_print
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Verweis):
            return (self.band == other.band) and (self.anfang == other.anfang) and (self.ref == other.ref)
        return False

    def _set_clean_ref(self, ref):
        if ref != '' and ref != None:
            clean_ref = re.search(r'\d{1,3}',ref)
            if clean_ref != None:
                self.ref_clean = str(clean_ref.group(0))
            else:
                self.ref_clean = None
        else:
            self.ref_clean = None

    def _set_print_ref(self, ref):
        if ref != '' and ref != None:
            self._ref_print = " [" + str(self.ref).strip() + "]"
        else:
            self._ref_print = ""

    def to_short_str(self) -> str:
        return 'BVerfGE' + str(self.band) + '_' + self.anfang

    def to_info_str(self) -> str:
        return str(self.band) + ', ' + str(self.anfang) + self._ref_print


class VerweiskettenIterator:
    '''
    Class to implement an iterator
    '''
    def __init__(self, kette):
        self._kette = kette
        self._index = 0
    
    def __next__(self):
        if self._index < len(self._kette):
            result = self._kette.kette[self._index]
            self._index += 1
            return result
        raise StopIteration


class Verweiskette:
    '''
    A class used to represent BVerfGE string citations.
    This is ultimately a list of Verweis objects.

    Correspondingly, objects of the class Verweiskette also have typical properties of lists:
    - Output length: len(obj) 
    - Iteration: [e for e in obj]
    - Get items from the list: obj[i]

    Methods:
    ----------
    to_list:
        returns a list of Verweis objects
    to_short_ref:
        returns a list of reference as strings in the short string notation.
    
    Usage:
    ----------
    example: "BVerfGE 37, 132 [140]; 50, 290 [339]; 52, 1 [31]"

    Verweiskette([Verweis(band="37", anfang="132", ref="140"),
                  Verweis(band="50", anfang="290", ref="339"),
                  Verweis(band="52", anfang="1", ref="31")])
    '''
    def __init__(self, verweise_input):
        if type(verweise_input) == list and all([type(e) == Verweis for e in verweise_input]):
            self.kette = verweise_input
            self.len = len(verweise_input)
        elif type(verweise_input) == Verweis:
            self.kette = [verweise_input]
            self.len = 1
        else:
            raise TypeError
    
    def __len__(self):
        return self.len

    def __repr__(self):
        return "BVerfGE " + "; ".join([e.to_info_str() for e in self.kette])
    
    def __iter__(self):
        return VerweiskettenIterator(self)

    def __getitem__(self, item):
        return self.kette[item]

    def to_list(self):
        return self.kette

    def to_short_str(self):
        return [e.to_short_str() for e in self if e.to_short_str() != None]



# functions for extractions
######################

#regex pattern to identify string citations
pattern_bverfge = re.compile(r'BVerfGE(?:;?\s?\d{1,3},?\s?\d{1,3}\s?f{0,2}\.?(?:\s?-.+?-)?){1,20}(?:;?\s?(?:st\.?\s?Rspr\.?|m\.?w\.?N\.))?')
#regex pattern to extract the information for each reference of the string citation
pattern_bverfge_inner = re.compile(r'(?P<band>\d{1,3}),?\s?(?P<aseite>\d{1,3}\s?f{0,2}\.?)\s?(?P<ref>-.+?-)?')

def clean_ref(ref):
    '''
    Small helper function to clean up exact references
    '''
    if type(ref) == str:
        return ref.replace("-","")
    else:
        return None

def transform_verweis(bverfge_zitat: str) -> Verweiskette:
    '''
    Splits string citations (string) into several references (Verweiskette with Verweise objects).
    '''
    kette = pattern_bverfge_inner.finditer(bverfge_zitat)
    verweise = Verweiskette([Verweis(band=t.group("band"), anfang=t.group("aseite"), ref=clean_ref(t.group("ref"))) for t in kette])

    return verweise

def search_bverfge_verweis(text: str) -> list:
    '''
    Text is searched for BVerfGE string citations.

    Input: text
    Output: list of Verweisketten objects.
    '''
    text = text.replace('[','-').replace(']','-')
    ls_zitate = pattern_bverfge.findall(text)
    return list(map(transform_verweis, ls_zitate))