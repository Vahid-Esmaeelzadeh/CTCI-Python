#region Question 8.6 (Hanoi Towers)
def moveDisks(n, origin, destination, buffer):
    if n <= 0:
        return
    moveDisks(n-1, origin,  buffer, destination)
    moveTop(origin, destination)
    moveDisks(n-1, buffer, destination, origin)


def moveTop(origin, destination):
    print("moving disk from ", origin, " to ", destination)

moveDisks(4, 'A', 'C', 'B')
#endregion
