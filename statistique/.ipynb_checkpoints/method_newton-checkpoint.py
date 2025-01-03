def newton(f, f_prime, x0, epsilon):
    """
    Implements Newton's method for finding the root of a function.

    Parameters:
    f (function): The function for which we are finding the root.
    f_prime (function): The derivative of the function f.
    x0 (float): Initial guess for the root.
    epsilon (float): Convergence criterion; the algorithm stops when successive
                     estimates differ by less than epsilon.

    Returns:
    float: The estimated root of the function.
    """
    x1 = x0 - f(x0) / f_prime(x0)

    while abs(x1 - x0) > epsilon:
        x2 = x1 - f(x1) / f_prime(x1)
        x0 = x1
        x1 = x2

    return x1