# Tutorial: https://pygame-zero.readthedocs.io/en/stable/introduction.html

# Docs:
#https://pygame-zero.readthedocs.io/en/1.1/builtins.html

WIDTH = 500
HEIGHT = 500

ball = Rect((200, 400), (20, 20))
paddle = Rect((0,250), (20,60))
paddle2 = Rect((480,240), (20,60))

velocity_x = 0

velocity_y = 0

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, "red")
    screen.draw.filled_rect(paddle, "white")
    screen.draw.filled_rect(paddle2, "white")

def on_key_down(key):
  if key == keys.UP:
    paddle2.top = paddle2.top - 45
  if key == keys.DOWN:
    paddle2.bottom = paddle2.bottom + 45
  if key == keys.W:
    paddle.top = paddle.top - 45
  if key == keys.S:
    paddle.bottom = paddle.bottom + 45
  
def update():
  global velocity_x, velocity_y
  ball.x = ball.x + velocity_x
  ball.y = ball.y + velocity_y
  if ball.bottom > HEIGHT or ball.top < 0:
    velocity_y = -velocity_y 
  if ball.colliderect(paddle) or ball.colliderect(paddle2):
    velocity_x = -velocity_x
  if ball.right > WIDTH or ball.left < 0:
    exit()
  if paddle.bottom > HEIGHT:
    paddle.bottom = HEIGHT
  if paddle2.bottom > HEIGHT:
    paddle2.bottom = HEIGHT
  if paddle.top < 0:
    paddle.top = 0
  if paddle2.top < 0:
    paddle2.top = 0
