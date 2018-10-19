import pandas as pd
import numpy as np
import csv

with open('./europarl-v7.fr-en.fr', 'r') as file:
	fr_snts = file.readlines()

	## Mapping the sentences with the help of a dataframe
	dataset = pd.DataFrame(np.nan,index=range(len(fr_snts)), columns=['fr','en'])
	dataset['fr'] = fr_snts

with open ('./europarl-v7.fr-en.en') as enFile:
	dataset.en = enFile.readlines()

## Shuffling the dataset
dataset = dataset.sample(frac=1)
#print(dataset.head())
#print()
train_marker = int(0.85*len(fr_snts))
val_marker = int(0.90*len(fr_snts))
test_marker = int(1.00 *len(fr_snts))

train = dataset.iloc[:train_marker,:]
valid = dataset.iloc[train_marker:val_marker,:]
test  = dataset.iloc[val_marker:test_marker,:]
#print(train.head())
train.to_csv('/Users/rajat/Downloads/fr-en/train.en',line_terminator='', columns=['fr'],header=False,index=False,sep=' ',encoding='utf-8')
