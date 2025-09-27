from __future__ import annotations

from pathlib import Path


class FolderReaderIterator:
    def __init__(self, folder_path: Path, file_extension: str | None = None) -> None:
        self._folder_path = folder_path
        self._file_extension = file_extension

    def __iter__(self):
        pass  # your code and type hints here

    def __next__(self):
        pass  # your code and type hints here
