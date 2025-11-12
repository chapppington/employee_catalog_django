from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime
from typing import Optional


@dataclass
class EmployeeEntity:
    id: int
    first_name: str
    last_name: str
    middle_name: str
    position: str
    date_hired: datetime
    salary: float
    manager: Optional["EmployeeEntity"] = field(default=None, kw_only=True)
    created_at: datetime
    updated_at: datetime
