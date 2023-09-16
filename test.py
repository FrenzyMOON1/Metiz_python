def number(lines):
    for i, j in enumerate(lines, start=1):
        a = [f"{i}: {j}"]
        print(a)


number(["a", "b", "c"])
