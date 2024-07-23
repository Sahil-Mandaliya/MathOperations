
from opcode_executor.model.register import Register
from opcode_executor.model.register_state import RegisterState, CurrentRegisters

class RegisterStateRepository:
    def __init__(self) -> None:
        pass

    def update_register(self, register: Register, current_state: RegisterState):
        current_state.update_state(register)
        return current_state
        