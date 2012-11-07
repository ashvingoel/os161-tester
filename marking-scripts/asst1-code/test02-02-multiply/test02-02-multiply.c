/*
 * Test 02 program to multiply two numbers: one as global variable, the other as 
 * local variable, both from the argument. Used to
 * test argument passing to child processes, test execv() system call implementation.
 *
 * test02-02-multply
 *
 * Test case:
 *      run: p /testbin/test02-02-multiply 3 5
 *      result expected: 15
 */

#include <stdio.h>
#include <stdlib.h>
#include <err.h>

int mult1 = 0;

int
main(int argc, char *argv[])
{
	int mult2;

    if ( argc != 3 )
        return -1;

    mult1 = atoi(argv[1]);
	mult2 = atoi(argv[2]);

	printf("%d\n", mult1 * mult2);

	return 0;
}
