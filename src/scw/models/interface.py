# models/interface.py

from dataclasses import dataclass


@dataclass
class Interface:
    name: str
    version: str
