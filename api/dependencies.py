import time
from fastapi import HTTPException, Request, status

class TokenBucketRateLimiter:
    """
    A simple Token Bucket rate limiter.
    Allows a burst of `capacity` requests, regenerating `refill_rate` tokens per second.
    """
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.clients = {}  # Map IP to {"tokens": float, "last_refill": float}

    def __call__(self, request: Request):
        client_ip = request.client.host if request.client else "unknown"
        now = time.time()
        
        if client_ip not in self.clients:
            # First time seeing this IP, give them full capacity
            self.clients[client_ip] = {"tokens": self.capacity, "last_refill": now}
            
        client_data = self.clients[client_ip]
        
        # Refill tokens based on time passed
        time_passed = now - client_data["last_refill"]
        client_data["tokens"] = min(
            self.capacity, 
            client_data["tokens"] + time_passed * self.refill_rate
        )
        client_data["last_refill"] = now
        
        # Consume token if available
        if client_data["tokens"] >= 1.0:
            client_data["tokens"] -= 1.0
            return True
        else:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded. Please slow down."
            )

# Create a global rate limiter instance
# E.g., 5 requests max burst, refills 1 request per second
rate_limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1.0)
