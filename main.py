#https://electronstudio.github.io/pygame-zero-book/chapters/chase.html

# TODO explain global variables
import random
import math

jake_speed = 0.5
finn_speed = 12
gumball_speed = 13
score = 0

WIDTH = 1100
HEIGHT = 619 

background = Actor("background")
finn = Actor("finn")
finn.x = 200
finn.y = 200

coin = Actor("coin")
coin.x = 356
coin.y = 289

jake = Actor("jake")
jake.x = 560
jake.y = 450

gumball = Actor("gumball")
gumball.x = 100
gumball.x = 150


def draw():
  screen.clear()
  background.draw()
  finn.draw() 
  jake.draw()
  coin.draw()
  gumball.draw()

def update():
  global jake_speed
  global finn_speed
  global gumball_speed
  global score
  
  # Moving finn around the world
  if keyboard.right:
    finn.x = finn.x + finn_speed
  if keyboard.left:
    finn.x = finn.x - finn_speed
  if keyboard.down:
    finn.y = finn.y +finn_speed
  if keyboard.up:
    finn.y = finn.y - finn_speed
  if finn.x > WIDTH:
    finn.x = 0
  if finn.x < 0:
    finn.x = WIDTH
  if finn.y < 0:
    finn.y = HEIGHT
  if finn.y > HEIGHT:
    finn.y = 0

  # Moving gumball 
  if keyboard.d:
    gumball.x = gumball.x + gumball_speed
  if keyboard.a:
    gumball.x = gumball.x - gumball_speed
  if keyboard.s:
    gumball.y = gumball.y + gumball_speed
  if keyboard.w:
    gumball.y = gumball.y - gumball_speed
  if gumball.x > WIDTH:
    gumball.x = 0
  if gumball.x < 0:
    gumball.x = WIDTH
  if gumball.y < 0:
    gumball.y = HEIGHT
  if gumball.y > HEIGHT:
    gumball.y = 0

  # Moving jake 

  # if jake is closer to finn 
    # move to finn 
  # else if jake is closer to gumball 
    # move to gumball 

  finn_distance = calculate_distance(finn, jake)
  
  gumball_distance = calculate_distance(gumball, jake)

  if finn_distance < gumball_distance: 
    # move jake to finn
    if finn.x > jake.x:
      jake.x = jake.x + jake_speed
    if finn.x < jake.x:
      jake.x =  jake.x - jake_speed
    if finn.y > jake.y:
      jake.y = jake.y + jake_speed
    if finn.y < jake.y:
      jake.y = jake.y - jake_speed
  else: 
    # move jake to gumball
    if gumball.x > jake.x:
      jake.x = jake.x + jake_speed
    if gumball.x < jake.x:
      jake.x =  jake.x - jake_speed
    if gumball.y > jake.y:
      jake.y = jake.y + jake_speed
    if gumball.y < jake.y:
      jake.y = jake.y - jake_speed 
  
  if finn.colliderect(coin):
    coin.x = random.randint(1,WIDTH)
    coin.y = random.randint(1,HEIGHT)
    score = score + 1
    print(score)
    gumball_speed = gumball_speed - 0.6
    jake_speed = jake_speed + 0.7

  if gumball.colliderect(coin):
    coin.x = random.randint(1,WIDTH)
    coin.y = random.randint(1,HEIGHT)
    score = score + 1
    print(score)
    finn_speed = finn_speed - 0.6
    jake_speed = jake_speed + 0.7

  if jake.colliderect(coin):
    coin.x = random.randint(1, WIDTH)
    coin.y = random.randint(1, HEIGHT)
    score = score - 1
    print(score)
    finn_speed = finn_speed - 0.6
    gumball_speed = gumball_speed - 0.6
    jake_speed = jake_speed + 3
    

  if gumball.colliderect(finn):
    finn_speed = finn_speed + 0.01
    gumball_speed = gumball_speed + 0.01
   
  if finn.colliderect(jake):
    exit()
  
  if gumball.colliderect(jake):
    exit()


def calculate_distance(character1, character2):
  
  dx = character2.x - character1.x 
  dy = character2.y - character1.y

  distance = math.sqrt(pow(dx,2) + pow(dy,2))
  return distance 
