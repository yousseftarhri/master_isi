def dichotomy(f, a, b, epsilon):
    """
    Implements the dichotomy (bisection) method for finding the root of a function.

    Parameters:
    f (function): The function for which we are finding the root.
    a (float): The starting point of the interval.
    b (float): The ending point of the interval.
    epsilon (float): The tolerance for convergence; the algorithm stops when the interval width is less than epsilon.

    Returns :
    float: The estimated root of the function.
    """
    while b - a > epsilon:
        m = (a + b) / 2
        if f(a) * f(m) > 0:
            a = m
        else:
            b = m

    return (a + b) / 2
