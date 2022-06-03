#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts node to a sorted list
 * @head: pointer to pointer to first node of list
 * @number: integer to be added to the new node
 *
 * Return: address of new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *tmp;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	current = *head;

	while (current)
	{
		if (current->n >= number)
		{
			new->next = current;
			current = new;
			break;
		}
		else if (!current->next)
			current->next = new;

		else if (current->next && current->next->n < number)
			current = current->next;
		else
		{
			tmp = current->next;
			current->next = new;
			new->next = tmp;
			break;
		}
	}
	return (new);
}
