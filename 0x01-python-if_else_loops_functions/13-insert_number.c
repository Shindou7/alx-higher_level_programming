#include "lists.h"

/**
 * insert_node - inserts a new node at a given position.
 * @head: head of a list.
 * @number: number  of the list
 * Return: new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp;
	listint_t *temp_prev;

	temp = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (temp != NULL)
	{
		if (temp->n > number)
			break;
		temp_prev = temp;
		temp = temp->next;
	}

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = temp;
		if (temp == *head)
			*head = new;
		else
			temp_prev->next = new;
	}

	return (new);
}
