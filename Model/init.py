import os
import pandas as pd

cwd = os.getcwd()
file = os.path.join(cwd, '..\\dataset\\BostonHousing.csv')

df = pd.read_csv(file, delimiter=',')
