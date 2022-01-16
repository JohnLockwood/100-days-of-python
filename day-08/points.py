# A Python file where I experiment with turning our random walk logic into a simple function
import random
import time


def get_random_points(num_points: int, volatility:int=3, start_y:int= 50, seed:int=None):
    """Return a random walk consisting of num_points, with the given volatilitystarting y coordinate"""
    assert volatility > 0, "Volatility must be a postive number"
    if not seed:
        seed = time.time()
        
    x = [i for i in range(0, num_points)]

    y = []
    for _ in range(0, num_points):
        start_y = start_y + random.randint(-volatility,volatility)
        y.append(start_y)
    
    return x,y