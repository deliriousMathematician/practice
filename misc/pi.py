import numpy as np, math as m

n = int(input("Enter number of accurate decimal places required: "))
thrown_in_circle = 0
total_throws = 0
pi = 0

def dart():
    coords = np.random.random(2)
    x = coords[0]
    y = coords[1]
    if x * x + y * y < 1:
        return 1
    else:
        return 0
while round(m.pi, n+1) != round(pi, n+1) :
    thrown_in_circle += dart()
    total_throws += 1
    pi = 4 * (thrown_in_circle/total_throws)
print(pi)
print(f"Total iterations: {total_throws}")

