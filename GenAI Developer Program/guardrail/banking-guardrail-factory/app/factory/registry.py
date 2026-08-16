from typing import Any, Dict


class GuardRegistry:
    def __init__(self) -> None:
        self.config: Dict[str, Any] = {}

    def register_config(self, config: Dict[str, Any]) -> None:
        self.config = config

    def get_guard_settings(self, category: str, guard_name: str) -> Dict[str, Any]:
        return self.config.get("guards", {}).get(category, {}).get(guard_name, {})

    def is_enabled(self, category: str, guard_name: str) -> bool:
        return bool(self.get_guard_settings(category, guard_name).get("enabled", False))
