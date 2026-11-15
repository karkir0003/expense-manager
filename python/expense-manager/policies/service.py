from typing import List, Optional, Tuple
from currency.models import Money
from employees.models import Role
from employees.service import EmployeeService
from policies.models import ExpenseCategory, PolicyAction, PolicyRule


class PolicyService:
    def __init__(self, employee_service: EmployeeService):
        self.employee_service = employee_service
        self._rules: List[PolicyRule] = []

    def register_rule(self, rule: PolicyRule) -> None:
        self._rules.append(rule)

    def evaluate_policy(
        self,
        department_id: str,
        category: ExpenseCategory,
        usd_amount: Money,
        role: Optional[Role] = None,
    ) -> Tuple[PolicyAction, Optional[str]]:
        """
        Evaluates applicable policy rules and returns (PolicyAction, matched_rule_id).
        """
        for rule in self._rules:
            if rule.department_id is None and rule.category == category:
                if rule.max_amount_cents is not None and usd_amount.amount_cents < rule.max_amount_cents:
                    return rule.action, rule.rule_id
                return PolicyAction.REQUIRE_APPROVAL, rule.rule_id

        return PolicyAction.REQUIRE_APPROVAL, None