'''
bverfgex
---------------------
Kilian Lüders & Bent Stohlmann
Contact: kilian.lueders@hu-berlin.de
02.05.2023

For the purpose of the workshop and the tutorial, we have provided several tools here to demonstrate our work. 

On the one hand, the functions to work with BVerfGE references are in the file verweis.py.
On the other hand, the functions in llconutils.py provide easy access to the decisions LLCon dataset (xml files). 

At this point, we just combine the two, so everything can be imported like a normal package:

from bverfgex import *

'''

from .verweis import *
from .llconutils import *