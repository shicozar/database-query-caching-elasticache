import json
import redis
from .config import Config

_redis_client = None

def get_cache_client():
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.Redis(
            host=Config.CACHE_HOST,
            port=Config.CACHE_PORT,
            decode_responses=True,
            ssl=False  # set True if your cache requires TLS
        )
    return _redis_client

def get_cached_product(product_id: int):
    client = get_cache_client()
    key = f"product:{product_id}"
    value = client.get(key)
    if value is None:
        return None
    return json.loads(value)

def set_cached_product(product_id: int, product: dict):
    client = get_cache_client()
    key = f"product:{product_id}"
    client.setex(key, Config.CACHE_TTL_SECONDS, json.dumps(product))
