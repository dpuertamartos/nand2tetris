from typing import List

from app.Code import Code
from app.Parser import Parser
from app.SymbolTable import SymbolTable


def to_binary(n: int, length: int) -> str:
    return bin(n)[2:].zfill(length)


class Assembler:
    def __init__(self) -> None:
        self.code = Code()

    def run(self, file_name: str) -> None:
        parser = Parser(file_name)
        self.symbols: SymbolTable = self._firstPassParseSymbols(parser)
        parser.reset()
        instructions: List[str] = self._secondPassTranslateInstructions(parser)

        with open(file_name.replace(".asm", ".hack"), "w") as file:
            file.write("\n".join(instructions))

    def _secondPassTranslateInstructions(self, parser: Parser) -> List[str]:
        instructions: List[str] = []

        while parser.hasMoreLines():
            parser.advance()
            i_type = parser.instructionType()
            if i_type == "C_INSTRUCTION":
                d = self.code.dest(parser.dest())
                c = self.code.comp(parser.comp())
                j = self.code.jump(parser.jump())
                r = "111" + c + d + j
                assert len(r) == 16
                instructions.append(r)

            elif i_type == "A_INSTRUCTION":
                a: str = parser.symbol()
                if not a[0].isdigit():
                    symbol_value: int | None = self.symbols.getAddress(a)
                    if symbol_value is not None:
                        a_int = symbol_value
                    else:
                        a_int = self.symbols.addEntryVariable(a)
                else:
                    a_int = int(a)

                a_bin = to_binary(a_int, 16)
                assert len(a_bin) == 16
                instructions.append(a_bin)

        return instructions

    def _firstPassParseSymbols(self, parser: Parser) -> SymbolTable:
        symbol_table = SymbolTable()
        counter: int = 0
        while parser.hasMoreLines():
            parser.advance()
            if parser.instructionType() == "L_INSTRUCTION":
                symbol: str = parser.symbol()
                symbol_table.addEntry(symbol, counter)
            else:
                counter += 1

        parser.reset()
        print(symbol_table.mem)

        return symbol_table
