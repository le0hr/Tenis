import time

def botBrains(difficulty, Ball,Bot, DeskLen, BSpeed, i, dt, vector):
    if time.time() -dt > difficulty:
        if not (Ball[0] >= Bot[0] and Ball[0]< Bot[0] + DeskLen ) and Bot[0]-Ball[0] < 0:
            vector= 'right'
        elif not (Ball[0] >= Bot[0] and Ball[0]< Bot[0] + DeskLen ) and Bot[0]-Ball[0] > 0:
            vector= 'left'
        dt = time.time()
    if Ball[1] < 404:
        if vector == 'right':
            Bot[0]+=BSpeed
        elif vector == 'left':
            Bot[0]-=BSpeed
    else:
        if Bot[0]-220 < 0:
            Bot[0]+=BSpeed
        elif Bot[0]-220 > 0:
            Bot[0]-=BSpeed
        else: 
            pass

    # else:
    #     if i % 20 == 0:
    #         Bot[0]+=2*BSpeed
    #     elif i % 20  == 10:
    #         Bot[0]-=2* BSpeed
    #     i += 1
    i = 0
    return Bot, i, dt, vector
    