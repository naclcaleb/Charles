from __future__ import absolute_import, division, print_function
import tensorflow as tf
tf.enable_eager_execution()
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import unicodedata
import re
import numpy as np
import os
import time
import helpers
import network_functions as nf

optimizer = tf.train.AdamOptimizer()
num_examples = 30000
input_tensor, target_tensor, inp_lang, targ_lang, max_length_inp, max_length_targ = helpers.load_dataset("./data/dataset_1.txt", num_examples)
input_tensor_train, input_tensor_val, target_tensor_train, target_tensor_val = train_test_split(input_tensor, target_tensor, test_size=0.2)
#Hyperparameters
BUFFER_SIZE = len(input_tensor_train)
BATCH_SIZE = 30
N_BATCH = BUFFER_SIZE//BATCH_SIZE
embedding_dim = 256
units = 1024
EPOCHS = 5
vocab_inp_size = len(inp_lang.word2idx)
vocab_tar_size = len(targ_lang.word2idx)

encoder = nf.Encoder(vocab_inp_size, embedding_dim, units, BATCH_SIZE)
decoder = nf.Decoder(vocab_tar_size, embedding_dim, units, BATCH_SIZE)


checkpoint_dir = './training_ckpts'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(optimizer=optimizer, encoder=encoder, decoder=decoder)

checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))


nf.translate('say hello', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ, units)
nf.translate('How are you?', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ, units)
nf.translate('Ok, whatever you want', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ, units)
nf.translate('Never mind', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ, units)
nf.translate('what do you bloody mean?', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ, units)
nf.translate('alright', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ, units)
nf.translate('now', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ, units)

