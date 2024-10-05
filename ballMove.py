def move(ScreenW, ScreenH, DeskWidth, DeskLen, XSpeed, YSpeed, Player, Bot, Score, Ball, BallRadius, Bounses, turn):
    goal = 0
    if (Ball[0] - BallRadius <=0 or Ball[0]+ BallRadius >= ScreenW):
        XSpeed = -XSpeed
        Bounses +=1
    elif (Ball[1] - BallRadius <=DeskWidth and Ball[0] + BallRadius>= Bot[0] and Ball[0] - BallRadius <= Bot[0] + DeskLen ) and not turn:
        YSpeed = - YSpeed
        Bounses +=1
        turn = 1
    elif (Ball[1] + BallRadius >= ScreenH - DeskWidth and Ball[0] + BallRadius >=Player[0] and Ball[0] - BallRadius <=Player[0] + DeskLen) and turn: 
        YSpeed = - YSpeed
        Bounses +=1
        turn = 0
    elif Ball[1] - BallRadius <=DeskWidth:
        Score[0] +=1
        goal = 1
    elif Ball[1] + BallRadius >=ScreenH-DeskWidth:
        Score[1] +=1
        goal = 1

    Ball[0] += XSpeed
    Ball[1] += YSpeed

    return XSpeed, YSpeed, Score,goal, Bounses, turn
    
