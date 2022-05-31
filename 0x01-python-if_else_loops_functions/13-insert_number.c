#include "lists.h"

/**
* insert_node - inserts a number in a sorted singly-linked list
* @head: head
* @number: int to add
* Return: pointer to head of the linked list
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp = *head;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	if (!*head)
	{
		*head = new;
		new->n = number;
		new->next = NULL;
		return (new);
	}
	if (number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (tmp->next)
		{
			if (number <= tmp->next->n)
			{
				new->next = tmp->next;
				tmp->next = new;
				return (new);
			}
			tmp = tmp->next;
		}
	}
	new->next = NULL;
	tmp->next = new;
	return (new);
}
