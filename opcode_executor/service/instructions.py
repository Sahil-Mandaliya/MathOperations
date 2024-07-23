
from abc import ABC, abstractmethod
from opcode_executor.service.operations import SetOperationSimulator, AdrOperationSimulator, AddOperationSimulator, MoveOperationSimulator, IncOperationSimulator, DcrOperationSimulator, RstOperationSimulator

instruction_to_operation_map = {
    "SET":SetOperationSimulator,
    "ADR":AdrOperationSimulator,
    "ADD":AddOperationSimulator,
    "MOV":MoveOperationSimulator,
    "INR":IncOperationSimulator,
    "DCR":DcrOperationSimulator,
    "RST":RstOperationSimulator
}

class InstructionSimulatorBase(ABC):
    @abstractmethod
    def execute(self):
        pass

class InstructionSimulator(InstructionSimulatorBase):
    def __init__(self, instruction_str, current_state) -> None:
        instruction = instruction_str.split(" ")
        self.instruction_type = instruction[0]
        self.params = []
        self.current_state = current_state
        if len(instruction) > 1:
            self.params = instruction[1:]

    def execute(self):
        if self.instruction_type.upper() not in instruction_to_operation_map:
            return
            # raise Exception("Invalid instruction ", self.instruction_type)
    
        operation_simulator = instruction_to_operation_map[self.instruction_type.upper()]
        operation_simulator().execute(self.params, self.current_state)


