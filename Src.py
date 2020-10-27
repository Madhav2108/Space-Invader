import turtle
import winsound
import os
import math
import random
# made by madhav narayan 
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Space Invaders by Mahesh Sawant")
wn.bgpic("background.gif")

turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0


score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

player = turtle.Turtle()

player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15


number_of_enemies = 10

enemies = []


for i in range(number_of_enemies):
    
    enemies.append(turtle.Turtle())

for enemy in enemies:
    
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y =  random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 5

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 30


bulletstate = "ready"


# made by madhav narayan
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC) 
       
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()


def isCollision_enemy_bullet(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False


def isCollision_enemy_player(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 30:
        return True
    else:
        return False


turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


Game_Over = False
missed_enemies = 0
while True:

    for enemy in enemies:
        # made by madhav narayan
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)


        
        if enemy.xcor() > 270:
            
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285 and Game_Over == False:
                    e.hideturtle()
                    missed_enemies += 1
                    if missed_enemies == 5:
                        Game_Over = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.setposition(x, y)
                    e.showturtle()
            
            enemyspeed *= -1

        if enemy.xcor() < -270:
            
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285 and Game_Over == False:
                    e.hideturtle()
                    missed_enemies += 1
                    if missed_enemies ==5:
                        Game_Over = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.setposition(x, y)
                    e.showturtle()
           
            enemyspeed *= -1
# made by madhav narayan
        if isCollision_enemy_bullet(bullet, enemy):
            winsound.PlaySound("explosion-e+b.wav", winsound.SND_ASYNC) 
            
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            enemyspeed += 0.5
           
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        # made by madhav narayan
        if isCollision_enemy_player(player, enemy):
            Game_Over = True
        if Game_Over == True:
            player.hideturtle()
            bullet.hideturtle()
            for e in enemies:
                e.hideturtle()
            wn.bgpic("end.gif")
            break

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

# made by madhav narayan
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

delay = input("Press enter to finish")