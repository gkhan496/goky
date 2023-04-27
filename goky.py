import requests
from collections.abc import MutableMapping
import threading
import queue
import urllib3
import ctypes
import argparse


ctypes.windll.msvcrt._setmaxstdio(2048)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


parser = argparse.ArgumentParser()
parser.add_argument('--threads', dest='threads', help='Number of threads (Default: 50)', default=50)
parser.add_argument('--pure', dest='pure', help='Pure Response URL (Default: False)', default = False)
parser.add_argument('--timeout', dest='timeout', help='Timeout For Requests (Default: 4)', default = 4)
parser.add_argument('--wordlist', dest='wordlist', help='Wordlist for fuzzing (Default: wordlist/wordlist.txt)', default='wordlist/wordlist.txt')
parser.add_argument('--list', dest='list', help='List of URLs (Default: input.txt)', default='input.txt')
parser.add_argument('--status', dest='list', help='List of URLs (Default: 200)', default = 200)


args = parser.parse_args()
url_queue = queue.Queue()
num_threads = args.threads
threads = []
unique_urls = set()


def make_request(full_url):
    f = open("output.txt", "a")

    try:

        response = requests.get(full_url, timeout= args.timeout, verify=False)
        response_size = int(response.headers.get("content-length", 0))
        if response_size != 0:
            if response.status_code == args.status:
                f.write(str(response_size) + '-'+full_url + '\n')

    except requests.exceptions.Timeout:
        result = f"Timeout - URL: {full_url}"
        
    except requests.exceptions.RequestException as e:
        result = f"Error - URL: {full_url} - Exception: {e}"
    f.close()

with open(args.list, 'r') as f:
    urls = [url.strip() for url in f.readlines()]

for url in urls:

    parts = url.split('/')
    parts = [part for part in parts if part]
    new_urls = ['/'.join(parts[:i]) + '/' for i in range(2, len(parts))]
    new_urls = [new_url.replace('http:/', 'http://') for new_url in new_urls]
    new_urls = [new_url.replace('https:/', 'https://') for new_url in new_urls]
    unique_urls.update(set(new_urls).difference(set(urls)))

sorted_urls = sorted(unique_urls)


with open('separated.txt', 'w') as f:
    for sorted_url in sorted_urls:
        f.write(sorted_url + '\n')


with open('separated.txt', 'r') as f:
    base_url = f.readline().strip()
    f.close()

with open('wordlist/wordlist.txt', 'r') as f:
    wordlist = [word.strip() for word in f.readlines()]
    f.close()

with open('separated.txt', 'r') as f:
    next(f)
    urls = [url.strip() for url in f.readlines()]
    f.close()

for url in urls:

    for word in wordlist:
        full_url =  url + word
        url_queue.put(full_url)


while not url_queue.empty():
    for i in range(num_threads):
        if not url_queue.empty():
            full_url = url_queue.get()
            thread = threading.Thread(target=make_request, args=(full_url,))
            thread.start()
            threads.append(thread)

for thread in threads:
    thread.join()

with open("output.txt", "r") as f:
    lines = f.readlines()
    f.close()

sorted_lines = sorted(lines, key=lambda line: int(line.split("-")[0]))

with open("responses/all.txt", "w") as f:
    f.writelines(sorted_lines)
    f.close()

with open('responses/all.txt', 'r') as f:
    lines = f.readlines()

numbers = {}
for line in lines:
    parts = line.strip().split('-')
    number = int(parts[0])
    
    chars = parts[1] + parts[2]

    if number not in numbers or chars < numbers[number]:
        numbers[number] = chars

unique_numbers = [(number, chars) for number, chars in numbers.items()]

unique_numbers.sort()

with open('responses/unique.txt', 'w') as f:
    for number, chars in unique_numbers:
        f.write('[Size: ' + str(number) + '] ' + chars  + '\n')

if args.pure:
    with open('responses/pure.txt', 'w') as f:
        for number, chars in unique_numbers:
            f.write(chars + '\n')

