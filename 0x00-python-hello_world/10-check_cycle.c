#include "lists.h"

/**
 * check_cycle - checks if a singly linked list.
 * @list: pointer to the list
 * Return: 0 is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *chaser2 = list;
	listint_t *winner = list;

	while (list && chaser2 && chaser2->next)
	{
		list = list->next;
		chaser2 = chaser2->next->next;

		if (list == chaser2)
		{
			list = winner;
			winner =  chaser2;
			while (1)
			{
				chaser2 = winner;
				while (chaser2->next != list && chaser2->next != winner)
				{
					chaser2 = chaser2->next;
				}
				if (chaser2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
