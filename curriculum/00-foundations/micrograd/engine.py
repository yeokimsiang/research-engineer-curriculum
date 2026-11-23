"""A tiny scalar autograd engine.

Step 2 (this version): Value wraps a number and remembers how it was made.
Every arithmetic op returns a new Value whose `_prev` holds the inputs and whose
`_op` names the operation. Doing ordinary maths with Values therefore builds a
graph (a DAG) of the whole computation as a side effect.

Backprop (step 3) will walk that graph backwards. It isn't written yet.
"""


class Value:
    def __init__(self, data, _children=(), _op="", label=""):
        self.data = data
        self.grad = 0.0  # d(final output)/d(this value); 0 means "no effect yet"
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data + other.data, (self, other), "+")

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data * other.data, (self, other), "*")


def print_graph(v, indent=0):
    """Print the graph that produced v, output first, inputs indented below."""
    name = v.label or "?"
    op = f" <- {v._op}" if v._op else ""
    print("  " * indent + f"{name} = {v.data}{op}")
    for child in v._prev:
        print_graph(child, indent + 1)


if __name__ == "__main__":
    a = Value(2.0, label="a")
    b = Value(-3.0, label="b")
    c = Value(10.0, label="c")
    e = a * b; e.label = "e"
    d = e + c; d.label = "d"
    f = Value(-2.0, label="f")
    L = d * f; L.label = "L"
    print_graph(L)
