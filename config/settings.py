import os
from dataclasses import dataclass
from typing import TypedDict

from config.environments import BASE_URLS, Environment


class ViewportSize(TypedDict):
    width: int
    height: int


@dataclass(frozen=True)
class Settings:
    env: Environment
    base_url: str
    browser: str
    headless: bool
    slow_mo: int
    timeout_ms: int
    navigation_timeout_ms: int
    viewport: ViewportSize


def _get_env() -> Environment:
    raw_env = os.getenv("ENV", Environment.LOCAL.value).lower()
    try:
        return Environment(raw_env)
    except ValueError as exc:
        raise ValueError(
            f"Invalid ENV '{raw_env}'. " f"Valid values: {[e.value for e in Environment]}"
        ) from exc


def load_settings() -> Settings:
    env = _get_env()
    browser = os.getenv("BROWSER", "chromium").lower()
    if browser not in ["chromium", "firefox", "webkit"]:
        raise ValueError(f"Invalid BROWSER '{browser}'. Valid values: chromium, firefox, webkit")

    return Settings(
        env=env,
        base_url=BASE_URLS[env],
        browser=browser,
        headless=os.getenv("HEADLESS", "true").lower() == "true",
        slow_mo=int(os.getenv("SLOW_MO", "0")),
        timeout_ms=int(os.getenv("TIMEOUT_MS", "30000")),
        navigation_timeout_ms=int(os.getenv("NAVIGATION_TIMEOUT_MS", "30000")),
        viewport={"width": 1280, "height": 720},
    )


settings = load_settings()
