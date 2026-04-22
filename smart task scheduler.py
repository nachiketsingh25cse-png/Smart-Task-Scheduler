"""
Smart Task Scheduler
--------------------
This program schedules tasks to maximize profit using a greedy algorithm.

Each task has:
- id
- deadline
- profit

Goal:
Complete tasks within deadlines to maximize total profit.

Author: Nachiket Singh
"""

from typing import List


class Task:
    def __init__(self, task_id: str, deadline: int, profit: int):
        self.task_id = task_id
        self.deadline = deadline
        self.profit = profit

    def __repr__(self):
        return f"{self.task_id}(d={self.deadline}, p={self.profit})"


def schedule_tasks(tasks: List[Task]) -> List[Task]:
    """
    Greedy algorithm to schedule tasks for maximum profit.
    """

    # Step 1: Sort tasks by profit (descending)
    tasks.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(task.deadline for task in tasks)
    schedule = [None] * max_deadline

    # Step 2: Assign tasks to latest possible slot
    for task in tasks:
        for slot in range(task.deadline - 1, -1, -1):
            if schedule[slot] is None:
                schedule[slot] = task
                break

    # Remove empty slots
    return [task for task in schedule if task is not None]


def main():
    print("📌 Smart Task Scheduler\n")

    tasks = [
        Task("A", 2, 100),
        Task("B", 1, 19),
        Task("C", 2, 27),
        Task("D", 1, 25),
        Task("E", 3, 15),
    ]

    print("Input Tasks:")
    for task in tasks:
        print(task)

    result = schedule_tasks(tasks)

    print("\n✅ Scheduled Tasks:")
    total_profit = 0

    for task in result:
        print(task)
        total_profit += task.profit

    print(f"\n💰 Total Profit: {total_profit}")


if __name__ == "__main__":
    main()