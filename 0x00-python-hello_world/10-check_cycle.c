#include "lists.h"

#include <stdlib.h>
/**
 * check_cycle - Finds the loop in a linked list.
 * @list: Pointer to list.
 * Return: 1 if loop found, or 0 if there is no loop.
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
