# Custom Review Generator - API & Caching Engine

A high-performance, robust backend engine for generating pseudo-random yet completely **deterministic** product reviews. 

This project is built using Python and FastAPI, focusing on practical backend architecture, system design, and algorithms. It demonstrates how to serve computed data via a REST API while optimizing performance using a custom-built caching layer.

## Architectural Highlights

1. **Deterministic Generation (Math)**: 
   - Uses an **FNV-1a hash** to convert a string Product ID into a 32-bit seed.
   - Uses a **Linear Congruential Generator (LCG)** to produce deterministic pseudo-random sequences to pick names and review texts.
2. **FastAPI Backend (Web Architecture)**: 
   - Asynchronous RESTful API for generating and retrieving reviews.
   - Includes data validation and automatic interactive documentation (Swagger UI).
3. **Custom LRU Cache (Algorithms & Data Structures)**:
   - A from-scratch implementation of a **Least Recently Used (LRU) Cache** using a Hash Map and Doubly Linked List.
   - Achieves O(1) time complexity for reads and writes, preventing the engine from wastefully recalculating reviews for frequently visited products.
4. **Token Bucket Rate Limiter (Security)**:
   - Custom dependency injection to prevent API abuse by limiting request bursts per IP address.

## Project Structure

```
├── api/                          # FastAPI Web Application
│   ├── main.py                   # API Endpoints & App definition
│   └── dependencies.py           # Rate Limiter & Dependencies
├── review_generator/             # Core Engine Package
│   ├── engine.py                 # Math (FNV-1a Hash, LCG)
│   ├── cache.py                  # Custom LRU Cache Algorithm
│   ├── generator.py              # Review orchestration
│   ├── data.py                   # String pools
│   └── models.py                 # Review Data models
├── cli.py                        # Legacy CLI tool
├── requirements.txt              # Project dependencies
└── tests/                        # Comprehensive Test Suites
    ├── test_api.py               # API & Rate Limit testing
    ├── test_cache.py             # LRU Cache eviction testing
    ├── test_engine.py            # Math testing
    └── test_generator.py
```

## Installation

Ensure you have Python 3.7+ installed.

```bash
git clone <your-repo-url>
cd "Custom Review Generator"
pip install -r requirements.txt
```

## Running the API

Start the FastAPI development server:

```bash
uvicorn api.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Endpoints

- **`GET /docs`**: Interactive Swagger UI documentation.
- **`GET /reviews/{product_id}?count=4`**: Generates (or retrieves from cache) reviews for a specific product.
- **`GET /system/cache/stats`**: View current cache utilization.

## Running Tests

To run the unit tests and verify the deterministic properties and cache evictions:

```bash
pytest tests/
```
