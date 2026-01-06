class Parser:
    def __init__(self, file_path: str) -> None:
        self.lines = []
        self.current_pos = 0

        with open(file_path, "r") as file:
            for line in file:
                clean_line = line.split("#")[0].strip()
                if len(clean_line) > 0:
                    self.lines.append(clean_line)

        self.final_pos = len(self.lines) - 1

        print(self.lines)
        print(self.final_pos)

    def hasMoreLines(self) -> bool:
        return self.current_pos < self.final_pos

    def advance(self) -> None:
        if self.hasMoreLines():
            self.current_pos += 1

    def instructionType(self) -> str:
        if self.lines[self.current_pos] == "@":
            return "A_INSTRUCTION"
        elif self.lines[self.current_pos] == "(":
            # TODO: improve it with regex
            return "L_INSTRUCTION"
        else:
            # TODO: add regex for C instruction
            return "C_INSTRUCTION"

    def symbol(self) -> str:
        instruction_type = self.instructionType()
        if instruction_type == "A_INSTRUCTION":
            return self.lines[self.current_pos].replace("@", "")
        elif instruction_type == "L_INSTRUCTION":
            return self.lines[self.current_pos].replace("(", "").replace(")", "")
        else:
            raise ValueError("instruction type should not be C for symbol()")

    def dest(self) -> str:
        if self.instructionType() == "C_INSTRUCTION":
            return self.lines[self.current_pos].split("=")[0]
        else:
            raise ValueError("instruction type must be C for dest()")

    def comp(self) -> str:
        if self.instructionType() == "C_INSTRUCTION":
            return self.lines[self.current_pos].split(";")[0].split("=")[1]
        else:
            raise ValueError("instruction type must be C for dest()")

    def jump(self) -> str:
        if self.instructionType() == "C_INSTRUCTION":
            return self.lines[self.current_pos].split(";")[1]
        else:
            raise ValueError("instruction type must be C for dest()")


Parser("text.asm")
