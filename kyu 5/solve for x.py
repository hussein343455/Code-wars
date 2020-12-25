def solve_for_x(equation):
  left_side,right_side  = equation.split('=');
  for x in range(-1000, 1000):
    if eval(left_side) == eval(right_side):
      return x

print(solve_for_x('3 * x - 5 - 3 + x = 20'))
