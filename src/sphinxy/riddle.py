from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """
        Check if the provided answer matches the correct answer, ignoring case.

        Parameters:
            answer (str): The answer to check for correctness.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """
        Returns an iterator that yields each element of the `answer` attribute.

        Returns:
            An iterator that yields each element of the `answer` attribute.
        """
        yield from iter(self.answer)
