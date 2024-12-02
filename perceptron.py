from typing import List

def dot(a: List[float], b: List[float]) -> float:
    return sum(x * y for x, y in zip(a, b))

def step_function(x: float) -> float:
    return 1.0 if x >= 0 else 0.0

def perceptron_output(weights: List[float], bias: float, x: List[float]) -> float:
    calculation = dot(weights, x) + bias
    return step_function(calculation)

def xor_gate(a: List[float], b: List[float]) -> float:
    and_output = perceptron_output(and_weights, and_bias, a)
    or_output = perceptron_output(or_weights, or_bias, a)
    not_and_output = perceptron_output(not_weights, not_bias, [and_output])
    return perceptron_output([1.0, 1.0], -2.0, [or_output, not_and_output])

# AND Gate
and_weights = [2., 2]
and_bias = -3.

print("AND Gate Outputs:")
print(f"[1, 1] -> {perceptron_output(and_weights, and_bias, [1, 1])}")  
print(f"[0, 1] -> {perceptron_output(and_weights, and_bias, [0, 1])}") 
print(f"[1, 0] -> {perceptron_output(and_weights, and_bias, [1, 0])}")
print(f"[0, 0] -> {perceptron_output(and_weights, and_bias, [0, 0])}")  

# OR Gate
or_weights = [2., 2]
or_bias = -1.

print("\nOR Gate Outputs:")
print(f"[1, 1] -> {perceptron_output(or_weights, or_bias, [1, 1])}")  
print(f"[0, 1] -> {perceptron_output(or_weights, or_bias, [0, 1])}")  
print(f"[1, 0] -> {perceptron_output(or_weights, or_bias, [1, 0])}")
print(f"[0, 0] -> {perceptron_output(or_weights, or_bias, [0, 0])}")  

# NOT Gate
not_weights = [-2.] 
not_bias = 1.       

print("\nNOT Gate Outputs:")
print(f"[0] -> {perceptron_output(not_weights, not_bias, [0])}") 
print(f"[1] -> {perceptron_output(not_weights, not_bias, [1])}")  

print("\nXOR Gate Outputs:")
print(f"[0, 0] -> {xor_gate([0, 0], [0, 0])}")
print(f"[0, 1] -> {xor_gate([0, 1], [0, 1])}")
print(f"[1, 0] -> {xor_gate([1, 0], [1, 0])}")
print(f"[1, 1] -> {xor_gate([1, 1], [1, 1])}")
