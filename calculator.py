import math

# input
# รับค่า x,y เป็นจำนวนเต็มเพื่อคำนวณผลรวมของจำนวนเต็มตั้งแต่ x ถึง y (0 ≤ x ≤ y)

x = float(input("x: "))
y = float(input("y: "))

x >= 0
y >= x
n = y-x+1
Sn=(n/2)*(x+y)

# output
# โปรแกรมจะแสดงผลบวกรวมของจำนวนเต็มตั้งแต่ x ถึง y

print("sum is: ", int(Sn) )