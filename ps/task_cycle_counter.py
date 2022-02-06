"""
Given a list of tasks and a cooldown to be respected for the same type of task, calculate how long it would take you to run the entire list of tasks, assuming each task takes one cycle.

Example:
tasks = [5, 5, 3, 3, 5]
cooldown = 2
execution plan = [5, _, _, 5, 3, _, _, 3, 5]
output = 9

1 + 2 + 1 + 2

tasks = [1, 2, 3, 1]
cooldown = 2
execution plan = [1, 2, 3, 1]


tasks = []
cooldown = 2
execution plan = []
output = 0
"""


def get_task_counter(tasks, cooldown):
    size = len(tasks)
    if size <= 1 or cooldown < 1:
        return size

    counters = dict()
    result = 1
    counter = 1
    counters[tasks[0]] = 0
    while counter < size:
        if counters.get(tasks[counter], -1) == -1 or (counters.get(tasks[counter], -1) >= 0 and (result - cooldown) > counters[tasks[counter]]):
            counters[tasks[counter]] = result
            counter += 1
        result += 1

    return result


if __name__ == "__main__":
    print("Enter Tasks, Space Separated: ")
    input_tasks = list(map(int, input().split(" ")))

    print("Enter Cooldown Period: ")
    cooldown_period = int(input())

    print("Total Counter is: ", get_task_counter(input_tasks, cooldown_period))
