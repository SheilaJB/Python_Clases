import ctypes

def funcion(a,b):
    c = a*a*a+b*b*b
    return c 

if __name__ == '__main__':

    lib = ctypes.CDLL('./lib_funcion.so')
    lib.func.argtypes = [ctypes.c_double, ctypes.c_int]
    lib.func.restype = ctypes.c_double
    a = -8.8197246129836
    b = 40
    print(funcion(a,b))
    print(lib.func(a,b))

