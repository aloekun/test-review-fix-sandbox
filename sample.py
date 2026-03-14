"""Sample Python module for E2E testing.

This module contains intentional code quality issues
that a code reviewer would flag.
"""


def divide(a, b):
    """Divide a by b."""
    return a / b  # missing zero division check


def get_first_element(lst):
    """Return the first element of a list."""
    return lst[0]  # IndexError when list is empty


def count_occurrences(items, target):
    """Count how many times target appears in items."""
    count = 0
    for i in range(len(items)):  # should use `for item in items`
        if items[i] == target:
            count = count + 1  # should use count += 1
    return count


class UserManager:
    """Manage a collection of users."""

    def __init__(self):
        self.users = []

    def add_user(self, name, age):
        # no validation: negative age or empty name are accepted
        user = {"name": name, "age": age}
        self.users.append(user)

    def find_user(self, name):
        for user in self.users:
            if user["name"] == name:
                return user
        # implicitly returns None without documentation


def calculate_ratio(numerator, denominator):
    """Calculate the ratio of two numbers.

    Raises:
        ValueError: If denominator is 0.
    """
    if denominator == 0:
        raise ValueError("denominator must not be zero")
    return numerator / denominator
