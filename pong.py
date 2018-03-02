  # https://www.youtube.com/watch?v=Hqf__FlRlzg

import pygame  # great library for making any 2d game in python
import random  # help us define which direction our ball is going to go in

  # start off by defining some of our variables
  # define variables for game
FPS = 60  # frame rate for how fast our game is going to move
WINDOW_WIDTH = 400  # size of our window, square window same witdth same height
WINDOW_HEIGHT = 400

PADDLE_WIDTH = 10  # size of our paddle
PADDLE_WIDTH = 60  # longer than wide

BALL_WIDTH = 10  # size of our ball
BALL_HEIGHT = 10

PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

WHITE = (255, 255, 255)  # color of our paddle and ball
BLACK = (0, 0, 0)

  # initialize our screen
screen = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)  # pygame module set mode to set our screen 

def drawBall(ballXpos, blallYpos):
    ball = pygame.rect(ballXpos, blallYpos, BALL_WIDTH, BALL_HEIGHT)  # use the rect function to draw our ball
    pygame.draw.rect(screen, WHITE, ball)  # draw our ball using draw function predifined screen size color and our ball function we just defined

def drawPaddle1(paddle1YPos):  # our first paddle, our us paddle, our dumb paddle
    paddle1 = pygame.rect(PADDLE_BUFFER, paddle1YPos, PADDLE_WIDTH, PADDLE_WIDTH)  # buffer so it doesnt hit the edge of the screen
    pygame.draw.rect(screen, WHITE, paddle1)
  # same thing for our next paddle, our evil ai, hes on some shit
def drawPaddle2(paddle2YPos):
    paddle2 = pygame.rect(WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH, paddle2YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.rect(screen, WHITE, paddle2)

def updateBall(paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXDirection, ballYDirection):
      # update x and y position
    ballXpos = ballXpos + ballXDirection * BALL_X_SPEED
    ballYpos = ballYpos + ballYDirection * BALL_Y_SPEED
    score = 0

    if(ballXPos <= PADDLE_BUFFER + PADDLE_WIDTH and ballYPos + BALL_HEIGHT >= paddle1Ypos and ballYpos - BALL_HEIGHT <= paddle1Ypos + PADDLE_HEIGHT):
          # check for collision if the ball hits the left side then switch direction
        ballXDirection = 1
    elif(ballXpos <= 0):
        ballXDirection = 1
        score = -1
        return [ score, paddle1YPos, paddle2Ypos, ballXpos, ballYpos, ballXDirection, ballYDirection]
      # check the other side
    if(ballXpos >= WINDOW_WIDTH - PADDLE_WIDTH - PADDLE_BUFFER and ballYpos + BALL_HEIGHT >= paddle2YPos and ballYpos - BALL_HEIGHT <= paddle2Ypos + PADDLE_HEIGHT):
        ballXDirection = -1
    elif(ballXPos >= WINDOW_WIDTH - BALL_WIDTH):
        ballXDirection = -1
        score = 1
        return [ score, paddle1YPos, paddle2Ypos, ballXpos, ballYpos, ballXDirection, ballYDirection]


