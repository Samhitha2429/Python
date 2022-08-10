def greet(name="Sam", message="Hi ?"):
    return f"Hello {name}, {message}"


def sub(a=2,b=5):
    return f"{a} *{b} ={a- b}"


def performOperation(name, operation, values=[5, 6]):
    return f"{greet(name)} .{name} is performing {operation(values[0],values[1])}"


print(performOperation("Sam", sub))
