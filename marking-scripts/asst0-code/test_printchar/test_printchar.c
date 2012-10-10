#include <stdio.h>
#include <unistd.h>

int test_printchar()
{
	printchar('$');
	printchar('#');
	printchar('@');
	printchar('$');
	printchar('#');
	printchar('@');
	printchar('\n');
}

int test_printf()
{
	printf("SYS161 OS TESTER FOR PRINTF\n");
}

int main(void)
{
	/*
	 * Test printchar
	 */
	test_printchar();
	test_printf();
	return 0;
}
