from fastapi import FastAPI, Depends, Query, Path
from typing import List, Dict, Any
import time

from review_generator import ReviewGenerator, LRUCache
from .dependencies import rate_limiter

app = FastAPI(
    title="Custom Review Generator API",
    description="A high-performance API for generating deterministic product reviews.",
    version="1.0.0"
)

# Initialize our custom LRU Cache to hold up to 1000 generated review sets
review_cache = LRUCache(capacity=1000)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Custom Review Generator API. Visit /docs for the API documentation."}

@app.get(
    "/reviews/{product_id}", 
    dependencies=[Depends(rate_limiter)],
    summary="Get reviews for a product",
    response_model=Dict[str, Any]
)
def get_reviews(
    product_id: str = Path(..., description="The unique identifier for the product"),
    count: int = Query(4, ge=1, le=20, description="Number of reviews to generate (1-20)")
):
    """
    Retrieves deterministic reviews for a given product ID.
    Utilizes an LRU Cache to avoid regenerating reviews that were recently requested.
    """
    cache_key = f"{product_id}_{count}"
    
    # 1. Check Cache
    cached_reviews = review_cache.get(cache_key)
    if cached_reviews:
        return {
            "source": "cache",
            "product_id": product_id,
            "count": count,
            "average_rating": ReviewGenerator.average_rating(cached_reviews),
            "reviews": [r.to_dict() for r in cached_reviews]
        }

    # 2. Generate if not in cache (Simulate some compute time for realism if desired, but here it's fast)
    generated_reviews = ReviewGenerator.generate(product_id, count=count)
    
    # 3. Store in Cache
    review_cache.put(cache_key, generated_reviews)
    
    return {
        "source": "generator",
        "product_id": product_id,
        "count": count,
        "average_rating": ReviewGenerator.average_rating(generated_reviews),
        "reviews": [r.to_dict() for r in generated_reviews]
    }

@app.get("/system/cache/stats")
def get_cache_stats():
    """Returns the current number of items in the LRU Cache."""
    return {
        "capacity": review_cache.capacity,
        "current_size": len(review_cache.cache)
    }
