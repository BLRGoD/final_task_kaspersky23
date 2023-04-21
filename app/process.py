import time
import random


def proc():
    while True:
        r = random.randint(60, 120)
        print("Process is running...")
        print("Next iteration in " + str(r) + " sec")
        time.sleep(r)