import pytest

from core.apps.employee.services import (
    BaseEmployeeService,
    ORMEmployeeService,
)


@pytest.fixture
def employee_service() -> BaseEmployeeService:
    return ORMEmployeeService()
