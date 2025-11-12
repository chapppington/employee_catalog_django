from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime
from typing import Optional

from core.apps.common.entitites import BaseEntity


@dataclass
class Employee(BaseEntity):
    first_name: str
    last_name: str
    middle_name: str
    position: str
    date_hired: datetime
    salary: float
    manager: Optional["Employee"] = field(default=None, kw_only=True)
