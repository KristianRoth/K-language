; To convert this assembly code to an executable file (machine language) and execute it, run:
; /usr/local/bin/nasm -f macho64 64.asm && ld -macosx_version_min 10.7.0 -lSystem -o 64 64.o && ./64

global start

section .text

start:
    mov     rax, 0x2000004 ; write
    mov     rdi, 1 ; stdout
    lea     rsi, [rel msg]
    mov     rdx, msg.len
    syscall


    mov     rax, 0x2000001 ; exit
    mov     rdi, 0
    syscall

; The .data section is for storing and naming constants.
section .data

msg:    db      "Hello, world!", 10
; Length of `msg`. `$` refers to the address of this constant, so `$ - msg` is the length of message
.len:   equ     $ - msg