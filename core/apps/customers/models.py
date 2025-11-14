from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities import CustomerEntity


class CustomerModel(TimedBaseModel):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, verbose_name="Имя пользователя")
    phone = models.CharField(max_length=20, verbose_name="Телефон", unique=True)
    token = models.CharField(
        max_length=255,
        verbose_name="Токен",
        default=uuid4,
        unique=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = "customer"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def to_entity(self) -> CustomerEntity:
        return CustomerEntity(
            id=self.id,
            username=self.username,
            phone=self.phone,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
