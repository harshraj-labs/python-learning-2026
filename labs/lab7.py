# Bisection Method
def square_root_bisection(value,tolerance=1e-7,iteration=50):
    if value<0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if value==0 or value==1:
        print(f"The square root of {value} is {value}")
        return value
    else:
        low = 0
        if value<1:
            high = 1
        else:
            high = value
        for i in range(iteration):
            middle = (low+high) /2
            if middle * middle < value:
                low = middle
            else:
                high = middle
            if abs(high-low)<=tolerance:
                print(f"The square root of {value} is approximately {middle}")
                return middle
        print(f"Failed to converge within {iteration} iterations")
        return None
    


print(square_root_bisection(0.001))
