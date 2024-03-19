import math

def calculate_expression(x):
    numerator = math.exp(-3*x) + math.tan(3*x - 3)
    denominator = abs(math.sin(x)) + (math.cos(x) + math.cos(2*x))**(1/4)
    return numerator / denominator if denominator != 0 else 'Ділення на нуль'

x_value = 0.1  #Значення х
p = calculate_expression(x_value)
print(f'p = {p}')