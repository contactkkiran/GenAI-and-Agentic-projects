from app.guards.base_guard import BaseGuardrail
from app.models.guardrail_result import GuardrailResult


class AuthorizationGuard(BaseGuardrail):

    @property
    def name(self) -> str:
        return "Authorization"

    def check_account_access(self, user_id: str, account_id: str) -> GuardrailResult:

        # Simulated banking ownership data
        user_accounts = {"user001": ["1001", "1002"], "user002": ["2001", "2002"]}

        allowed_accounts = user_accounts.get(user_id, [])

        if account_id not in allowed_accounts:
            return GuardrailResult(
                allowed=False,
                guardrail=self.name,
                reason=f"User {user_id} is not authorized to access account {account_id}.",
            )

        return GuardrailResult(
            allowed=True,
            guardrail=self.name,
            reason=f"User {user_id} is authorized to access account {account_id}.",
        )
