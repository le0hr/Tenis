import pygame, os, time, ballMove, bot

ScreenW = 480
ScreenH = 808
difficulty = 0
DeskWidth = 20
DeskLen = 100
XSpeed = 2
YSpeed = 2
Score = [0,0]
Ball = [100,100]
BallRadius = 10
Player = [(ScreenW - DeskLen)/2, ScreenH - DeskWidth]
Bot = [(ScreenW - DeskLen)/2,0]
PSpeed = 5
BSpeed = 5
i  = 0
dt = 1
vector = 0
Bounses = 0
turn = 1
goal = 0

pygame.init()

f1 = pygame.font.Font('fonts/HomeVideo-Regular.otf', 48)
screen = pygame.display.set_mode((ScreenW, ScreenH))
clock = pygame.time.Clock()

def render(Ball, Bot, Player, DeskWidth,DeskLen  ):
     screen.fill("black")
     pygame.draw.line(screen, "white", (0, (ScreenH-20)/2), (ScreenW, (ScreenH-20)/2))
     pygame.draw.circle(screen, "white", Ball, BallRadius)
     pygame.draw.rect(screen, "white", (Player[0], Player[1], DeskLen, DeskWidth))
     pygame.draw.rect(screen, "white", (Bot[0], Bot[1], DeskLen, DeskWidth))
     score1 = f1.render(str(Score[1]), True, (180, 180, 180))
     score2 = f1.render(str(Score[0]), True, (180, 180, 180))
     screen.blit(score1, (ScreenW/2-20, ScreenH/4-20))
     screen.blit(score2, (ScreenW/2-20, 3*ScreenH/4-20))
     pygame.display.flip()
     
while True:
    if Bounses //5 > 0:
        if XSpeed > 0:
            XSpeed += Bounses //5
        elif XSpeed < 0:
            XSpeed -= Bounses //5
        
        if YSpeed > 0:
            YSpeed += Bounses //5
        elif YSpeed < 0:
            YSpeed -= Bounses //5
        Bounses = 0
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os.abort()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Player[0] -= PSpeed
    if keys[pygame.K_RIGHT]:
        Player[0] += PSpeed
    Bot, i, dt, vector = bot.botBrains(difficulty, Ball, Bot, DeskLen, BSpeed, i, dt, vector)
    XSpeed, YSpeed, Score, goal, Bounses, turn  = ballMove.move(ScreenW, ScreenH, DeskWidth, DeskLen, XSpeed, YSpeed, Player, Bot, Score, Ball, BallRadius, Bounses, turn)
    if goal == 1:
        Ball[0] = ScreenW/2//1
        Ball[1] = ScreenH/2//1
        Bounses = 0
        if turn ==1:
            YSpeed = -2
            XSpeed = 2
            turn = 0
        elif turn == 0:
            YSpeed = 2
            XSpeed = 2
            turn =1
        dt = time.time()
        while time.time()-dt <3:
            screen.fill("black")
            Time = f1.render(str(int((time.time()-dt)//1)), True, (180, 180, 180))
            screen.blit(Time, (ScreenW/2-20, ScreenH/2-20))
            pygame.display.flip()
    render(Ball, Bot, Player, DeskWidth, DeskLen)
    clock.tick(60)