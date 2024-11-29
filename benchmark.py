import requests
import time

# API Endpoints
PERSISTENT_MODEL_URL = "http://0.0.0.0:8001/predict"
ON_DEMAND_MODEL_URL = "http://0.0.0.0:8001/predict-on-demand"

# Sample input
payload = {"text": "This is a performance test."}

# Function to measure time taken for a single request
def measure_time(url):
    start_time = time.time()
    response = requests.post(url, json=payload)
    end_time = time.time()
    return end_time - start_time, response.json()

# Measure response times for both scenarios
print("Testing Persistent Model...")
persistent_times = [measure_time(PERSISTENT_MODEL_URL)[0] for _ in range(10)]

print("Testing On-Demand Model...")
on_demand_times = [measure_time(ON_DEMAND_MODEL_URL)[0] for _ in range(10)]

# Print average times
print(f"Persistent Model Avg Time: {sum(persistent_times) / len(persistent_times):.4f} seconds")
print(f"On-Demand Model Avg Time: {sum(on_demand_times) / len(on_demand_times):.4f} seconds")
