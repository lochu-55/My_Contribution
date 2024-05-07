import pytest
from Base.Libraries.logging import logger


@pytest.fixture
def log():
    logs = logger(r"Base/utils/Logs/API_logs/API.log")
    return logs
