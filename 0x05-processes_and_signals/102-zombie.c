#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

int infinite_while(void);

/**
 * infinite_while - puts the main function in an infinite sleep
 * Return: 0
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: integer (0)
*/

int main(void)
{
	int i = 0;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();
	return (0);
}
