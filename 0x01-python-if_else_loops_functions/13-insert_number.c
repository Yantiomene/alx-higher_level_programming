#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list.
 * @head: pointer to pointer of the head of the list
 * @number: number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head, *prev;
	int i;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (current->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	for (i = 0; current->n <= number && current->next != NULL; i++)
	{
		prev = current;
		current = current->next;
	}
	if (current->next == NULL)
	{
		current->next = new;
		return (new);
	}
	new->next = current;
	prev->next = new;
	return (new);
}
