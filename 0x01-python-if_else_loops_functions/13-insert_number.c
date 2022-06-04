#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

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
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;

	else if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		current = *head;
		while (current)
		{
			if (current->next == NULL && number != '\0')
			{
				current->next = new;
				break;
			}

			if (current->next->n >= number)
			{
				new->next = current->next;
				current->next = new;
				break;
			}

			current = current->next;
		}
	}
	return (new);
}
