from pydantic import BaseModel


class GuardrailResult(BaseModel):
    allowed: bool
    guardrail: str
    reason: str = ""
    modified_input: str | None = None
