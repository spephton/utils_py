import time

DEFAULT_ITERS = 1000000
LESS_ITERS = 10000

def main():
    
    short_test_string = "zigzag"
    test_string = "This is an example of Speex, an audio compression codec " +\
        "specifically tuned for the reproduction of human speech."
    long_test_string: str

    with open('bee_movie_script.txt') as jerry: # BYO, mine is the first 12 KB
        lines = jerry.readlines()
        long_test_string = '\n'.join(lines)         
    

    ## Functions

    functions = []

    def comprh(a_string) -> list[str]:
        strarr = [c for c in a_string]
        return strarr

    functions.append(comprh)

    def unpack(a_string) -> list[str]:
        strarr = [*a_string]
        return strarr

    functions.append(unpack)

    def forlst(a_string) -> list[str]:
        strarr = []
        for letter in a_string:
            strarr.append(letter)
        return strarr

    functions.append(forlst)

    def castls(a_string) -> list[str]:
        strarr = list(a_string)
        return strarr

    functions.append(castls)

    def extend(a_string) -> list[str]:
        strarr: list[str] = []
        strarr.extend(a_string)
        return strarr

    functions.append(extend)

    

    

    def benchmark_string(n_trials, test_string, print_iter = True, iterations = DEFAULT_ITERS):
        cmp_result = None
        result = None
        exec_times = {f.__name__: [] for f in functions}

        for _ in range(n_trials):
            for f in functions:
                exec_time, result = time_function(f, (test_string,), iterations)
                exec_times[f.__name__].append(exec_time)
                if cmp_result == None:
                    cmp_result = result
                elif cmp_result != result:
                    etext = f'Function "{f.__name__}" is not equivalent ' + \
                        f'to first function, "{functions[0].__name__}".'
                    raise FunctionEquivalenceException(etext)
                if print_iter:
                    print(f'{f.__name__}: {exec_time}')
        return exec_times

    n = 2
    print(f'Testing each function with short string: {short_test_string}')
    short_exec_times = benchmark_string(n, short_test_string)
    
    print(f'Testing each function with medium-length string:')
    print(test_string)
    exec_times = benchmark_string(n_trials = n, test_string = test_string)

    print('Testing each function with the Bee Movie script:')
    long_exec_times = benchmark_string(n, long_test_string, iterations=LESS_ITERS)
    
    for table, title in zip([short_exec_times, exec_times, long_exec_times],
                            ['short', 'regular', 'long']):    
        print(f'Perfomance of each function with {title} strings:')
        for fname, times in table.items():
            print(f'{fname}: {times}')
        print('\n')

def time_function(
        f: callable,
        args: tuple[any, ...] = (),
        iterations: int = DEFAULT_ITERS):
    '''Time wall clock exec time of a function over many iterations
    
    f: your target function
    args: args your function will be called with i.e. f(*args)
    iterations: n of times to call function while timing

    Returns a tuple containing: total execution time of n iterations of
    the function (sec), and the return value of the last iteration.
    '''
    now = time.time()
    for _ in range(iterations):
        fn_return = f(*args)
    later = time.time()
    return later - now, fn_return
            
class FunctionEquivalenceException(Exception):
    pass



if __name__ == "__main__":
    main()