import matplotlib.pyplot as plt

class Vector:
    """A class to represent Euclidean vectors"""

    def __init__(self, *numbers):
        # error checking
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise TypeError(f"{number} is not a valid number.")
        if len(numbers) <= 0:
            raise ValueError("Vector can't be empty.")

        self._numbers = tuple(float(number) for number in numbers)

    @property
    def numbers(self):
        return self._numbers

    @staticmethod
    def validate2d(instance):
        if not len(instance) == 2:
            raise ValueError("Vector is not 2d")
        return True
        
    def __add__(self, other):
        if self.validate_vector(other):
            numbers = (a+b for a, b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    def __sub__(self, other):
        if self.validate_vector(other):
            numbers = (a-b for a, b in zip(self.numbers, other.numbers))
            return Vector(*numbers)
        
    def __mul__(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Value must be a scalar (int or float).")
        numbers = (value*a for a in self.numbers)
        return Vector(*numbers)
    
    def __rmul__(self, value):
        return self*value

    def __len__(self):
        return len(self.numbers)

    def validate_vector(self, other):
        if not isinstance(other, Vector):
            raise ValueError(f"{other} is not a Vector")
        if len(self) != len(other):
            raise TypeError(f"Dimensions of vectors not equal: {len(other)} != {len(self)}")
        return True

    def __abs__(self):
        """Returns the Euclidian norm of a Vector, aka the L2-norm"""
        return sum(a**2 for a in self.numbers) ** .5
    
    def __repr__(self):
        return f"Vector{self.numbers}"

    def __getitem__(self, index):
        return self.numbers[index]
    
    def __eq__(self, other):
        if not self.validate_vector(other):
            return False
        
        for v1, v2 in zip(self.numbers, other.numbers):
            if v1 != v2:
                return False
        
        return True
    
    @staticmethod
    def plot(*vectors):
        X, Y = [], []
        for v in vectors:
            if Vector.validate2d(v):
                X.append(v[0])
                Y.append(v[1])
            
        originX = originY = tuple(0 for _ in range(len(X)))
        plt.quiver(originX, originY, X, Y, angles='xy', scale_units='xy', scale=1)
        plt.xlim(-2, 10)
        plt.ylim(-2, 10)
        plt.grid()
        plt.show()

def test_function():
    a = Vector(1,2)
    b = Vector(3,4)
    Vector.plot(a, b)

if __name__ == '__main__':
    test_function()
    