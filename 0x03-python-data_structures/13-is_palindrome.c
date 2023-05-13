#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * reverse_listint - reverse a listint_t list
 * @h: pointer to pointer to the first element of the list
 *
 * Return: the pointer to the first element of the reverse list
 */
listint_t *reverse_listint(listint_t **h)
{
	listint_t *next, *prev = NULL;

	while (*h != NULL)
	{
		next = (*h)->next;
		(*h)->next = prev;
		prev = *h;
		*h = next;
	}
	*h = prev;
	return (*h);
}

/**
 * is_palindrome - checks if a listint_t is a palindrome
 * @head: pointer to pointer to the first element of the listint_t
 *
 * Return: 1 if a palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *p, *q, *sec_part;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	p = *head, q = *head;
	while (p && p->next)
	{
		p = p->next->next;
		if (p == NULL)
		{
			sec_part = q->next;
			break;
		}
		if (p->next == NULL)
		{
			sec_part = q->next->next;
			break;
		}
		q = q->next;
	}
	q->next = NULL;
	sec_part = reverse_listint(&sec_part);
	while (*head != NULL && sec_part != NULL)
	{
		if ((*head)->n != sec_part->n)
			return (0);
		*head = (*head)->next;
		sec_part = sec_part->next;
	}
	return (1);
}
