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
