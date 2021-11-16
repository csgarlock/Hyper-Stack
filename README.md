stack_max = number of stacks in the enviroment - 1 (aka the index of the last stack)

init n (n >= 1) #inits the enviroment with n stacks.

place n (n is any positive integer) #pushs n to stack[0]

push n (n > 0 and n <= stack_max) #pops stack[n-1] and pushes to stack[n]

pull n (n >= 0 and n < stack_max) #pops stack[n+1] and pushes to [n]

popcop n(n >= 0 and n < stack_max) #pops stack[n] returns pushs back whatever was popped twice

rot n (n is any positive integer) for each integer 0 <= m <= stack_max take stack[m] and put the top n elements on stack[m+1]. If m = stack_max put the top elements on stack[0] instead

inc n (n >= 0 and n <= stack_max) #pops stack[n], add 1 to it then push to stack[n]

dec n (n >= 0 and n) #pops stack[n], subtracts 1 from it then pushes to stack[n]

call f n (0 <= n <= stack_max) #call function f and pushs a copy of stack[n] to that function

callif f n (0 <= n <= stack_max) #pops stack[n] and calls function f only if the popped value = 0

callifnot f n (0 <= n <= stack_max) #pops stack[n] and calls function f only if the popped value != 0

ret n (0 <= n <= stack_max) #pops stack[n] returns from function.

dis #pops stack[stack_max]

Format of a function
stack[0] is a copy of the stack passed into the function

:name
init n #number of stacks in function
~body~
ret n #pops and returns top element 