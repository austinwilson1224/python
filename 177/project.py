path = "/Users/austinwilson/downloads/archive/"

'''

files 

genome_scores.csv	link.csv		rating.csv
genome_tags.csv		movie.csv		tag.csv

''' 

import pandas as pd
import numpy as np 


movies = pd.read_csv(path+"movie.csv")
ratings = pd.read_csv(path+"rating.csv")

movies.head()
ratings.head()