from redis.asyncio import ConnectionPool, Redis

from core.config import config


def _make_pool(url: str) -> ConnectionPool:
    return ConnectionPool.from_url(url, decode_response=True, max_connections=20)


_token_pool = _make_pool(config.REDIS_URL_TOKENS)
_cache_pool = _make_pool(config.REDIS_URL_CACHE)


def get_token_redis() -> Redis:
    return Redis(connection_pool=_token_pool)


def get_cache_redis() -> Redis:
    return Redis(connection_pool=_cache_pool)
