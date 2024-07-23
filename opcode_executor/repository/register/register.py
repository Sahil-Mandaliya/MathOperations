
from opcode_executor.model.register import Register
from opcode_executor.model.register_state import RegisterState, CurrentRegisters

class RegisterStateRepository:
    def __init__(self, registers) -> None:
        self.registers = registers

    def update_register(self, register: Register):
        state = RegisterState(self.registers)
        state.update_state(register)
        return state
        