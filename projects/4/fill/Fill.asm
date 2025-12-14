// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.
(START_LOOP)
    @KBD
    D=M

    @BLACK_SCREEN
    D;JNE
    
    @COLOR
    M=0

    @PAINT
    0;JMP

    (BLACK_SCREEN)
    @COLOR
    M=-1

    (PAINT)
    @SCREEN
    D=A
    @SCREEN_ADDRESS_POINTER
    M=D

    @8192
    D=A
    @COUNTER
    M=D

    (PAINT_LOOP)
    @COUNTER
    D=M
    @START_LOOP
    D;JEQ

    @COLOR
    D=M

    @SCREEN_ADDRESS_POINTER
    A=M
    M=D

    @SCREEN_ADDRESS_POINTER
    M=M+1

    @COUNTER
    M=M-1

    @PAINT_LOOP
    0;JMP
(END_LOOP)

@END_LOOP
0;JMP