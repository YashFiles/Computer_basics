section .data

;this line defines a data where you can initalize data(variables).
;Variables declared here will have a fixed value throughout the program

num db 5   ; number to calculate factorial for

; num is a variable that holds the value 5. The db directive
; stands for "define byte", which reserves a byte of space
;for the variable.

result db 1   ;variable to store the result

; result is initialized to 1, which will store the calculated factorial

msg db 'Factorial: ', 0

msg_result db 'Result: ', 0

msg_length db 10
msg_length_result db 10

section .text

global _start
_start:

movzx rax, byte [num]  ; Load num into rax
mov rbx, rax  ; store the current number in rbx

mov rax, 1   ; Initize result to 1
.factorial_loop: 

; this label marks the beginning of the lop for calculaing the factorial_loop

cmp rbx, 1   ;compare rbx with 1
jle .done   ;if rbx <= 1, we're done

mul rbx     ; multiply rax(result) by rbx
dec rbx     ; decrease rbx by 1

jmp .factorial_loop   ; repeat the factorial_loop
; The jmp instruction jumps back to the .factorial_loop label, repeating
; the loop until rbx is less than or equal to 1.

.done: ;ending the program

mov rdi, msg  ; Load address of the message
call print_string  ; Call print function for message

mov rdi, rax   ; Move the result (factorial)  to rdi for printing  
call print_string  ; Call print function for message

; Exit the program
mov rax, 60   ; syscall number for sys_exit
xor rdi, rdi   ; exit code
syscall      ; call teh kernel

print_string:

mov rax, 1  ; syscall number for sys_write
mov rdi, 1  ; file descriptor 1 (stdout)
mov rsi, rdi   ; Load address of the string  
mov rdx, msg_length   ; Length of the message
syscall      ; call the   kernel
ret 

print_result:
