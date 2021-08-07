import math

"""
A sample class with various math operations. 
"""


class MathOperations:
    def __init__(self, n1, n2):
        self.a = n1
        self.b = n2

    def get_sum(self):
        return self.a + self.b

    def get_sub(self):
        return self.a - self.b

    def get_sub_abs(self):
        return abs(self.a - self.b)

    def get_mul(self):
        return self.a * self.b

    def get_div(self):
        return self.a / self.b

    def get_div_floor(self):
        return math.floor(self.a / self.b)

    def get_div_ceil(self):
        return math.ceil(self.a / self.b)

    def get_mod(self):
        return self.a % self.b

    def get_max(self):
        return max(self.a, self.b)

    def get_min(self):
        return min(self.a, self.b)

    def get_sqr(self):
        return self.a ** self.b

    def get_pi(self):
        return math.pi


if __name__ == "__main__":
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    math_operations = MathOperations(a, b)
    print(f"Sum of {a} and {b} is:", math_operations.get_sum())
    print(f"Sub of {a} and {b} is:", math_operations.get_sub())
    print(f"Absolute Sub of {a} and {b} is:", math_operations.get_sub_abs())
    print(f"Mul of {a} and {b} is:", math_operations.get_mul())
    print(f"Div of {a} and {b} is:", "{:.2f}".format(math_operations.get_div()))
    print(f"Floor of Div of {a} and {b} is:", math_operations.get_div_floor())
    print(f"Ceil of Div of {a} and {b} is:", math_operations.get_div_ceil())
    print(f"Mod of {a} and {b} is:", math_operations.get_mod())
    print(f"Max of {a} and {b} is:", math_operations.get_max())
    print(f"Min of {a} and {b} is:", math_operations.get_min())
    print(f"Square of {a} and {b} is:", math_operations.get_sqr())
    print("Pi value is", math_operations.get_pi())
