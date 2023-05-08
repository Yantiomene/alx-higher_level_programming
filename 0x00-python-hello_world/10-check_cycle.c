#include "lists.h"

/**
 * check_cycle - checks if a listint_t has a cycle in it.
 * @list: pointer to the listint_t needed to be checked
 *
 * Return: 0 if there is no cycle and 1 if there is.
 */
int check_cycle(listint_t *list)
{
	listint_t *p1, *p2;

	p1 = list;
	p2 = list;
	while (p1 && p2 && p2->next)
	{
		p1 = p1->next;
		p2 = (p2->next)->next;
		if (p1 == p2)
			return (1);
	}
	return (0);
}
