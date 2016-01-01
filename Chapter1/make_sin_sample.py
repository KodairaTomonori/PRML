import numpy
import sys
import matplotlib.pyplot as pyplot



def get_sample(sample_num=10, func=numpy.sin):
    rand = lambda x, min=0, error=0.05: numpy.arange((0 - min), 1, (1. + min)/x) \
        + numpy.random.uniform(-error, error, x)
    sample_array1 = numpy.sin(rand(sample_num, 1, 0.0001) * -3.14)
    sample_array2 = rand(sample_num, 0, 0.1)
    pyplot.scatter(sample_array2, sample_array1)
    pyplot.plot(numpy.arange(0, 1, 0.01), numpy.sin(numpy.arange(-1, 1, 0.02) * -3.14)) 
    
    pyplot.show()

if __name__ == "__main__":
    # get sample num
    try: sample_num = int(sys.argv[1])
    except: sample_num = 10
    print(repr(get_sample(sample_num=sample_num)))
    
