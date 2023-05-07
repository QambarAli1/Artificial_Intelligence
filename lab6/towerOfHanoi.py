# TOWER OF HONOI
steps = 0
def towerOfHonoi(n, source, auxiliary, destination):
    global steps
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        steps += 1
        return

    towerOfHonoi(n-1, source, destination, auxiliary)

    print(f"Move disk {n} from {source} to {destination}")

    steps += 1
    towerOfHonoi(n-1, auxiliary, source, destination)


towerOfHonoi(3, "A", "C", "B")
print("Steps = " , steps)
