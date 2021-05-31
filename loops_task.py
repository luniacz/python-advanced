import time

counter_while = 0
time_while_start = time.time()
while time.time() - time_while_start < 1:
    counter_while += 1

counter_for = 0
time_for_start = time.time()
for i in range(counter_while):
    counter_for += 1
time_for_end = time.time()

print(time_for_end - time_for_start)

