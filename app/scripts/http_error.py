from fastapi import HTTPException
import logging


def http_error(error_message: str, error: Exception | str = "",
               logger: logging.Logger = None, error_code: int = 500) -> None:
    if logger is not None:
        # Передаём логгеру информацию об ошибке
        logger.critical(error_message)
        if str(error) == "":
            pass
        else:
            logger.error(str(error))

        # Вызываем класс ошибки FastAPI
        raise HTTPException(status_code=error_code,
                            detail={"error_description": error_message, "details": str(error)})
    else:
        # Вызываем класс ошибки FastAPI
        raise HTTPException(status_code=error_code,
                            detail={"error_description": error_message, "details": str(error)})
