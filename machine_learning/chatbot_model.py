# -*- coding: utf-8 -*-
"""ChatBot_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19Tu9SoRAiDglSeqwjuhM70ydFoJ9XkMe
"""

from google.colab import drive
drive.mount('/content/drive')

import os
os.chdir('/content/drive/My Drive/SoftwareSecurity')

import pandas as pd
user_type=input("give user type:")
COLUMN_NAMES =['Question','Answer']
DATASET_ENCODING = "ISO-8859-1"
if user_type=="hospital staff":
  questions_dataset = pd.read_csv('questions_hospital_staff.csv', encoding=DATASET_ENCODING, names=COLUMN_NAMES, usecols=['Question'], header=None)
  answers_dataset = pd.read_csv('questions_hospital_staff.csv', encoding=DATASET_ENCODING, names=COLUMN_NAMES, usecols=['Answer'], header=None)
elif user_type=="doctor":
  questions_dataset = pd.read_csv('questions_doctors.csv', encoding=DATASET_ENCODING, names=COLUMN_NAMES, usecols=['Question'], header=None)
  answers_dataset = pd.read_csv('questions_doctors.csv', encoding=DATASET_ENCODING, names=COLUMN_NAMES, usecols=['Answer'], header=None) 
elif user_type=="lab staff":
  questions_dataset = pd.read_csv('questions_lab_staff.csv', encoding=DATASET_ENCODING, names=COLUMN_NAMES, usecols=['Question'], header=None)
  answers_dataset = pd.read_csv('questions_lab_staff.csv', encoding=DATASET_ENCODING, names=COLUMN_NAMES, usecols=['Answer'], header=None) 
elif user_type=="insurance staff":
  questions_dataset = pd.read_csv('questions_insurance_staff.csv', encoding=DATASET_ENCODING, names=COLUMN_NAMES, usecols=['Question'], header=None)
  answers_dataset = pd.read_csv('questions_insurance_staff.csv', encoding=DATASET_ENCODING, names=COLUMN_NAMES, usecols=['Answer'], header=None) 
elif user_type=="administrator":
  questions_dataset = pd.read_csv('questions_administrator.csv', encoding=DATASET_ENCODING, names=COLUMN_NAMES, usecols=['Question'], header=None)
  answers_dataset = pd.read_csv('questions_administrator.csv', encoding=DATASET_ENCODING, names=COLUMN_NAMES, usecols=['Answer'], header=None)
else:
  questions_dataset = pd.read_csv('questions_patients.csv', encoding=DATASET_ENCODING, names=COLUMN_NAMES, usecols=['Question'], header=None)
  answers_dataset = pd.read_csv('questions_patients.csv', encoding=DATASET_ENCODING, names=COLUMN_NAMES, usecols=['Answer'], header=None)

print(questions_dataset)
print(answers_dataset)

!pip install sentence-transformers

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('bert-base-nli-mean-tokens')

q1=questions_dataset.to_numpy()
q2=q1.flatten()
print(q2)

a1=answers_dataset.to_numpy()
a2=a1.flatten()
print(a2)

questions_dataset.to_numpy()
embeddings = model.encode(q2)

sentence_embeddings = embeddings

embeddings_test = model.encode(str(test))

#let's calculate cosine similarity for sentence 0:
similarity=cosine_similarity( [embeddings_test],sentence_embeddings[0:])
print(similarity)

import numpy

index = numpy.argmax(similarity)
print(q2[index])
print(a2[index])

import pickle
with open('chatbot_model.pkl', 'wb') as file:
  pickle.dump(model, file)

import pickle
model = pickle.load(open('chatbot_model.pkl', 'rb'))