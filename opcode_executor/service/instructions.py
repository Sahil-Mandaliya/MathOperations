
from opcode_executor.service.operations import SetOperationSimulator, AdrOperationSimulator, AddOperationSimulator, MoveOperationSimulator, IncOperationSimulator, DcrOperationSimulator, RstOperationSimulator
from opcode_executor.model.register import CurrentRegisters

instruction_to_operation_map = {
    "SET":SetOperationSimulator,
    "ADR":AdrOperationSimulator,
    "ADD":AddOperationSimulator,
    "MOV":MoveOperationSimulator,
    "INC":IncOperationSimulator,
    "DCR":DcrOperationSimulator,
    "RST":RstOperationSimulator
}

class InstructionSimulator:
    def __init__(self, instruction_str:str) -> None:
        instruction = instruction_str.split(" ")
        self.instruction_type = instruction[0]
        self.params = []
        if len(instruction) > 1:
            self.params = instruction[1:]


    def execute(self):
        operation_simulator = instruction_to_operation_map[self.instruction_type.upper()]
        operation_simulator.execute()


