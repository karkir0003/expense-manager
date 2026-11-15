# Expense Manager - AI Assisted Design

Welcome to the **Expense Manager** design round!

### Overview

Expense Manager is an enterprise expense submission, policy evaluation, approval routing, and accounting ledger system.

The core system is structured into domain packages:
- **`employees`**: Employee reporting hierarchy and department tree traversal.
- **`currency`**: Normalized multi-currency money representation and FX conversion rates.
- **`policies`**: Configurable, prioritized policy rules (Auto-Approve, Require Approval, Reject) evaluated by category, department, role, and spending thresholds.
- **`routing`**: Approval routing generation based on management hierarchy and finance sign-offs.
- **`ledger`**: Finalized transaction posting categorized into Capital Expenditures (CapEx) vs Operating Expenditures (OpEx).
- **`expenses`**: End-to-end orchestration of submission, policy evaluation, approval workflows, and ledger posting.

---

### Quick Start Instructions

1. **Choose your language** and change into its directory:
   ```bash
   cd python        # For Python (pytest)
   cd javascript    # For JavaScript (Node.js)
   cd java          # For Java (JUnit 5)
   cd c++           # For C++ (Google Test)
   ```

2. **Verify / install environment** (optional):
   ```bash
   make setup
   ```
   *(Checks compilers/runtimes and automatically verifies or provisions dependencies).*

3. **Run your tests**:
   ```bash
   make
   ```
   *(Runs the test suite).*

4. **Clean artifacts** (optional):
   ```bash
   make clean
   ```

---

## Directory & File Reference

| Language | Directory | Test Framework | Source Package / File | Test Suite |
| :--- | :--- | :--- | :--- | :--- |
| **Python** | [`python/`](python/) | `pytest` (configured via `pyproject.toml`) | [`python/expense-manager/`](python/expense-manager/) | [`python/expense-manager/*/test_service.py`](python/expense-manager/) |
| **JavaScript** | `javascript/` | Built-in Node assertions (zero dependencies) | [`javascript/`](javascript/) | [`javascript/tests/test_expense_manager.js`](javascript/tests/) |
| **Java** | `java/` | `JUnit 5` (bundled standalone runner) | [`java/src/...`](java/src/) | [`java/tests/TestExpenseManager.java`](java/tests/) |
| **C++** | `c++/` | `Google Test` (auto-provisioned via setup.sh) | [`c++/include/...`](c++/include/) | [`c++/tests/test_expense_manager.cpp`](c++/tests/) |

Every language directory contains a standardized `Makefile` with identical targets (`make`, `make setup`, `make clean`) so your workflow is consistent regardless of which language you choose.
