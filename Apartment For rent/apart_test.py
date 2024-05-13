#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#%%

df = pd.read_csv('z Sample Project/Apartment For rent/apartments_for_rent_classified_10K.csv', sep=";", encoding='cp1252')

#%%
df.info()
df.head()
