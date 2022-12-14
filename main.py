import time, sys, math
# Variables
A = 0
B = 0
C = 90
a = 0
b = 0
c = 0
showDiagram = False

# Types a string one character at a time
def type_out(string, t):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(t)

# Finds the third side of a triangle from the given sides
def hyp_from_two_sides(a, b):
  c = round(math.sqrt(a**2 + b**2), 4)
  return c

def a_from_b_c(b, c):
  a = round(math.sqrt(c**2 - b**2), 4)
  return a

def b_from_a_c(a, c):
  b = round(math.sqrt(c**2 - a**2), 4)
  return b

# Finds an angle from a side and the hypotenuse
def A_from_b_c(b, c):
  A = round(math.degrees(math.acos(b/ c)), 2)
  return A

def B_from_a_c(a, c):
  B = round(math.degrees(math.asin(a/ c)), 2)
  return B

# Finds a side from an angle and the hypotenuse
def a_from_A_c(A, c):
  a = round(c * math.degrees(math.sin(A)), 2)
  return a

def b_from_A_c(A, c):
  b = round(c * math.degrees(math.cos(A)), 2)
  return b

def a_from_B_c(B, c):
  a = round(c * math.degrees(math.cos(B)), 2)
  return a

def b_from_B_c(B, c):
  b = round(c * math.degrees(math.sin(B)), 2)
  return b

# Finds an angle from two sides
def A_from_a_b(a, b):
  A = round(math.degrees(math.atan(a/b)), 2)
  return A

def B_from_a_b(a, b):
  B = round(math.degrees(math.atan(b/a)), 2)
  return B

# Finds the third angle in the triangle
def A_from_B_C(B):
  A = 180 - B - C
  return A

def B_from_A_C(A):
  B = 90 - A
  return B

# Draws a triangle with labeled values
def draw_triangle_sides(a, b, c):
  print('     |\\')
  print('     | \\')
  print('     |  \\')
  print('     |   \\')
  print(str(round(b, 1)) + ' |    \\ ' + str(c))
  print('     |     \\')
  print('     |      \\')
  print('     --------')
  print('     ' + str(a))

def draw_triangle_angles(A, B):
  print(str(A) + '|\\')
  print('   | \\')
  print('   |  \\')
  print('   |   \\')
  print('   |    \\ ')
  print('   |     \\')
  print('   |      \\')
  print('   --------')
  print(' ' + str(C) + '       ' + str(B))

def draw_full_triangle(a, b, c, A, B, C):
  print(str(A) + '|\\')
  print('    | \\')
  print('    |  \\')
  print('    |   \\')
  print(str(b) + ' |    \\ ' + str(c))
  print('    |     \\')
  print('    |      \\')
  print('    --------')
  print('    ' + str(C) + ' ' + str(a) + ' ' + str(B))


# Explaining right triangles
type_out('Would you like an explanation of the program? y/n: ', 0.02)
explain = input('')
if explain == 'y':
  type_out('A right triangle is a triangle with one 90 degree angle.', 0.02)
  print()
  type_out('For this program, the 90 degree angle will be denoted by variable C.', 0.02)
  print()
  type_out('The other two angles will be denoted by variables A and B.', 0.02)
  print()
  type_out('The three angles will always add up to 180 degrees.', 0.02)
  print()
  type_out('As for the sides, they will be denoted by variables a, b, and c.', 0.02)
  print()
  type_out('Capitalization matters here.', 0.02)
  print()
  type_out('Side c is the square root of the sum of side a and side b squared.', 0.02)
  print()
  type_out('Sides a and b can be found using the trigonomic functions sin, cos, and tan.', 0.02)
  print()
  type_out('If no other angle measure is given by the user,', 0.02)
  print()
  type_out('the program will find them using the inverse functions of sin, cos, and tan.', 0.02)
  time.sleep(1)
  print()
  print()

type_out('Would you like to see a diagram with your answer? y/n: ', 0.02)
answer = input('')
if answer == 'y':
  showDiagram = True

# Asking what kind of function to do
print()
print('1. Finding the hypotenuse from two sides')
print('2. Finding side a from sides b and c')
print('3. Finding side b from sides a and c')
print('4. Finding angle A from sides b and c')
print('5. Finding angle B from sides a and c')
print('6. Finding side a from angle A and side c')
print('7. Finding side b from angle A and side c')
print('8. Finding side a from angle B and side c')
print('9. Finding side b from angle B and side c')
print('10. Finding angle A from sides a and b')
print('11. Finding angle B from sides a and b')
print('12. Finding angle A from angles B and C')
print('13. Finding angle B from angles A and C')
time.sleep(1)
print()

type_out('What kind of problem do you have? ', 0.02)
type = int(input(''))
if type == 1:
  a = float(input('Side a: '))
  b = float(input('Side b: '))
  print('Side c is ' + str(hyp_from_two_sides(a, b)))
  print()
  if showDiagram == True:
    draw_triangle_sides(a, b, hyp_from_two_sides(a, b))

if type == 2:
  b = float(input('Side b: '))
  c = float(input('Side c: '))
  print('Side a: ' + str(a_from_b_c(b, c)))
  if showDiagram == True:
    draw_triangle_sides(a_from_b_c(b, c), b, c)

if type == 3:
  a = float(input('Side a: '))
  c = float(input('Side c: '))
  print('Side b: ' + str(b_from_a_c(a, c)))
  if showDiagram == True:
    draw_triangle_sides(a, b_from_a_c(a, c), c)

if type == 4:
  b = float(input('Side b: '))
  c = float(input('Side c: '))
  print('Angle A: ' + str(A_from_b_c(b, c)) + ' degrees')
  if showDiagram == True:
    a = 1

if type == 5:
  a = float(input('Side a: '))
  c = float(input('Side c: '))
  print('Angle B: ' + str(B_from_a_c(a, c)))
  if showDiagram == True:
    a = 1

if type == 6:
  A = float(input('Angle A: '))
  c = float(input('Side c: '))
  print('Side a: ' + str(a_from_A_c(A, c)))
  if showDiagram == True:
    a = 1

if type == 7:
  A = float(input('Angle A: '))
  c = float(input('Side c: '))
  print('Side b: ' + str(b_from_A_c(A, c)))
  if showDiagram == True:
    a = 1

if type == 8:
  B = float(input('Angle B: '))
  c = float(input('Side c: '))
  print('Side a: ' + str(a_from_B_c(B, c)))
  if showDiagram == True:
    a = 1

if type == 9:
  B = float(input('Angle B: '))
  c = float(input('Side c: '))
  print('Side b: ' + str(b_from_B_c(B, c)))
  if showDiagram == True:
    a = 1

if type == 10:
  a = float(input('Side a: '))
  b = float(input('Side b: '))
  print('Angle A: ' + str(A_from_a_b(a, b)))
  if showDiagram == True:
    a = 1

if type == 11:
  a = float(input('Side a: '))
  b = float(input('Side b: '))
  print('Angle B: ' + str(B_from_a_b(a, b)))
  if showDiagram == True:
    a = 1

if type == 12:
  B = float(input('Angle B: '))
  print('Angle A: ' + str(A_from_B_C(B)) + ' degrees')
  if showDiagram == True:
    draw_triangle_angles(A_from_B_C(B), B)

if type == 13:
  A = float(input('Angle A: '))
  print('Angle B: ' + str(B_from_A_C(A)) + ' degrees')
  if showDiagram == True:
    draw_triangle_angles(A, B_from_A_C(A))