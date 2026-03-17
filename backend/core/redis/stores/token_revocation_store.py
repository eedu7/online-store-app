from typing import Annotated

from fastapi import Depends
from redis.asyncio import Redis

from core.config import config
from core.redis.base import BaseRedisStore
from core.redis.client import RedisDep


class TokenRevocationStore(BaseRedisStore):
    def __init__(self, redis: Redis, prefix: str) -> None:
        super().__init__(redis, prefix)

    async def revoke(self, jti: str, ttl: int) -> None:
        if ttl > 0:
            await self.set(key=self._make_key(jti), value="REVOKED", ttl=ttl)

    async def is_revoked(self, jti: str) -> bool:
        return await self.exists(self._make_key(jti))


def get_token_revocation_store(redis: RedisDep) -> TokenRevocationStore:
    return TokenRevocationStore(redis=redis, prefix=config.REDIS_TOKEN_REVOKE_PREFIX)


TokenRevocationStoreDep = Annotated[
    TokenRevocationStore, Depends(get_token_revocation_store)
]
