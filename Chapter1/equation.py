import numpy
'''
    PRML: Chapter1: Equations    
    all function should require numpy object
'''



def polinomial(w):
    '''
        p5, 1.1, polinomial function
        numpy.array: w = w0, w1, w2...wn
        this function return function, not float or integer.
        returned function return float or integer.
        return type tend to values of x and w. 
    '''
    temp = numpy.arange(numpy.size(w))
    return lambda x: numpy.sum(w * (x ** temp))


def sse(func_y, func_t, values_x):
    ''' 
        p5, 1.2, sum-of-squares error
    '''
    return sum((numpy.vectorize(func_y)(values_x) - numpy.vectorize(func_t)(values_x)) ** numpy.int(2)) / numpy.int(2)
    

def rms(sse_value, values_x):
    '''
        p7, 1.3, root-mean-square error
    '''
    return numpy.sqrt(2 * sse_value / numpy.size(values_x))


def error_function(sse_value, lam, w):
    return sse_value + lam * 0.5 * w.dot(w)




if __name__ == "__main__":
    ''
