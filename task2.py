import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

dataset=pd.read_csv('3_analcatdata_dmft.csv',encoding='utf-8',header=None,sep=';')
print(len(dataset))
train, test = train_test_split(dataset, test_size=0.2)

