# NMT-with-OpenNMT-Py


Some basic starter kits to address the Neural MAchine Translation(NMT) problem using OpenNMT-Py. OpenNMT library was created by [@harvardNLP](https://twitter.com/harvardnlp/). It is released under MIT license so it can also be used for commercial purpose. OpenNMT-Py is a port of the original library in Lua to Pytorch This repo stores codes for my article on Medium titled __Creating your own Language Translator__. These are basic commands that needs to be executed and a more [detailed version](http://opennmt.net/OpenNMT-py/extended.html) is avilable at OpenNMT-Py website. The reason I wrote this article was because when I was working on NMT I had the codes at one place but the explanations on why we are doing that step was not avilable. To bridge the gap, I thought of writing an article(my first article).


## Code

Run the following in your terminal
```shell
## To download the OpenNMT library
git clone https://github.com/OpenNMT/OpenNMT-py
cd OpenNMT-py

## Installing the requiremnets
pip install -r requirements.txt

## Downloading the data (if wget not avilable, then download using a browser by going to the link)
wget http://www.statmt.org/europarl/v7/fr-en.tgz

## Extraing the files
mkdir ./data/fr-en
tar -xf fr-en.tgz -C data/fr-en/

## Clone this repository to get the python script for creating train, test, val
git clone https://github.com/R1j1t/NMT-with-OpenNMT-Py.git
cd NMT-with-OpenNMT-Py

## This will create 3 divisons in the dataset
python3 dataset_split.py

## Moving back to main folder
cd ..

## Install `perl`
## Run the default tokenizer script to tokenize the dataset
## You can use your own tokenizer, but remember to use the same tokenizer in production
## NOTE: This will take a 5-10 minutes because of the size of the dataset
perl ./tools/tokenizer.perl -a -no-escape -l en < ./data/fr-en/train.en > ./data/fr-en/train.en.atok
perl ./tools/tokenizer.perl -a -no-escape -l fr < ./data/fr-en/train.fr > ./data/fr-en/train.fr.atok
perl ./tools/tokenizer.perl -a -no-escape -l en < ./data/fr-en/val.en > ./data/fr-en/val.en.atok
perl ./tools/tokenizer.perl -a -no-escape -l fr < ./data/fr-en/val.fr > ./data/fr-en/val.fr.atok
perl ./tools/tokenizer.perl -a -no-escape -l en < ./data/fr-en/test.en > ./data/fr-en/test.en.atok
perl ./tools/tokenizer.perl -a -no-escape -l fr < ./data/fr-en/test.fr > ./data/fr-en/test.fr.atok

## Creating the vocab using the OpenNMT-Py Preprocessing
## NOTE: This will take a 5-10 minutes because of the size of the dataset
python3 preprocess.py -train_src data/fr-en/train.en.atok -train_tgt data/fr-en/train.fr.atok -valid_src data/fr-en/val.en.atok -valid_tgt data/fr-en/val.fr.atok -save_data data/fr-en/fr-en.atok.low -lower

## Training the model

## ====   If using GPU    ==== ##
python3 train.py -data data/fr-en/fr-en.atok.low -save_model data/fr-en/ckt/fr-en_model -gpu_ranks 0 -enc_layers 2 -dec_layer 2 -optim adam -learning_rate 0.001 -learning_rate_decay 1 -train_steps 10000

## ====   Only CPU    ==== ##
python3 train.py -data data/fr-en/fr-en.atok.low -save_model data/fr-en/ckt/fr-en_model -enc_layers 2 -dec_layer 2 -optim adam -learning_rate 0.001 -learning_rate_decay 1 -train_steps 10000

## Translate on trained model
python translate.py -gpu 0 -model data/fr-en/ckt/fr-en_model_*_e13.pt -src data/fr-en/test.en.atok -tgt data/fr-en/test.fr.atok -replace_unk -verbose -output multi30k.test.pred.atok
```

Thats it!!
