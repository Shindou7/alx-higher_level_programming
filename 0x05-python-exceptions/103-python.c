#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_hexn(const char *str, int n);
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_hexn - .....
 * @str: string.
 * @n: ....
 */
void print_hexn(const char *str, int n)
{
	int i;

	for (i = 0; i < n; ++i)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < n - 1)
		{
			printf(" ");
		}
	}
	printf("\n");
	fflush(stdout);
}
/**
 * print_python_bytes - .....
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytesObj = (PyBytesObject *)p;
	Py_ssize_t size = PyBytes_Size(p);
	const char *data = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n",data);
	printf("  first %ld bytes: ", size <= 10 ? size : 10);
	print_hexn(data, size <= 10 ? size : 10);
	fflush(stdout);
}
/**
 * print_python_list - .....
 * @p: A PyObject byte object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t listLen = PyList_Size(p);
	int i;
	const char *typeName;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", (long)listLen);
	printf("[*] Allocated = %ld\n", (long)((PyListObject *)p)->allocated);

	for (i = 0; i < listLen; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);

		typeName = Py_TYPE(item)->tp_name;

		printf("Element %d: %s\n", i, typeName);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
	fflush(stdout);
}
/**
 * print_python_float - .....
 * @p: A PyObject byte object.
 */

void print_python_float(PyObject *p)
{
	double value = PyFloat_AS_DOUBLE(p);

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	/**value = Obj->ob_fval;*/
	printf("  value: %0.16g\n", value);
	fflush(stdout);
}
