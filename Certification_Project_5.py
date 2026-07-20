# Hanoi Tower Problem
def hanoi_solver(n):

    source = list(range(n, 0, -1))
    auxiliary = []
    target = []

    rods = [source, auxiliary, target]

    states = []

    states.append(f"{source} {auxiliary} {target}")

    def move(disks, source, auxiliary, target):

        if disks == 1:
            target.append(source.pop())
            states.append(f"{rods[0]} {rods[1]} {rods[2]}")
            return

        move(disks - 1, source, target, auxiliary)

        target.append(source.pop())
        states.append(f"{rods[0]} {rods[1]} {rods[2]}")

        move(disks - 1, auxiliary, source, target)

    move(n, source, auxiliary, target)

    return "\n".join(states)

print(hanoi_solver(3))
