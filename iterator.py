from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any


class Node:
    def __init__(self, content: Any, next_element: Node | None = None):
        self._content = content
        self.next_element = next_element

    @property
    def content(self) -> Any:
        return deepcopy(self._content)

    def __str__(self) -> str:
        return f"Node: {self._content}"


class SinglyLinkedList:
    def __init__(self):
        self._root = None
        self._last = None

    def add_node(self, node: Node):
        if self._root is None:
            self._root = node
        else:
            self._last.next_element = node
        self._last = node

    def __iter__(self) -> SinglyLinkedList:
        pass  # your code here

    def __next__(self):
        pass  # your code and type hints here


if __name__ == "__main__":
    with open("dc.txt", "r") as file:
        lines = file.read()

    lines = lines.split("\n\n")

    singly_linked_list = SinglyLinkedList()
    for i, line in enumerate(lines):
        singly_linked_list.add_node(Node(line))

    singly_linked_list = iter(singly_linked_list)
    while True:
        print(next(singly_linked_list))
