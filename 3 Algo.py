n = 4

guess = input("Total points: 1 + 2 + 3 + 4 =")

input("Formula: one calculation. Press enter to run.")

total = n* (n+1)//2
print("  total =", total, "  steps = 1")

input("Loops: adds one student at a time. Press enter to run.")
total = 0
for student in range(1, n+1):
    total += student
print("  total =", total, "  steps =", n)

input("Double Loop: counts every single point. Press enter to run.")
total = 0
steps = 0
for student in range(1, n + 1):
    for point in range(1, student + 1)
        total += 1
        steps += 1
print("  total =", total, "  steps =", steps, "  your guess was:", guess)

input("Double Loop at n = 4 took 10 steps. Watch it grow. Press Enter.")
for n in [10, 100, 1000]
    input("n = " + str(n) + "  Press Enter")
    print("  steps =", n* (n + 1)//2)