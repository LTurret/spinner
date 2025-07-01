import time

from sys import stdout
from typing import Any, Generator, Optional


spinner_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]


def box(text: Optional[str], width: int = 16):
    stdout.write("\033[F" * 3 if hasattr(box, "ran_once") else "")
    box.ran_once = True
    stdout.write("\033[K")
    stdout.write(f"╭{"─" * width}╮\n")
    stdout.write(f"│{" " * width}│\r")
    stdout.write(f"│ {text}\n")
    stdout.write(f"╰{"─" * width}╯\n")
    stdout.flush()


def spinner(text: Optional[str] = None, duration: int = 3) -> Generator[Any]:
    start = time.time()
    idx = 0

    while time.time() - start < duration:
        frame = spinner_frames[idx % len(spinner_frames)]
        yield f"\033[96m{frame}\033[00m {text}"
        time.sleep(0.1)
        idx += 1

    yield f"\033[92m✔ Done!\033[00m"


for frame in spinner("Loading", duration = 3):
    box(frame, width=16)
