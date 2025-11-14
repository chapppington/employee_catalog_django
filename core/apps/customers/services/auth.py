from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.customers.services.codes import BaseCodeService
from core.apps.customers.services.customers import BaseCustomerService
from core.apps.customers.services.sender import BaseSenderService


@dataclass(eq=False)
class BaseAuthService(ABC):
    customer_service: BaseCustomerService
    codes_service: BaseCodeService
    send_service: BaseSenderService

    @abstractmethod
    def authenticate(self, phone: str): ...

    @abstractmethod
    def confirm(self, code: str, phone: str): ...


class AuthService(BaseAuthService):
    def authenticate(self, phone: str):
        customer = self.customer_service.get_or_create(phone)
        code = self.codes_service.generate_code(customer)
        self.send_service.send_code(code, customer)

    def confirm(self, code: str, phone: str):
        customer = self.customer_service.get_by_phone(phone)
        self.codes_service.validate_code(code, customer)

        return self.customer_service.generate_token(customer)
