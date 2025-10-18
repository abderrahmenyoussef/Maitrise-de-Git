import numpy as np 
import pandas as pd 
#creer un array 2 dim 10lignes et 10cols 
array_2d = np.random.randint(0,100,size=(10,3))
#creer un dataframe a partir de cet array
df = pd.DataFrame(array_2d)
print(df.head())
#afficher les infos du dataframe
print(df.info())