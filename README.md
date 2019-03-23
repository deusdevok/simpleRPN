# simpleRPN
A very simple Reverse Polish Notation script

RPN stands for Reverse Polish Notation. This is a mathematical notation in which the operators such as ‘+’, ‘-’, ‘/’ and ‘*’, come after the operands, which can be simply numbers. For this reason this is sometimes also called “postfix notation”.

For example, if we want to add two numbers, say 6 and 13, in conventional notation this would be 6 + 13 = 19. In Reverse Polish Notation this is written like 6 13 +.

A more complex example can be ‘1000 990 1 2 + * +’. If we read this line from left to right, the first operator found is ‘+’, right after 1 and 2. So the first step is to add the numbers 1 and 2, which gives 3. At this point we have ‘1000 990 3 * +’. Now the first operator found is ‘*’ right after the 3. Then we make the product between 990 and 3, which is 2970. Now we have ‘1000 2970 +’. Finally, add 1000 with 2970, and the final result is 3970.

To evaluate such expressions in an efficient way, we make use of Stacks. First create an instance of a Stack, this is an empty Stack, and store it in “s”. Define the main operators: ‘+’, ‘-’, ‘/’ and ‘*’, and store them in a list called “ops”. The main idea es to traverse the input string and parse its operands and operators. These are called “tokens”. 

Starting from left to right, we have to “push” each operand (number) onto the stack, until we find an operator. Once we find an operator (by means of an “if” statement), we have to apply that operator to the last two operands before it. This two operands are the last two elements in our Stack (by construction). So we “pop” and save both of them in variables “op1” and “op2”. Finally, simply make the corresponding operation between them, and “push” the result back in the Stack.

Repeating this process for the whole input string (“tokens”) will lead to the final result.

Both time complexity and space complexity are O(n), since each operand or operator is pushed and popped from the Stack only once.
