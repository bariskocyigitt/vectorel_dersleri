import os, time
# os.mkdir("deneme77")

for a in range(10,20):
    os.mkdir(f"deneme{a}")
    time.sleep(1)
    os.rmdir(f"deneme{a}")
    time.sleep(1)