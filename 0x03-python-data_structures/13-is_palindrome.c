#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Double pointer to the first element on the list.
 * Return: 1 if list is palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, j, N[1000];

	if (!head || !*head)
		return (1);

	i = 0;
	current = *head;
	while (current->next)
	{
		N[i++] = current->n;
		current = current->next;
	}

	for (j = 0; j < i; j++, i--)
		if (N[j] != N[i - 1])
			return (0);
	return (1);
}
