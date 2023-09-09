#include "lists.h"
/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
    unsigned int count = 0, n = 0;
    listint_t *current;
    current = *head;

    while (current != NULL && count != 5)
    {
        count++;
        current = current->next;
        n++;
    }

    if (count == 5)
    {
        listint_t *new_node = malloc(sizeof(listint_t));
        if (new_node == NULL)
            return NULL;

        new_node->n = number;
        current>next = new->next;
        return (current);
    }

    return current;
}
