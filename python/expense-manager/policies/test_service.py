from currency.models import Currency, Money
from employees.models import Department
from employees.service import EmployeeService
from policies.models import ExpenseCategory, PolicyAction, PolicyRule
from policies.service import PolicyService


def test_default_fallback_requires_approval():
    emp_svc = EmployeeService()
    emp_svc.register_department(Department("CORP", "Corp"))
    policy_svc = PolicyService(emp_svc)

    action, rule_id = policy_svc.evaluate_policy(
        "CORP", ExpenseCategory.LODGING, Money(15000, Currency.USD)
    )
    assert action == PolicyAction.REQUIRE_APPROVAL
    assert rule_id is None


def test_policy_exact_boundary_and_priority_order():
    emp_svc = EmployeeService()
    emp_svc.register_department(Department("CORP", "Corp"))
    policy_svc = PolicyService(emp_svc)

    policy_svc.register_rule(
        PolicyRule(
            rule_id="r_meal_auto",
            category=ExpenseCategory.FOOD_AND_BEVERAGE,
            max_amount_cents=5_000,
            action=PolicyAction.AUTO_APPROVE,
            priority=100,
        )
    )
    policy_svc.register_rule(
        PolicyRule(
            rule_id="r_meal_ban",
            category=ExpenseCategory.FOOD_AND_BEVERAGE,
            min_amount_cents=50_000,
            action=PolicyAction.REJECT,
            priority=10,
        )
    )

    action_50, rule_50 = policy_svc.evaluate_policy(
        "CORP", ExpenseCategory.FOOD_AND_BEVERAGE, Money(5_000, Currency.USD)
    )
    assert action_50 == PolicyAction.AUTO_APPROVE
    assert rule_50 == "r_meal_auto"

    action_600, rule_600 = policy_svc.evaluate_policy(
        "CORP", ExpenseCategory.FOOD_AND_BEVERAGE, Money(60_000, Currency.USD)
    )
    assert action_600 == PolicyAction.REJECT
    assert rule_600 == "r_meal_ban"