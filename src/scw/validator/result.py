from dataclasses import dataclass


@dataclass
class ValidationMessage:
    rule_id: str
    level: str
    message: str


@dataclass
class ValidationResult:
    valid: bool
    messages: list[ValidationMessage]