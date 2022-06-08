#include <stdlib.h>
#include "lists.h"

/**
 * reverse - reverses a linked list
 * @head: pointer to pointer to the first node
 *
 * Return: head pointer, pointing to reversed list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *front;
	listint_t *back;

	back = *head;
	*head = (*head)->next;
	back->next = NULL;

	front = *head;
	*head = (*head)->next;

	while (1)
	{
		if (*head == NULL)
		{
			front->next = back;
			*head = front;
			break;
		}
		front->next = back;
		back = front;

		front = *head;
		*head = (*head)->next;
	}
	return (*head);
}

/**
 * is_paplindrome - checks if a singly linked list is palindrome
 * @head: pointer to pointer to list's first node
 *
 * Description: An empty list is considered a palindrome
 *
 * Return: 1 if it's a palindrome, or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp; /* traverse the list to get its length */
	listint_t *front; /* upper half of the list */
	listint_t *back; /* lower half */

	listint_t *tmp_front; 		/* traverse the upper half of the list */

	int n;	/* length of the list */
	int half = 0;
	int palind = 1;

	if (!(*head))
		return (0);
	
	tmp = *head;
	n = 0;
	while (tmp != NULL)
	{
		tmp = tmp->next;
		n++;
	}

	back = front = *head;

	while (half < n/2)
	{
		front = front->next;
		half++;
	}

	reverse(&front);	/* reverse the upper half of the list */
	tmp_front = front;

	while (tmp_front != NULL)
	{
		if (tmp_front->n != back->n)
		{
			palind = 0;
			break;
		}
		tmp_front = tmp_front->next;
		back = back->next;
	}
	reverse(&front);	/* reconstitute the original list */

	if (palind == 0)
		return (0);
	return (1);
}
