# models/component.py

from dataclasses import dataclass


@dataclass
class Component:
    name: str
    version: str

    provides: list[str]
    depends_on: list[str]
