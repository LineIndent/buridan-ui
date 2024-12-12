import asyncio
from collections.abc import AsyncGenerator
from random import randint

import reflex as rx

from .style import AuthDynamicStyle

numberList: list[str] = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
]


class SandboxAuthState(rx.State):
    # ... account numbers vars ...
    one: str = "_"
    two: str = "_"
    three: str = "_"
    four: str = "_"

    five: str = "_"
    six: str = "_"
    seven: str = "_"
    eight: str = "_"

    nine: str = "_"
    ten: str = "_"
    eleven: str = "_"
    twelve: str = "_"

    thirteen: str = "_"
    fourteen: str = "_"
    fifteen: str = "_"
    sixteen: str = "_"

    # ... generate button vars ...
    authGenButton: dict[str, bool] = AuthDynamicStyle.passive

    # ... alert text vars ...
    authAlert: dict[str, str] = AuthDynamicStyle.alert_passive

    # ... dummy vars
    accountNumber: str

    @rx.event
    async def can_copy_account_number(self) -> rx.event:
        if self.accountNumber:
            yield rx.set_clipboard(self.accountNumber)
            yield rx.toast.info("Copied account number.")

        else:
            yield rx.toast.warning("No account number generated yet.")

    async def run_number_animation(self, place_name: str):
        for _ in range(35):
            number = str(randint(0, 9))
            setattr(self, place_name, number)
            yield
            await asyncio.sleep(0.061)

    @rx.event
    async def run_animation_task(self) -> AsyncGenerator:
        self.authGenButton = AuthDynamicStyle.active
        yield
        tasks = [self.run_number_animation(number) for number in numberList]

        for _ in range(35):
            await asyncio.gather(*[task.__anext__() for task in tasks])
            yield

        for number_name in numberList:
            value = getattr(self, number_name)
            self.accountNumber += value

        yield
        self.authGenButton = AuthDynamicStyle.finished
        self.authAlert = AuthDynamicStyle.alert_active
