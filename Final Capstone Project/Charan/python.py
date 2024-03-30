import requests
import time
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pprint import pprint

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

# Set target URL
target_url = input("Enter the target URL: ")

# Define XSS and SQL injection payloads
xss_payloads_file = input("Enter the path to the XSS payloads file: ")
sql_payloads_file = input("Enter the path to the SQL injection payloads file: ")

# Read payloads from files
with open(xss_payloads_file, "r", encoding='utf-8') as xss_file:
    xss_payloads = [line.strip() for line in xss_file]

with open(sql_payloads_file, "r", encoding='utf-8') as sql_file:
    sql_payloads = [line.strip() for line in sql_file]

def get_all_forms(url):
    soup = bs(s.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {}
    try:
        action = form.attrs.get("action").lower()
    except:
        action = None
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def is_vulnerable(response):
    errors = {
        # MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated",
    }
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False

def send_request_and_analyze_response(payload, method="GET"):
    if method == "GET":
        params = {
            "param": payload,
        }
        url = target_url + "?" + "&".join([f"{k}={v}" for k, v in params.items()])
        response = s.get(url)
    elif method == "POST":
        data = {
            "param": payload,
        }
        url = target_url
        response = s.post(url, data=data)

    return response, url

# Send requests with XSS payloads
print("Testing for XSS vulnerabilities...")
for payload in xss_payloads:
    response, url = send_request_and_analyze_response(payload)
    if response and payload in response.text:
        print(f"[!] XSS vulnerability detected with payload: {payload} in URL: {url}")
    else:
        print(f"[ ] No XSS vulnerability detected with payload: {payload} in URL: {url}")

# Send requests with SQL injection payloads
print("\nTesting for SQL injection vulnerabilities...")
for payload in sql_payloads:
    start_time = time.time()  # Record the start time
    response, url = send_request_and_analyze_response(payload, method="GET")
    end_time = time.time()  # Record the end time

    # Calculate the time taken for the request
    elapsed_time = end_time - start_time

    # Check if the elapsed time is greater than 1 second
    if elapsed_time > 1:
        print(f"[!] SQL injection vulnerability detected with payload: {payload} in URL: {url}")
    else:
        print(f"[ ] No SQL injection vulnerability detected with payload: {payload} in URL: {url}")

# Scan for SQL injection vulnerabilities
print("\nScanning for SQL injection vulnerabilities in forms...")
for c in "\"'":
    new_url = f"{target_url}{c}"
    print("[!] Trying", new_url)

    res = s.get(new_url)
    if is_vulnerable(res):
        print("[+] SQL Injection vulnerability detected, link:", new_url)

forms = get_all_forms(target_url)
print(f"[+] Detected {len(forms)} forms on {target_url}.")
for form in forms:
    form_details = get_form_details(form)
    for c in "\"'":
        data = {}
        for input_tag in form_details["inputs"]:
            if input_tag["value"] or input_tag["type"] == "hidden":
                try:
                    data[input_tag["name"]] = input_tag["value"] + c
                except:
                    pass
            elif input_tag["type"] != "submit":
                data[input_tag["name"]] = f"test{c}"
        url = urljoin(target_url, form_details["action"])
        if form_details["method"] == "post":
            res = s.post(url, data=data)
        elif form_details["method"] == "get":
            res = s.get(url, params=data)
        if is_vulnerable(res):
            print("[+] SQL Injection vulnerability detected, link:", url)
            print("[+] Form:")
            pprint(form_details)