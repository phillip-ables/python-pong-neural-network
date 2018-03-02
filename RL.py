  # our reinforcement learning with tensor flow
import tensorflow as tf
from opencv import cv2  # open cv helps us format our pixel data better for reading in tensor flow
import pong
import numpy as np  # which is going to help us with math
import random
from collections import deque  # store some memory in this deque 

  # defining hyperparameters
ACTIONS = 3  # up down or stay
  # learning rate
GAMME = 0.99
  # when we update our gradient or training we want to make sure our epsilon equals 1.05
INITIAL_EPSILON = 1.0
FINAL_EPSILON = 0.05
  # how many frames do we want to anneal our epsilon
EXPLORE = 500000
OBSERVE = 50000
REPLAY_MEMORY = 50000
BATCH = 100  # batch size how many times we want to train

  # five layer convulusional nuero network, a convulusional neuro network is the kind that reads an image
  # create TensorFlow TF graph
def createGraph():
      # we want to first create our first convolutional layer, bias vector
      # tf.zeros start an empty tensor graph with just zeros and we are going to fill it with information over time
    W_conv1 = tf.Variable(tf.zeros([8, 8, 4, 32]))  # first convolusional layer using tensor flow variables and define the size of it,
    b_conv1 = tf.Variable(tf.zeros[32])  # our bias vector will help us find out in what way we want our data to flow, 32 bits

      # second convolutional layer
    W_conv2 = tf.Variable(tf.zeros[4,4,32,64])
    b_conv2 = tf.Variable(tf.zeros[64])

      # third
    W_conv3 = tf.Variable(tf.zeros[3,3,64,64])
    b_conv3 = tf.Variable(tf.zeros[64])

    W_fc4 = tf.Variable(tf.zeros[784, ACTIONS])
    b_fc4 = tf.Variable(tf.zeros[784])

      # last layer
    W_fc5 = tf.Variable(tf.zeros[784, ACTIONS])
    b_fc5 = tf.Variable(tf.zeros[ACTIONS])

    '''
    we created five layers 
    and in each of them we created an input size
    '''
