#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
	char *data;
	long int length, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	length = ((PyVarObject *)(p))->ob_size;
	data = ((PyBytesObject *)p)->ob_sval;

	printf("  length: %ld\n", length);
	printf("  trying data: %s\n", data);

	if (length >= 10)
		limit = 10;
	else
		limit = length + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (data[i] >= 0)
			printf(" %02x", (unsigned char)data[i]);
		else
			printf(" %02x", 256 + data[i]);
	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *python_list;
	PyObject *element;

	size = ((PyVarObject *)(p))->ob_size;
	python_list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", python_list->allocated);

	for (i = 0; i < size; i++)
	{
		element = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((element)->ob_type)->tp_name);
		if (PyBytes_Check(element))
			print_python_bytes(element);
	}
}
