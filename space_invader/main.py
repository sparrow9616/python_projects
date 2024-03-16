import pygame
import random

pygame.init()

# Create screen

screen = pygame.display.set_mode((1080, 720))

# Background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (1080, 720))


# Create title and Icon

pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

running = True

# PLayer

playerImg = pygame.image.load("player.png")
playerX = 500
playerY = 580
playerXchange = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 1000)
enemyY = random.randint(50, 150)
enemyXchange = 2
enemyYchange = 40


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet
# Ready - Bullet hidden
# Fire - Bullet seems to fire
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 580
bulletXchange = 0
bulletYchange = 10
bullet_state = "ready"


def fire_bullet(x, y):
    print(x, y)
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


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
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0

    playerX += playerXchange

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1000:
        playerX = 1000

    enemyX += enemyXchange

    if enemyX <= 0:
        enemyXchange = 2
        enemyY += enemyYchange
    elif enemyX >= 1000:
        enemyXchange = -2
        enemyY += enemyYchange

    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletYchange

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
