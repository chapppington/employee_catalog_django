from datetime import datetime

from ninja import Schema

from core.apps.employee.entities.employee import EmployeeEntity


class EmployeeSchema(Schema):
    id: int
    first_name: str
    last_name: str
    middle_name: str
    position: str
    date_hired: datetime
    salary: float
    manager_id: int | None = None
    created_at: datetime
    updated_at: datetime | None = None

    @staticmethod
    def from_entity(entity: EmployeeEntity) -> "EmployeeSchema":
        return EmployeeSchema(
            id=entity.id,
            first_name=entity.first_name,
            last_name=entity.last_name,
            middle_name=entity.middle_name,
            position=entity.position,
            date_hired=entity.date_hired,
            salary=entity.salary,
            manager_id=entity.manager.id if entity.manager else None,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


EmployeeListSchema = list[EmployeeSchema]
