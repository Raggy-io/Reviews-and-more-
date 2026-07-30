# Just exploring: A Custom Review Generator API

Hey there! 👋 This is just a little side project I've been working on to explore some backend concepts. I wanted to see if I could build a review generator that doesn't rely on expensive AI APIs or a clunky database, but instead uses some cool math to generate reviews deterministically. 

Basically, the idea is that if you put the same product ID in, you always get the exact same reviews out. It's pretty fun!

## What I was trying out

I mostly used this to practice and explore a few different things:

1. **Math instead of AI**: I used an FNV-1a hash and a Linear Congruential Generator (LCG) to make the pseudo-randomness. It sounds complicated, but it's basically just a fast way to map a string to a predictable sequence of numbers. 
2. **FastAPI**: I wanted to play around with FastAPI since everyone seems to be using it these days. It was super quick to set up the endpoints.
3. **Writing an LRU Cache from scratch**: Instead of just using Python's built-in `@lru_cache`, I thought it would be a cool challenge to build my own using a Doubly Linked List and a Hash Map. It saves the server from recalculating reviews if the same product is requested back-to-back.
4. **Rate Limiting**: I added a quick Token Bucket rate limiter just to see how dependency injection works in FastAPI and keep the API from being spammed.

## What's inside

- `api/` - This is where the FastAPI app lives.
- `review_generator/` - The actual core logic. The math, the cache, and the data pools are all in here.
- `tests/` - I wrote a bunch of unit tests (using `pytest`) to make sure my custom cache actually evicts things correctly and that the math is actually deterministic.

## How to run it

If you want to mess around with it, feel free to clone it. You'll need Python installed.

1. Install the stuff:
   ```bash
   pip install -r requirements.txt
   ```

2. Spin up the server:
   ```bash
   uvicorn api.main:app --reload
   ```

3. Open up your browser and go to `http://127.0.0.1:8000/docs`. FastAPI automatically makes this cool Swagger UI where you can test the endpoints right in the browser. 

You can also run the tests if you want to see them pass:
```bash
pytest tests/
```

Anyway, that's pretty much it! Just a fun weekend-style project exploring FastAPI and some data structures. Let me know if you break it! 😅
