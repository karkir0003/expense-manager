from typing import Dict, List, Optional
from employees.models import Department, Employee


class EmployeeService:
    def __init__(self):
        self._employees: Dict[str, Employee] = {}
        self._departments: Dict[str, Department] = {}

    def register_employee(self, employee: Employee) -> None:
        self._employees[employee.employee_id] = employee

    def register_department(self, department: Department) -> None:
        self._departments[department.dept_id] = department

    def get_employee(self, employee_id: str) -> Optional[Employee]:
        return self._employees.get(employee_id)

    def get_department(self, dept_id: str) -> Optional[Department]:
        return self._departments.get(dept_id)

    def get_management_chain(self, start_employee_id: str) -> List[Employee]:
        """Climbs the manager reporting hierarchy until reaching the top executive."""
        chain: List[Employee] = []
        curr = self.get_employee(start_employee_id)
        visited = set()

        while curr and curr.manager_id and curr.manager_id not in visited:
            visited.add(curr.manager_id)
            mgr = self.get_employee(curr.manager_id)
            if not mgr:
                break
            chain.append(mgr)
            curr = mgr

        return chain

    def get_department_hierarchy(self, dept_id: str) -> List[str]:
        """Returns ordered department path: [current_dept_id, parent_dept_id, ..., root_dept_id]."""
        hierarchy: List[str] = []
        curr_id: Optional[str] = dept_id
        visited = set()

        while curr_id and curr_id not in visited:
            visited.add(curr_id)
            hierarchy.append(curr_id)
            dept = self.get_department(curr_id)
            curr_id = dept.parent_dept_id if dept else None

        return hierarchy