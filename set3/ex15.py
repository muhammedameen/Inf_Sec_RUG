import sys

a = 11
N = 167

def addPoints(point1, point2, same):
    if (same):
        #pow(x,n-2,n) = modular inverse
        m = (3 * point1[0]**2 + a) * pow((2 * point1[1]), N-2, N) 
    else:
        m = (point2[1] - point1[1]) * pow((point2[0] - point1[0]), N-2, N) 

    x3 = ( m*m - point1[0] - point2[0] ) % N
    y3 = ( m * (point1[0] - x3) - point1[1] ) % N
    point3 = [x3,y3]
    return point3

def multiplyWithPoint(multiplier,point):
    idxPoints = []
    points = [point]

    #get the points we need to add from binary
    cnt = 0
    while (multiplier != 0):
        if (multiplier % 2): #last bit is 1
            idxPoints.append(cnt)
        cnt += 1
        multiplier >>= 1
    
    #create list of P0+P0, P1+P1 etc. 
    for idx in range(0,cnt):
        points.append(addPoints(points[idx], points[idx], True))
    
    pointFinal = points[idxPoints.pop()]
    for idx in reversed(idxPoints):
        pointFinal = addPoints(pointFinal, points[idx], False)

    print(idxPoints)
    print(points)
    return pointFinal


        

def main():
    point0 = [2,7] #point P0 = (x,y)
    multiplier = 22
    b = ( point0[1]*point0[1] - point0[0]**3 - a*point0[0] ) % N
    print(multiplyWithPoint(multiplier,point0))
    


if __name__ == "__main__":
    main()