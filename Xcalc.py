import math

#
# CalcDist        = Calculate the distance between two X,Y coordinates
# CalcMid         = Calculate the midpoint between two X,Y coordinates
# CalcFullFromMid = Calculate the final point from a mid X,Y coordinate
# ClacTan         = Calculate the Tangent of an angle from the Opposite face and the adjacent face (The hypotenuse isn't a face)
# CalcCos         = Calculate the cosin of an angle from the adjacent and the hypotenuse
# CalcSinMinusCos = Calculate  a  sin - cos or vise versa
# CalcSinPlusCos  = Calculate  a  sin + cos or vise versa
# FindSinOrCos    = Calculate the sin or cos from the opposite one ex Sin -> cos / cos -> sin
# CalcTan2        = Calculate the tangent from the Sin and Cos





def CalcDist(X1, Y1, X2, Y2):
    Dist1 = ((X1 - X2) ** 2) + ((Y1 - Y2) ** 2)
    Distfinal = math.sqrt(Dist1)

    print("no sqrt : ", Dist1, )
    print('sqrt : ', Distfinal, )
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def CalcMid(X1, Y1, X2, Y2):
    Mid1X = ((X1 + X2) / 2)
    Mid1Y = ((Y1 + Y2) / 2)

    print('X : (', Mid1X, ') Y : (', Mid1Y, ')')
    print("-----------------------------")


def CalcFullFromMid(X1, Y1, X2, Y2):
    FinalPoint1X = (X2 - (X1 * 2))*-1
    FinalPoint1Y = (Y2 - (Y1 * 2))*-1

    print('MidX : (', FinalPoint1X, ')')
    print('MidY : (', FinalPoint1Y, ')')

    ########## X 1 IS THE MID POINT AND Y 1 IS THE MID POINT ########


def CalcTan(OPPOSITE, adjacent):

    Tan1 = (OPPOSITE/adjacent)
    print('Tan :',Tan1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def CalcCos(adjacent, hypotenuse):

    Cos1 = (adjacent/hypotenuse)
    print('Cos :',Cos1,)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def CalcSinMinusCos(sin, cos):

    f1 = (90-cos)

    Answer1 = (f1-sin)
    if (sin == cos):
        print('1')
    else:
        print('Answer:', Answer1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def CalcSinPlusCos(sin, cos):

    Answer1 = ((90-cos)+sin)
    print('Answer:',Answer1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def FindSinOrCos(Known):

    cosix = (90-Known)
    print('Inverse',cosix)


def CalcTan2(Sin, cos):

    answer = (Sin/cos)
    print('tan :',answer)

def CalcTendency(X1, Y1, X2, Y2):
    Tendency = (Y2-Y1)/(X2-X1)
    print('mid:',Tendency)


def CalcR(X1, Y1, number):

    answer = math.sqrt((X1**2)+(Y1**2)-number)
    print('Half:',answer)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


