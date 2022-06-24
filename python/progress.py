import math

def progress(progress, total):
    percent = 100 * (progress/float(total))
    bar = "\u2593" * int(percent) + "\u2591" *(100- int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")

numbers = [x * 1 for x in range(0, 10000)]
results = []
progress(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress(i+1, len(numbers))