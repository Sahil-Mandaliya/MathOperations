from abc import ABC, abstractmethod

from typing import List
from opcode_executor.service.opcode_simulator import OpcodeSimulator
from opcode_executor.service.instructions import InstructionSimulator
from opcode_executor.model.register_state import RegisterState
from opcode_executor.model.register import Register
from opcode_executor.repository.register.register import RegisterStateRepository

class SetOperationSimulator(InstructionSimulator):
    def execute(self) -> RegisterState:
        params = self.params
        if len(params) != 2:
            raise Exception("Invalid parameters for SET instruction")
        
        register_name = params[0]
        value = params[1]
        register = Register(register_name).set_value(value)
        return RegisterStateRepository.update_register(register)

class AdrOperationSimulator(InstructionSimulator):
    def execute(self) -> RegisterState:
        params = self.params
        if len(params) != 2:
            raise Exception("Invalid parameters for ADR instruction")
        
        register1_name = params[0]
        register2_name = params[1]

        register1_value = RegisterState.get_register(register1_name)
        register2_value = RegisterState.get_register(register2_name)

        register = Register(register1_name).set_value(register1_value+register2_value)
        return RegisterStateRepository.update_register(register)


class AddOperationSimulator(InstructionSimulator):
    def execute(self) -> RegisterState:
        params = self.params
        if len(params) != 2:
            raise Exception("Invalid parameters for ADD instruction")
        
        register1_name = params[0]
        value = params[1]
        register1_value = RegisterState.get_register(register1_name)
        register = Register(register1_name).set_value(register1_value+value)
        return RegisterStateRepository.update_register(register)


class MoveOperationSimulator(InstructionSimulator):
    def execute(self) -> RegisterState:
        params = self.params
        if len(params) != 2:
            raise Exception("Invalid parameters for MOV instruction")
        
        register1_name = params[0]
        register2_name = params[1]

        register2_value = RegisterState.get_register(register2_name)

        register = Register(register1_name).set_value(register2_value)
        return RegisterStateRepository.update_register(register)

class IncOperationSimulator(InstructionSimulator):
    def execute(self) -> RegisterState:
        params = self.params
        if len(params) != 1:
            raise Exception("Invalid parameters for INC instruction")
        
        register1_name = params[0]
        return AddOperationSimulator.execute([register1_name,1])

class DcrOperationSimulator(InstructionSimulator):
    def execute(self) -> RegisterState:
        params = self.params
        if len(params) != 1:
            raise Exception("Invalid parameters for DCR instruction")
        
        register1_name = params[0]
        return AddOperationSimulator.execute([register1_name,-1])

class RstOperationSimulator(InstructionSimulator):
    def execute(self) -> RegisterState:        
        state = RegisterState(self.registers)
        state.reset()
        return state


