from typing import Callable

import pygame


class Timers:
    """
    A class that can handle an execution of a function after a period of time
    """

    def __init__(self, duration: int, func: Callable = None) -> None:
        self.duration = duration
        self.func = func
        self.start_time = 0
        self.active = False

    def activate(self) -> None:
        """
        Star the timer counter
        @return:
        """
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        """
        Stop the timer counting
        @return:
        """
        self.active = False
        self.start_time = 0

    def update(self):
        """
        Update the timer : ) Execute the function if the time comes
        @return:
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration:
            self.deactivate()
            if self.func:
                self.func()
