x1 = int(input('Enter x1:'))
y1 = int(input('Enter y1:'))
x2 = int(input('Enter x2:'))
y2 = int(input('Enter y2:'))
x = int(input('Enter x:'))
y = int(input('Enter y:'))
def check_points():
    if(x>x1 and x<x2 and y>y1 and y<y2):
        return True
    return False
print(check_points())