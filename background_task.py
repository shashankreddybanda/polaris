import time

def backgroundTask(n):

    delay = 2
    
    print("task running")
    print(f"simulating {delay} seconds delay")

    time.sleep(delay)

    print(len(n))
    print("'''task complete'''")
    return len(n)