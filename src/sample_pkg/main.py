from __future__ import annotations

from core import app_settings, db_settings


def say_hello() -> str:
    return "Hello, world!"


def print_dynaconf_settings() -> None:
    print(f"Dynaconf settings:\n{app_settings}")
    print(f"Dynaconf DB settings\n{db_settings}")

    print(f"Test DB host: {db_settings.host}")


if __name__ == "__main__":
    print_dynaconf_settings()
