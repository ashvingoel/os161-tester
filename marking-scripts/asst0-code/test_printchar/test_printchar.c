#include <stdio.h>
#include <unistd.h>

void test_printchar()
{
	printchar('$');
	printchar('#');
	printchar('@');
	printchar('$');
	printchar('#');
	printchar('@');
	printchar('\n');
}

void test_printf()
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
