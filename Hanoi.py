def Hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk from {source} to {target}")
        return
    Hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk from {source} to {target}")
    Hanoi(n - 1, auxiliary, source, target)


# Example usage
Hanoi(5, 'A', 'B', 'C')