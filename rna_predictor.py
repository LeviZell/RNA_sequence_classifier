""" 
Read input file

usage: python rna_file.py ./data/pyrococcus_furiousus.genome  
"""

import sys 
import numpy as np
import h5py
from operator import itemgetter
from itertools import groupby
from tensorflow.keras.models import load_model, predict

def readfile(fname):
  with open(fname, 'r') as genome:
    dna_seq_str = genome.readlines()[0]
  return dna_seq_str

def one_hot_encode(gen_str):
  gen_arr = np.asarray(list(gen_str)

  gen_arr[gen_arr == 'A'] = 0
  gen_arr[gen_arr == 'T'] = 1
  gen_arr[gen_arr == 'C'] = 2
  gen_arr[gen_arr == 'G'] = 3

  gen_arr=gen_arr.astype(int)

  return gen_arr

def load_saved_model():
  model=load_model('my_model.h5')
  return data

def get_RNA_from_genes(prediction):
  start_inds=[]
  end_inds=[]
  rna_inds=[]
  indexes = [next(group) for key, group in groupby(enumerate(myList), key=itemgetter(1))]

  for inds in indexes:
    if inds[1] == 1]
      start_ind.append(inds[0])
    else:
      end_ind.append(inds[0])

  for s_ind in start_inds:
    e_ind = next(i for i in end_inds if i > s_ind)
    rna_inds.append([s_ind, e_ind])
    
  return rna_inds

def save_indices(gene_lst):
  with open('genes.txt', 'w') as genes:
    for start_end in gene_lst:
      genes.write(str(start_end[0])+' '+str(start_end[1])+'\n')
      print(str(start_end[0])+' '+str(start_end[1])+' '+str([start_end[0]: start_end[1]])+'\n')

def main(argv):
  if len(argv) != 1:
    print ('You promised only 1 input...')
    sys.exit(1)
  
  fname = argv[0]
  dna_seq_str = readfile(fname)
  dna_seq_arr = one_hot_encode(dna_seq_str)

  # load model
  model=load_saved_model()
  
  #predict
  prediction = model.predict(dna_seq_arr)
  
  # get RNA segment indices
  genes_lst = get_RNA_from_genes(prediction)

  # save and print RNA seq indices
  save_indices(gene_lst)

if __name__=='__main__':
  main(sys.argv[1:])

