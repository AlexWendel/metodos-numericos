import math

def calc(x1, fx1, x0, fx0):
  return x1 - ( (fx1 * (x0 - x1)) / (fx0 - fx1))

def calc_func(x):
  return math.sin(x) - pow(x, 2)

def calc_err(x1, x0):
  return abs((x1-x0) / x0)
  
error = 10000
x0 = math.pi/2
x1 = math.pi/4

while error > 0.001:
  fx1 = calc_func(x1)
  fx0 = calc_func(x0)

  print("=============================")
  print(f"X0: {x0}")
  print(f"X1: {x1}")  
  print(f"FX0: {fx0}")
  print(f"FX1: {fx1}")
  next_x = calc(x1, fx1, x0, fx0)
  error = calc_err(x1, x0)
  print(f"Next X: {next_x}")
  print(f"Erro: {error}")

  x0 = x1
  x1 = next_x