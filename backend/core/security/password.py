from typing import Annotated, Tuple

from argon2 import PasswordHasher
from argon2.exceptions import (
    InvalidHashError,
    VerificationError,
    VerifyMismatchError,
)
from fastapi import Depends

from core.config import config


class PasswordService:
    def __init__(
        self,
        time_cost: int | None = None,
        memory_cost: int | None = None,
        parallelism: int | None = None,
        hash_len: int | None = None,
        salt_len: int | None = None,
    ) -> None:
        self._hasher = PasswordHasher(
            time_cost=time_cost or config.PASSWORD_TIME_COST,
            memory_cost=memory_cost or config.PASSWORD_MEMORY_COST,
            parallelism=parallelism or config.PASSWORD_PARALLELISM,
            hash_len=hash_len or config.PASSWORD_HASH_LENGTH,
            salt_len=salt_len or config.PASSWORD_SALT_LENGTH,
        )

    def hash_password(self, password: str) -> str:
        if not password:
            raise ValueError("Password cannot be empty")

        return self._hasher.hash(password)

    def verify_password(self, hashed_password: str, plain_password: str) -> bool:
        try:
            self._hasher.verify(hashed_password, plain_password)
            return True
        except VerifyMismatchError:
            return False

        except (VerificationError, InvalidHashError) as e:
            raise ValueError(f"Invalid password hash format: {str(e)}")

    def needs_rehash(self, hashed_password: str) -> bool:
        try:
            return self._hasher.check_needs_rehash(hashed_password)
        except (VerificationError, InvalidHashError):
            return True

    def verify_and_rehash(
        self, hashed_password: str, plain_password: str
    ) -> Tuple[bool, str | None]:
        is_valid = self.verify_password(hashed_password, plain_password)

        if is_valid and self.needs_rehash(hashed_password):
            new_hash = self.hash_password(plain_password)
            return True, new_hash

        return is_valid, None


def get_password_service() -> PasswordService:
    return PasswordService()


PasswordServiceDep = Annotated[PasswordService, Depends(get_password_service)]
