#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list, *new_tmp = list->next;

	while (tmp && new_tmp && new_tmp->next)
	{
		if (tmp == new_tmp)
			return (1);
		tmp = tmp->next;
		new_tmp = new_tmp->next->next;
	}
	return (0);
}
