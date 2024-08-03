
import sys

delta = 10**(-14)
try:
    circle_param = sys.argv[1]   #= input()
    points = sys.argv[2]        #= input()

    with open(circle_param,"r") as f:
        x, y = map(int, f.readline()[:-1].split())
        r = int(f.readline())
        
    with open(points, "r") as f:
        for s in f:
            x1, y1 = map(int, s.split())
            
            c = (x - x1)**2 + (y - y1)**2
            if (r**2 - delta) <= c <= (r**2 + delta):
                print("0")
            elif c> r**2:
                print("2")
            else:
                print("1")
        
except IndexError:
    print("Input files names!")
except FileNotFoundError:
    print("Can not open file!")
