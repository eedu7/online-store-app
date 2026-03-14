from typing import Tuple

from argon2 import PasswordHasher
from argon2.exceptions import (
    InvalidHashError,
    VerificationError,
    VerifyMismatchError,
)


class PasswordService:
    def __init__(
        self,
        time_cost: int = 2,
        memory_cost: int = 65536,  # 64 MiB
        parallelism: int = 4,
        hash_len: int = 32,
        salt_len: int = 16,
    ) -> None:
        self._hasher = PasswordHasher(
            time_cost=time_cost,
            memory_cost=memory_cost,
            parallelism=parallelism,
            hash_len=hash_len,
            salt_len=salt_len,
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


password_service = PasswordService()
