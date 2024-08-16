import tensorflow as tf
from tensorflow . keras import layers
from tensorflow . keras . layers import Dense
import matplotlib . pyplot as plt
import numpy as np
import pandas as pd
IMAGE SIZE = 256
BATCH SIZE = 32
training_dataset = tf.keras.preprocessing.image dataset from directory(
’ / content / drive / MyDrive / Train ’ ,
  shuffle=True ,
  image size = (IMAGE SIZE,IMAGE SIZE) ,
  batch size = BATCH SIZE
)
testing_dataset = tf.keras.preprocessing.image dataset from directory( 
’ / content / drive / MyDrive / Test ’ ,
  shuffle=True ,
  image size = (IMAGE SIZE,IMAGE SIZE) ,
  batch size = BATCH SIZE
)
validation dataset = tf.keras.preprocessing.image dataset from directory(
’ / content / drive / MyDrive / Valid ’ ,
  shuffle=True ,
  image size = (IMAGE SIZE,IMAGE SIZE) ,
  batch size = BATCH SIZE
)
