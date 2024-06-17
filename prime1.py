def filtzeroDiv(func):
    def wrapper(arr_data):
        filtered_data = [n for n in arr_data if n != 0]
        return func(filtered_data)
    return wrapper

@filtzeroDiv
def PrimeNum(arr_data):
    for ind in range(len(arr_data)):
        for div in range(2, arr_data[ind] // 2 + 1):
            if arr_data[ind] % div == 0:
                break
        else:
            print(arr_data[ind])

if __name__ == "__main__":
    data = [n for n in range(20)]
    PrimeNum(data)
