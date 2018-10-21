import pandas as pd
import numpy as np
import csv
from subprocess import Popen, PIPE


# TODO: Correct the output, has `"` as the starting character

path = input('Enter the directory in which Fr and En txt files are:')

with open('{0}/europarl-v7.fr-en.fr'.format(path), 'r') as file:
	fr_snts = file.readlines()

	## Mapping the sentences with the help of a dataframe
	dataset = pd.DataFrame(np.nan,index=range(len(fr_snts)), columns=['fr','en'])
	dataset['fr'] = fr_snts

with open ('{0}/europarl-v7.fr-en.en'.format(path)) as enFile:
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

## Output files
train.to_csv('../data/fr-en/train.fr',line_terminator='', columns=['fr'],header=False,index=False,sep=' ',encoding='utf-8')
train.to_csv('../data/fr-en/train.en',line_terminator='', columns=['en'],header=False,index=False,sep=' ',encoding='utf-8')
valid.to_csv('../data/fr-en/train.fr',line_terminator='', columns=['fr'],header=False,index=False,sep=' ',encoding='utf-8')
valid.to_csv('../data/fr-en/train.en',line_terminator='', columns=['en'],header=False,index=False,sep=' ',encoding='utf-8')
test.to_csv('../data/fr-en/train.fr',line_terminator='', columns=['fr'],header=False,index=False,sep=' ',encoding='utf-8')
test.to_csv('../data/fr-en/train.en',line_terminator='', columns=['en'],header=False,index=False,sep=' ',encoding='utf-8')

## CHECK: Try to run the perl scripts from python
for j in ['train','valid','test']:
	for i in ['en','fr']:
		var = r'./data/{}.{}.atok'.format(j,i)
		print('perl ../tools/tokenizer.perl -a -no-escape -l {0} < {1}.{2} > {3}.{4}.atok'.format(i,j,i,j,i))
