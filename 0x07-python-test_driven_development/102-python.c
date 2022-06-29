#include <Python.h>
#include <stdio.h>
void print_python_string(PyObject *p)
{
    puts("[.] string object info");
    printf("  type: %s\n", (char *)PyUnicode_AsUnicode(p));
}
