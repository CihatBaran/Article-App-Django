import time


def time_calc_dec(param_func):
    def wrapper(num_arr):
        start = time.time()
        result = param_func(num_arr)
        finish = time.time()

        return str(num_arr)+" to calculate the square of the each element => "+str(result)+" to this, " + str(finish-start) + " took to execute"
    return wrapper


@time_calc_dec
def square_calc(num_arr):
    return [(lambda x: x*x)(x) for x in num_arr]


myarr = [1, 2, 3, 4, 5]
print(square_calc(myarr))
