"""Step 1: what a derivative is, measured numerically.

The derivative of f at x answers: "if I nudge x by a tiny h, how much does
f(x) move, per unit of nudge?"  That is just rise over run:

    f'(x) ~= (f(x + h) - f(x)) / h      for small h

Backprop computes exactly this quantity for every input at once, analytically.
Everything below is the slow, honest way, which we will use later to check
that our fast backprop is correct.
"""


def f(x):
    return 3 * x**2 - 4 * x + 5


def numerical_derivative(fn, x, h=1e-6):
    return (fn(x + h) - fn(x)) / h


if __name__ == "__main__":
    for x in [3.0, -3.0, 2 / 3]:
        print(f"x={x:+.4f}  f(x)={f(x):8.4f}  slope~={numerical_derivative(f, x):+.4f}")

    # A function of several inputs: d = a*b + c.
    # Nudge one input at a time to get each partial derivative.
    a, b, c = 2.0, -3.0, 10.0
    h = 1e-6
    d = a * b + c
    print(f"\nd = a*b + c = {d}")
    print(f"dd/da ~= {((a + h) * b + c - d) / h:+.4f}")
    print(f"dd/db ~= {(a * (b + h) + c - d) / h:+.4f}")
    print(f"dd/dc ~= {(a * b + (c + h) - d) / h:+.4f}")
