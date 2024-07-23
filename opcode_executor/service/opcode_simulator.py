from abc import ABC, abstractmethod

from typing import List

from opcode_executor.model.register_state import RegisterState


class OpcodeSimulator(ABC):

    @abstractmethod
    def execute(self, instructions: List[str]) -> RegisterState:
        pass
