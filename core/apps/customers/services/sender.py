from abc import (
    ABC,
    abstractmethod,
)

from core.apps.customers.entities import CustomerEntity


class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, code: str, customer: CustomerEntity) -> None: ...


class DummySendService(BaseSenderService):
    def send_code(self, code: str, customer: CustomerEntity) -> None:
        print(f"Sending code {code} to customer {customer.phone}")
