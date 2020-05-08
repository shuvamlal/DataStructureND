def heapsort(arr):
    arr_len = len(arr)

    for i in range(arr_len - 1, -1, -1):
        heapify(arr, len(arr), i)

        # Swap the top element in heap with last element in array
        arr[0], arr[i] = arr[i], arr[0]


def heapify(arr, n, i):
    for i in range(1, i + 1):
        # Perform heapify processing
        data_index = i
        while data_index > 0:
            parent_index = (data_index - 1) // 2
            if arr[data_index] > arr[parent_index]:
                arr[data_index], arr[parent_index] = arr[parent_index], arr[data_index]
                data_index = parent_index
            else:
                break
        
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    heapsort(input_list)
#     print(input_list)
    sum1, sum2 = '', ''
    for i in range(len(input_list)-1, -1,-1):
        if i%2==0:
            sum1 += str(input_list[i])
        else:
            sum2 += str(input_list[i])
    return (int(sum1), int(sum2)) if int(sum1) > int(sum2) else (int(sum2), int(sum1))

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[0, 1, 0, 1, 0], [100, 10]])           # print Pass
test_function([[1, 2, 3, 4, 5], [542, 31]])           # print Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])           # print Pass
test_function([[0, 0, 1, 3, 8, 9, 7, 6, 4, 4, 5], [975410, 86430]])           # print Pass