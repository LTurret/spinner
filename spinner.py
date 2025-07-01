import time

from sys import stdout
from typing import Any, Generator, Optional


spinner_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]


def box(title: Optional[str] = None, text: Optional[str] = None, width: int = 16, stream: bool = False) -> None:
    if stream:
        stdout.write("\033[F" * 3 if hasattr(box, "ran_once") else "")
        box.ran_once = True
        stdout.write("\033[K")
    if title is not None:
        stdout.write(f"╭─┐\033[90m{title}\033[00m┌{"─" * (width - len(title) - 3)}╮\n")
    else:
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


if __name__ == "__main__":
    for frame in spinner("Baking ur cake properly", duration=3):
        box(title="meow :3", text=frame, width=30, stream=True)
    box(title="result", text="Ur cake is good now meow", width=30)

