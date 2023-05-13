#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - print python list information
 * @p: pointer to a Python object
 *
 */
void print_python_list_info(PyObject *p)
{
	size_t size, i;
	PyListObject *list;
	PyObject *item;

	size = PyList_Size(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
