from abc import ABC, abstractmethod

from typing import List
from opcode_executor.model.register_state import RegisterState
from opcode_executor.model.register import Register
from opcode_executor.repository.register.register import RegisterStateRepository

class SetOperationSimulator():
    def __init__(self) -> None:
        pass

    def execute(self, params, current_state) -> RegisterState:
        if len(params) != 2:
            raise Exception("Invalid parameters for SET instruction")
        
        register_name = params[0]
        value = params[1]
        register = Register(register_name)
        register.set_value(int(value))
        return RegisterStateRepository().update_register(register, current_state)

class AdrOperationSimulator():
    def __init__(self) -> None:
        pass
    
    def execute(self, params, current_state) -> RegisterState:
        if len(params) != 2:
            raise Exception("Invalid parameters for ADR instruction")
        
        register1_name = params[0]
        register2_name = params[1]

        register1_value = current_state.get_register(register1_name).value
        register2_value = current_state.get_register(register2_name).value

        register = Register(register1_name)
        register.set_value(int(register1_value)+int(register2_value))
        return RegisterStateRepository().update_register(register, current_state)


class AddOperationSimulator():
    def __init__(self) -> None:
        pass
    
    def execute(self, params, current_state) -> RegisterState:
        if len(params) != 2:
            raise Exception("Invalid parameters for ADD instruction")
        
        register1_name = params[0]
        value = params[1]
        register1_value = current_state.get_register(register1_name).value
        register = Register(register1_name)
        register.set_value(int(register1_value)+int(value))
        return RegisterStateRepository().update_register(register, current_state)


class MoveOperationSimulator():
    def __init__(self) -> None:
        pass
    
    def execute(self, params, current_state) -> RegisterState:
        if len(params) != 2:
            raise Exception("Invalid parameters for MOV instruction")
        
        register1_name = params[0]
        register2_name = params[1]

        register2_value = current_state.get_register(register2_name).value

        register = Register(register1_name)
        register.set_value(int(register2_value))
        return RegisterStateRepository().update_register(register, current_state)

class IncOperationSimulator():
    def __init__(self) -> None:
        pass
    
    def execute(self, params, current_state) -> RegisterState:
        if len(params) != 1:
            raise Exception("Invalid parameters for INC instruction")
        
        register1_name = params[0]
        return AddOperationSimulator().execute([register1_name,1], current_state)

class DcrOperationSimulator():
    def __init__(self) -> None:
        pass

    def execute(self, params, current_state) -> RegisterState:
        if len(params) != 1:
            raise Exception("Invalid parameters for DCR instruction")
        
        register1_name = params[0]
        return AddOperationSimulator().execute([register1_name,-1], current_state)

class RstOperationSimulator():
    def __init__(self) -> None:
        pass
    
    def execute(self, params, current_state) -> RegisterState:        
        current_state.reset()
        return current_state


