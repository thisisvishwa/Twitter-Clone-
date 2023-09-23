```python
import time
from prometheus_client import start_http_server, Summary, Counter, Gauge

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNTER = Counter('requests_total', 'Total requests')
ACTIVE_USERS = Gauge('active_users', 'Number of active users')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

def monitor_performance():
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(1)
        REQUEST_COUNTER.inc()  # Increment by 1

def count_active_users(users):
    ACTIVE_USERS.set(len(users))  # Set to a given value

def fine_tune_system():
    # Placeholder for system fine-tuning logic
    pass
```