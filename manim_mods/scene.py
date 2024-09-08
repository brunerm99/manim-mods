# scene.py

from manim import *
from contextlib import contextmanager
from typing import Generator


# 100% thanks to https://github.com/abul4fia :)
@contextmanager
def new_section(
    self,
    name: str = "unnamed",
    type: str = DefaultSectionType.NORMAL,
    skip_animations: bool = False,
    start_wait: float = 0.5,
    end_wait: float = 0,
) -> Generator[None, None, None]:
    print(f"Entering section: {name}")
    self.next_section(name, type, skip_animations)
    self.wait(start_wait)
    yield
    print(f"Exiting section: {name}")
    self.wait(end_wait)


Scene.new_section = new_section
