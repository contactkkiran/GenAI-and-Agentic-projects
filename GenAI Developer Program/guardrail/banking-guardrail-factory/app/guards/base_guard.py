from abc import ABC, abstractmethod
from app.models.guardrail_result import GuardrailResult


# Helper class that provides a standard way to create an ABC using
# inheritance.
class BaseGuardrail(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def check(self, text: str) -> GuardrailResult:
        pass
