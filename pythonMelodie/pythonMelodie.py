# Import beep from winsound
from winsound import Beep
notes = {'C':1635,'D':1835,'E':2060,'S':1945,'G':2450,'A':2750,'B':3087,' ':37

         }   #Create a dictionary of frequencies
melodie = 'CDSE GAB S AGB DSC EDGA A AAAAB EEES DDDA'
for note in melodie:
    Beep(notes[note],500)  #500 is duration
