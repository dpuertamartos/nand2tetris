class Code:
    def __init__(self) -> None:
        self.memory = {
            # Destination (3 bits): d1 d2 d3 (A D M)
            "dest": {
                "null": "000",
                "M": "001",
                "D": "010",
                "MD": "011",
                "A": "100",
                "AM": "101",
                "AD": "110",
                "AMD": "111",
            },
            # Computation (7 bits): a c1 c2 c3 c4 c5 c6
            # a=0 corresponds to operations with A
            # a=1 corresponds to operations with M
            "comp": {
                "0": "0101010",
                "1": "0111111",
                "-1": "0111010",
                "D": "0001100",
                "A": "0110000",
                "!D": "0001101",
                "!A": "0110001",
                "-D": "0001111",
                "-A": "0110011",
                "D+1": "0011111",
                "A+1": "0110111",
                "D-1": "0001110",
                "A-1": "0110010",
                "D+A": "0000010",
                "D-A": "0010011",
                "A-D": "0000111",
                "D&A": "0000000",
                "D|A": "0010101",
                "M": "1110000",
                "!M": "1110001",
                "-M": "1110011",
                "M+1": "1110111",
                "M-1": "1110010",
                "D+M": "1000010",
                "D-M": "1010011",
                "M-D": "1000111",
                "D&M": "1000000",
                "D|M": "1010101",
            },
            "jump": {
                "null": "000",
                "JGT": "001",
                "JEQ": "010",
                "JGE": "011",
                "JLT": "100",
                "JNE": "101",
                "JLE": "110",
                "JMP": "111",
            },
        }

    def dest(self, d: str) -> str:
        if not d:
            d = "null"
        r = self.memory["dest"][d]
        assert len(r) == 3 and isinstance(r, str)
        return r

    def comp(self, c: str) -> str:
        r = self.memory["comp"][c]
        assert len(r) == 7 and isinstance(r, str)
        return r

    def jump(self, j: str) -> str:
        if not j:
            j = "null"
        r = self.memory["jump"][j]
        assert len(r) == 3 and isinstance(r, str)
        return r


c = Code()
