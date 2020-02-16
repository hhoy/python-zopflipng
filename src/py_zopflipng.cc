#include "../zopfli/src/zopflipng/zopflipng_lib.h"
#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

extern "C" {

static char docs[] = "";

static PyObject * PNGOptimize(PyObject *self,PyObject *args){
    PyBytesObject *buffer;
    bool verbose=true;
    bool lossy_transparent;
    bool lossy_8bit;
    const char * filter_strategies;
    PyListObject *keepchunks;
    bool use_zopfli=true;
    int num_iterations;
    int num_iterations_large;
    
    // https://docs.python.org/zh-cn/3.8/c-api/arg.html#c.PyArg_ParseTuple
    if (!PyArg_ParseTuple(args, "S|pppzOpii", &buffer,&verbose,&lossy_transparent,&lossy_8bit,&filter_strategies,&keepchunks,&use_zopfli,&num_iterations,&num_iterations_large))
        return NULL;
    char *origpng_buffer =PyBytes_AS_STRING(buffer);
    Py_ssize_t length =PyBytes_GET_SIZE(buffer);
    
    const std::vector<unsigned char> origpng(origpng_buffer, origpng_buffer + length);
    std::vector<unsigned char> resultpng;

    ZopfliPNGOptions png_options;
    png_options.lossy_transparent =lossy_transparent;
    png_options.lossy_8bit =lossy_8bit;

    if(filter_strategies){
        for (size_t j = 0,count=strlen(filter_strategies); j < count; j++) {
          ZopfliPNGFilterStrategy strategy = kStrategyZero;
          char f = filter_strategies[j];
          switch (f) {
            case '0': strategy = kStrategyZero; break;
            case '1': strategy = kStrategyOne; break;
            case '2': strategy = kStrategyTwo; break;
            case '3': strategy = kStrategyThree; break;
            case '4': strategy = kStrategyFour; break;
            case 'm': strategy = kStrategyMinSum; break;
            case 'e': strategy = kStrategyEntropy; break;
            case 'p': strategy = kStrategyPredefined; break;
            case 'b': strategy = kStrategyBruteForce; break;
            default:
              printf("Unknown filter strategy: %c\n", f);
              continue;
          }
          png_options.filter_strategies.push_back(strategy);
          // Enable auto filter strategy only if no user-specified filter is
          // given.
          png_options.auto_filter_strategy = false;
    }
    }
    if((void *)keepchunks!=Py_None){
        for(size_t i =0, count =PyList_GET_SIZE(keepchunks);i<count; i++){
            PyObject *pychunk = PyList_GET_ITEM(keepchunks,i);
            const char *chunk;
            if(!PyArg_Parse(pychunk,"s",&chunk)){
                printf("chunks item type should be string");
                return NULL;
            }
            png_options.keepchunks.push_back(chunk);
        }
    }
    png_options.use_zopfli =use_zopfli;
    png_options.num_iterations =num_iterations;
    png_options.num_iterations_large=num_iterations_large;

    int ret = ZopfliPNGOptimize(origpng, png_options, verbose, &resultpng);
    PyObject *result_bytes = PyBytes_FromStringAndSize((char*)&resultpng[0],resultpng.size());
    return result_bytes;
}

static PyMethodDef Methods[] = {
    {"zopfli_png_optimize", PNGOptimize, METH_VARARGS}, 
    {NULL, NULL}
};

static struct PyModuleDef module = {
	PyModuleDef_HEAD_INIT,
	"zopflipng._clib", /*module name*/
	docs, /* module documentation, may be NULL */
	-1, /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
	Methods
};

PyMODINIT_FUNC PyInit__clib(void){
    PyObject *m;
    m = PyModule_Create(&module);
    return m;
}

}