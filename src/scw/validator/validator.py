from pathlib import Path

import yaml

from .rules import (
    validate_scw_001,
    validate_scw_002,
    validate_scw_003,
)
from .result import ValidationResult


class Validator:

    def validate_file(self, path: str) -> ValidationResult:

        data = yaml.safe_load(
            Path(path).read_text(
                encoding="utf-8"
            )
        )

        messages = []

        messages.extend(
            validate_scw_001(data)
        )

        messages.extend(
            validate_scw_002(data)
        )

        messages.extend(
            validate_scw_003(data)
        )

        valid = not any(
            msg.level == "ERROR"
            for msg in messages
        )

        return ValidationResult(
            valid=valid,
            messages=messages,
        )