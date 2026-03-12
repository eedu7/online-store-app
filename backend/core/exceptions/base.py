from typing import Any, Dict

from fastapi import HTTPException, status


class CustomException(HTTPException):
    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        error_code: str | None = None,
        headers: Dict[str, str] | None = None,
        details: Dict[str, Any] | None = None,
    ) -> None:
        detail: Dict[str, Any] = {"message": message}
        if error_code:
            detail["error_code"] = error_code
        if details:
            detail["details"] = details

        self.message = message
        self.error_code = error_code
        super().__init__(status_code=status_code, detail=detail, headers=headers)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.message}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(message={self.message!r}, status_code={self.status_code})"
