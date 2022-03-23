import time

def calculate_time():
    start_time = time.time()

    #test
    '''for i in range(5):
        for j in range(5):
            for k in range(100):
                print('done')'''

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    calculate_time()