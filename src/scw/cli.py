import sys

from scw.validator.validator import Validator


def main():

    if len(sys.argv) != 2:
        print(
            "Usage: scw <manifest.yml>"
        )
        sys.exit(1)

    result = Validator().validate_file(
        sys.argv[1]
    )

    for msg in result.messages:
        print(
            f"[{msg.level}] "
            f"{msg.rule_id}: "
            f"{msg.message}"
        )

    if result.valid:
        print("\nPASS")
        sys.exit(0)

    print("\nFAIL")
    sys.exit(1)


if __name__ == "__main__":
    main()