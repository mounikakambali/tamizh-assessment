# TAMIZH Technical Assessment - Task 1

## Problem

A wearable device executes tasks sequentially.

Each task consumes battery during execution.

Between tasks, the device may remain idle and recharge.

The goal is to find the minimum total runtime required to execute all tasks.

---

## Approach

For every task:

1. Calculate battery required.

   required = duration × drainRate

2. If battery is sufficient:
   - Execute task immediately.

3. Otherwise:
   - Charge only the minimum amount needed.
   - Add charging time to total runtime.

4. Execute task and reduce battery.

5. If required battery exceeds battery capacity:
   - Return -1.

---

## Time Complexity

O(n)

where n is the number of tasks.

---

## Assumptions

- Battery level changes continuously.
- Charging is allowed only between tasks.
- Tasks must execute in given order.
- Idle duration may be fractional.

---

## Run

python solution.py
