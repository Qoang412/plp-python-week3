count = 1
total = 0

# BUG 1: The while statement was missing a colon. Added the colon.
# BUG 2: The loop stopped before adding 5. Changed count < 5 to count < 6.
while count < 6:
    total = total + count
    count = count + 1

# BUG 3: total is an integer. Converted it to a string using str().
print("Sum of 1 to 5 is: " + str(total))