// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

//// Replace this comment with your code.
@R2
M=0

(START_LOOP)
    @R1
    D=M
    @END_LOOP
    D;JEQ

    // ADD R0 TO R2
    @R0
    D=M        // Get R0
    @R2
    M=D+M      // R2 = R0 + R2

    // DECREMENT R1
    @R1
    M=M-1

    // REPEAT
    @START_LOOP
    0;JMP

(END_LOOP)
    @END_LOOP
    0;JMP