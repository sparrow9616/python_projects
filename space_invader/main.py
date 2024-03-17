import pygame
import random
import math
from pygame import mixer


pygame.init()

# Create screen

screen = pygame.display.set_mode((1080, 720))

# Background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (1080, 720))

# background music

mixer.music.load("background.wav")
mixer.music.play(-1)

# Create title and Icon

pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

running = True

# Score
score_value = 0
score_font = pygame.font.Font("freesansbold.ttf", 32)
score_text_x = 10
score_text_y = 10


def show_score(x, y):
    score = score_font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Game over text
game_over_font = pygame.font.Font("freesansbold.ttf", 64)


def game_over_text():
    game_over = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (500, 360))


# PLayer

playerImg = pygame.image.load("player.png")
playerX = 500
playerY = 580
playerXchange = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyX.append(random.randint(0, 1000))
    enemyY.append(random.randint(50, 150))
    enemyXchange.append(2)
    enemyYchange.append(40)


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet
# Ready - Bullet hidden
# Fire - Bullet seems to fire
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 580
bulletXchange = 0
bulletYchange = 5
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distance < 27:
        return True
    else:
        return False


while running:

    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -3
            if event.key == pygame.K_RIGHT:
                playerXchange = 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0

    playerX += playerXchange

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1000:
        playerX = 1000

    # enemy movement

    for i in range(num_of_enemies):

        # Game over
        if enemyY[i] > 550:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyXchange[i]
        if enemyX[i] <= 0:
            enemyXchange[i] = 2
            enemyY[i] += enemyYchange[i]
        elif enemyX[i] >= 1000:
            enemyXchange[i] = -2
            enemyY[i] += enemyYchange[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play()
            bulletY = 580
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 1000)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i])

    if bulletY <= 0:
        bulletY = 580
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletYchange

    player(playerX, playerY)
    show_score(score_text_x, score_text_y)
    pygame.display.update()
