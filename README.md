# Sentiment Analysis API Performance Benchmark (model loaded persistently vs on-demand)

This repository contains a FastAPI application that performs sentiment analysis on text input and benchmarks two different approaches to model loading: persistent and on-demand.  It provides a simple API for sentiment analysis and demonstrates the performance differences between loading the model once at startup (persistent) versus loading it for each request (on-demand).

## Relevance

This project is designed to explore the performance trade-offs of different model loading strategies in a real-world API scenario.  Understanding these trade-offs is crucial for optimizing API response times and resource utilization, especially when dealing with large language models.  The benchmark helps developers choose the best strategy for their specific use case.

## Setup and Running

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
   (A `requirements.txt` file containing `fastapi`, `uvicorn`, `pydantic`, `transformers`, and `requests` is implicitly required to run this code).

2. **Run the FastAPI Server:**

   ```bash
   python main.py
   ```

   This will start the server on `http://0.0.0.0:8001`.

3. **Run the Benchmark Script:**

   ```bash
   python benchmark.py
   ```

   This script will send 10 requests to both the `/predict` (persistent model) and `/predict-on-demand` endpoints and measure the average response times. The output will be printed to the console.

## API Endpoints

* **`/predict`**: Uses the persistently loaded sentiment analysis model.  This endpoint is expected to be faster after the initial model loading.
* **`/predict-on-demand`**: Loads the sentiment analysis model for each request. This endpoint showcases the overhead of loading the model repeatedly.


## Key Files

* `main.py`: Contains the FastAPI application logic, including model loading and prediction endpoints.
* `benchmark.py`:  A script to benchmark the performance of the two API endpoints.


## Expected Output

The `benchmark.py` script will output the average response times for both the persistent and on-demand models, allowing for a direct comparison of their performance.  You should observe that the persistent model has a longer initial response time due to the model loading during server startup but subsequent requests have lower latency. Conversely, the on-demand model has similar latency for all requests. For Example:

```
Testing Persistent Model...
Testing On-Demand Model...
Persistent Model Avg Time: 0.0123 seconds
On-Demand Model Avg Time: 2.3456 seconds
```
