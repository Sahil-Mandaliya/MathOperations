import unittest

from opcode_executor.service.opcode_simulator import OpcodeSimulator


class OpCodeSimulatorTest(unittest.TestCase):
    def setUp(self) -> None:
        # TODO initiate the class
        self.opcode_simulator = OpcodeSimulator()

    def test_set_instructions(self):
        instructions = ["RST", "SET A 1", "SET B -2", "SET C 3", "SET D 4"]
        state = self.opcode_simulator.execute(instructions)
        self.assertEqual(1, state.get_register('A').value)
        self.assertEqual(-2, state.get_register('B').value)
        self.assertEqual(3, state.get_register('C').value)
        self.assertEqual(4, state.get_register('D').value)

    def test_add_value_instructions(self):
        instructions = ["RST", "SET A 11", "ADD A -12"]
        state = self.opcode_simulator.execute(instructions)
        self.assertEqual(-1, state.get_register('A').value)

    def test_add_register_instructions(self):
        instructions = ["RST", "SET C 5", "SET D 2", "ADR C D"]
        state = self.opcode_simulator.execute(instructions)
        self.assertEqual(7, state.get_register('C').value)

    def test_mov_register_instructions(self):
        instructions = ["RST", "SET A 5", "SET B 2", "SET D 12", "MOV B A", "MOV D B"]
        state = self.opcode_simulator.execute(instructions)
        self.assertEqual(5, state.get_register('B').value)
        self.assertEqual(5, state.get_register('D').value)

    def test_inc_dec_register_instructions(self):
        instructions = ["RST", "SET A 5", "SET B 2", "INR A", "DCR B", "MOV D B"]
        state = self.opcode_simulator.execute(instructions)
        self.assertEqual(6, state.get_register('A').value)
        self.assertEqual(1, state.get_register('B').value)

    def test_reset_register_instructions(self):
        instructions = ["RST", "SET A 1", "SET B -2", "SET C 3", "SET D 4", "RST"]
        state = self.opcode_simulator.execute(instructions)
        self.assertEqual(0, state.get_register('A').value)
        self.assertEqual(0, state.get_register('B').value)
        self.assertEqual(0, state.get_register('C').value)
        self.assertEqual(0, state.get_register('D').value)

    def test_multiple_instructions_with_no_op(self):
        instructions = ["RST", "SET A 10", "SET B 14", "ADD B 12", "INR A", "# Decrementing", "DCR B"]
        state = self.opcode_simulator.execute(instructions)
        self.assertEqual(11, state.get_register('A').value)
        self.assertEqual(25, state.get_register('B').value)
