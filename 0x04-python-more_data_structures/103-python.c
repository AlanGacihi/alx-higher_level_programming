#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
/**
 * print_python_list - Prints info about Python lists.
 * @p: Python object.
 */
void print_python_list(PyObject *p)
{
	int i;

	puts("[*] Python list info");
	printf("[*] Size of the Python List = %d\n", (int)PyList_Size(p));
	printf("[*] Allocated = %d\n", (int)(((PyListObject *)p)->allocated));
	for (i = 0; i < (int)PyList_Size(p); i++)
	{
		printf("Element %d: %s\n", i, PyList_GET_ITEM(p, i)->ob_type->tp_name);
		if (!strcmp(PyList_GET_ITEM(p, i)->ob_type->tp_name, "bytes"))
			print_python_bytes(PyList_GET_ITEM(p, i));
	}

}

/**
 * print_python_bytes - Prints info about Python bytes.
 * @p: Python object.
 */
void print_python_bytes(PyObject *p)
{
	int bytes, i;

	puts("[.] bytes object info");
	if (!PyBytes_Check(p))
	{
		puts("  [ERROR] Invalid Bytes Object");
		return;
	}
	printf("  size: %ld\n", PyBytes_Size(p));
	if (PyBytes_Size(p) > 0)
	{
		printf("  trying string: %s\n", PyBytes_AsString(p));
		bytes = PyBytes_Size(p) + 1;
		if (bytes > 10)
			bytes = 10;
		printf("  first %d bytes:", bytes);
		for (i = 0; i < bytes; i++)
			printf(" %02x", (unsigned char)*(PyBytes_AsString(p) + i));
		puts("");
	}
}
