import requests
import time

def increase_network_usage(url, num_requests):
    for _ in range(num_requests):
        response = requests.get(url)
        print(f"Status code: {response.status_code}")
        time.sleep(0.1)  # Sleep for a short duration to avoid overwhelming the server

if __name__ == "__main__":
    target_url = "https://example.com"
    num_requests_to_make = 100

    increase_network_usage(target_url, num_requests_to_make)
