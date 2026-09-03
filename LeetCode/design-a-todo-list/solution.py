from collections import defaultdict
from sortedcontainers import SortedList
from typing import List


class TodoList:

    def __init__(self):
        self.counter = 0
        self.users_tasks = defaultdict(SortedList)
        self.complete = defaultdict(set)
        self.user_tags = defaultdict(set)

    def addTask(
        self,
        userId: int,
        taskDescription: str,
        dueDate: int,
        tags: List[str]
    ) -> int:
        self.counter += 1
        taskId = self.counter

        # Store tasks sorted by (dueDate, taskId)
        self.users_tasks[userId].add((dueDate, taskId, taskDescription))

        # Store tasks for each tag
        for tag in tags:
            self.user_tags[(userId, tag)].add((dueDate, taskDescription, taskId))

        return taskId

    def getAllTasks(self, userId: int) -> List[str]:
        return [
            desc
            for _, taskId, desc in self.users_tasks[userId]
            if taskId not in self.complete[userId]
        ]

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        result = sorted(
            (dueDate, desc)
            for dueDate, desc, taskId in self.user_tags[(userId, tag)]
            if taskId not in self.complete[userId]
        )
        return [desc for _, desc in result]

    def completeTask(self, userId: int, taskId: int) -> None:
        self.complete[userId].add(taskId)


# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId, taskDescription, dueDate, tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId, tag)
# obj.completeTask(userId, taskId)