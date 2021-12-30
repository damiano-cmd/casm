global _start

section .data
    msg db "hello", 0x0a

section .text
_start:

    mov eax, 4
    cmp eax, 1
    jle quit

    mov ebx, 1
    mov ecx, msg
    mov edx, 6
    int 0x80

quit:
    mov eax, 1
    mov ebx, 0
    int 0x80