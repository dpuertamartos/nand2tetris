from typing import TextIO

from app.Code import Code
from app.Parser import Parser


def to_binary(n: int, length: int) -> str:
    return bin(n)[2:].zfill(length)


class Assembler:
    def __init__(self) -> None:
        self.code = Code()

    def run(self, file_name: str) -> None:
        parser = Parser(file_name)

        with open(file_name.replace(".asm", ".hack"), "w") as file:
            while parser.hasMoreLines():
                parser.advance()
                self.writeInstruction(parser, file)

    def writeInstruction(self, parser: Parser, file: TextIO) -> None:
        i_type = parser.instructionType()
        if i_type == "C_INSTRUCTION":
            d = self.code.dest(parser.dest())
            c = self.code.comp(parser.comp())
            j = self.code.jump(parser.jump())
            r = "111" + c + d + j
            assert len(r) == 16
            file.write(r + "\n")

        elif i_type == "A_INSTRUCTION":
            a = parser.symbol()
            a = to_binary(int(a), 16)
            assert len(a) == 16
            file.write(a + "\n")

        elif i_type == "L_INSTRUCTION":
            pass
