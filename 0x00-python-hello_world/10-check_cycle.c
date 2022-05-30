#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks for cycle in a linked list
 * @list: linked list to check
 * Return: 1 if cycle, 0 if not
 */
int check_cycle(listint_t *list)
{

	if (!list)
		return (0);
	while (1)
	{
		if (list->next >= list || !list->next)
			break;
		list = list->next;
	}
	if (list->next)
		return (1);
	return (0);
}
