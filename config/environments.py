from enum import StrEnum


class Environment(StrEnum):
    LOCAL = "local"
    STAGING = "staging"
    PROD = "prod"


BASE_URLS: dict[Environment, str] = {
    Environment.LOCAL: "https://www.saucedemo.com",
    Environment.STAGING: "https://www.saucedemo.com",
    Environment.PROD: "https://www.saucedemo.com",
}
