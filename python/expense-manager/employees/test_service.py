from employees.models import Department, Employee, Role
from employees.service import EmployeeService


def test_management_chain_traversal():
    service = EmployeeService()
    service.register_department(Department("ENG", "Engineering"))
    service.register_employee(Employee("e_ceo", "Alice", "ENG", Role.C_LEVEL))
    service.register_employee(Employee("e_vp", "Bob", "ENG", Role.VP, manager_id="e_ceo"))
    service.register_employee(Employee("e_ic", "Charlie", "ENG", Role.IC, manager_id="e_vp"))

    chain = service.get_management_chain("e_ic")
    assert [e.employee_id for e in chain] == ["e_vp", "e_ceo"]


def test_management_chain_handles_cyclic_reference_safely():
    service = EmployeeService()
    service.register_department(Department("ENG", "Engineering"))
    service.register_employee(Employee("e_a", "Alice", "ENG", Role.VP, manager_id="e_b"))
    service.register_employee(Employee("e_b", "Bob", "ENG", Role.MANAGER, manager_id="e_a"))

    chain = service.get_management_chain("e_a")
    assert [e.employee_id for e in chain] == ["e_b"]


def test_department_hierarchy_resolution():
    service = EmployeeService()
    service.register_department(Department("CORP", "Corporate"))
    service.register_department(Department("ENG", "Engineering", parent_dept_id="CORP"))
    service.register_department(Department("INFRA", "Infrastructure", parent_dept_id="ENG"))

    assert service.get_department_hierarchy("INFRA") == ["INFRA", "ENG", "CORP"]