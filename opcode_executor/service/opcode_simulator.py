from abc import ABC, abstractmethod

from typing import List

from opcode_executor.model.register_state import RegisterState
from opcode_executor.model.register import Register
from opcode_executor.service.instructions import InstructionSimulator

class OpcodeSimulator(ABC):
    def __init__(self) -> None:
        self.register_names = ["A","B","C","D"]
        self.registers = []
        for register_name in self.register_names:
             self.registers.append(Register(register_name))

        super().__init__()

    @abstractmethod
    def execute(self, instructions: List[str]) -> RegisterState:
        pass

class OperationsSimulator(OpcodeSimulator):
    def execute(self, instructions: List[str]) -> RegisterState:
        for instruction in instructions:
            InstructionSimulator.execute(instruction)
        
        return self.registers


opcode_simulator = OpcodeSimulator()
print(opcode_simulator.register_names)