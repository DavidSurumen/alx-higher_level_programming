#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	tmp = list;
	while (tmp->next != NULL)
	{
		if (tmp->next == list)
			return (1);
		tmp = tmp->next;
	}
	return (0);
}
