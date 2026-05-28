"""Exception types for the tasks package."""


class TaskError(Exception):
    """Base class for task errors."""


class TaskNotFoundError(TaskError):
    """Raised when a task id does not exist."""
