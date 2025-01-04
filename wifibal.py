import requests

# Router URL
dashboard_url = "http://192.168.254.254"

# Default login credentials
username = "admin"
password = "pw"

# Start a session to persist cookies
session = requests.Session()

# Step 1: Test login page
print("Testing login page...")
login_page = session.get(dashboard_url, timeout=10)
if login_page.status_code == 200:
    print("Login page accessed successfully.")
else:
    print(f"Failed to access login page. Status code: {login_page.status_code}")
    exit()

# Step 2: Test login
print("\nAttempting login...")
login_data = {"username": username, "password": password}
login_response = session.post(f"{dashboard_url}/cgi-bin/luci", data=login_data, timeout=10)
if login_response.status_code == 200:
    print("Login successful!")
else:
    print("Login failed.")
    print(f"Status Code: {login_response.status_code}")
    print(login_response.text[:500])  # Debug response
    exit()

# Step 3: Explore available endpoints
print("\nExploring endpoints...")
test_endpoints = [
    "/api/balance",
    "/api/status",
    "/api/account",
    "/api/sms",
    "/cgi-bin/sms",
    "/cgi-bin/balance",
    "/api/usage"
]

for endpoint in test_endpoints:
    url = f"{dashboard_url}{endpoint}"
    print(f"Testing {url}...")
    try:
        response = session.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.text[:500]}")
        else:
            print("Endpoint not found or inaccessible.")
    except Exception as e:
        print(f"Error testing {url}: {e}")
