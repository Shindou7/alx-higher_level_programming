#include "/usr/include/python3.8/Python.h"
#include <stdio.h>
#include <stdlib.h>

void print_hexn(const char *str, int n);
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
* print_hexn - .....
* @p: A PyObject byte object.
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
    int size = PyBytes_Size(p);

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %d\n", size);
    printf("  trying string: %s\n", bytesObj->ob_sval);
    printf("  first %d bytes: ", size <= 10 ? size : 10);
    print_hexn(bytesObj->ob_sval, size <= 10 ? size : 10);
    fflush(stdout);
}
/**
 * print_python_list - .....
 * @p: A PyObject byte object.
 */
void print_python_list(PyObject *p)
{   
    int listLen = PyList_Size(p), i;
  const char *typeName;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Size of the Python List = %d\n", listLen);
    printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < listLen; ++i)
    {
        PyObject *item = PyList_GetItem(p, i);
        typeName = item->ob_type->tp_name;
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
  PyFloatObject *Obj = (PyFloatObject *)p;
  float Obj;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    double value = Obj->ob_fval;
    printf("  value: %0.16g\n", value);
    fflush(stdout);
}
