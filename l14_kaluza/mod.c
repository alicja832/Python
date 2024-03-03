#include <Python.h>
#include "zad2.h"
//mozliwe sygnatury funkcji stanowiącej "interfejs" pomiędzy pythonem i C
//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){
static PyObject *mod_met(PyObject *self, PyObject *args){
	int a,b,c=0;
	PyObject *d=NULL;
	if(!PyArg_ParseTuple(args, "ii|iO", &a, &b, &c, &d)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	int s=a+b+c;
	if(d){
		int r=PyList_Size(d);
		for(int i=0; i<r; i++){
			s+=PyLong_AsLong(PyList_GetItem(d,i));
		}
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", s);
}
static PyObject *mod_sort(PyObject *self, PyObject *args){
	PyObject *a;
	int b;
	if(!PyArg_ParseTuple(args, "Oi", &a, &b)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	int tab[b];
	if(a){
		for(int i=0; i<b; i++){
			tab[i]=PyLong_AsLong(PyList_GetItem(a,i));
		}
	}
	sort_one(tab,b);
	
		for(int i=0; i<b; i++){
			PyList_SetItem(a,i,PyLong_FromLongLong(tab[i]));
		}

	return Py_BuildValue("O", a);
}
//tablica metod
static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."}, 
	{"sort_one", (PyCFunction)mod_sort, METH_VARARGS, "Funkcja ..."}, 
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
