"""
binarysearch Module
~~~~~~~~~~~~~~~~~~~~~
Basic search_element usage:
    >>> import binarysearch as bs
    >>> res = bs.search_element([11,14,18,22,28,29],28)
    >>> print(res)
    {'found': True, 'index': 4, 'iter_count': 2}

Assumption: Input Sorted Array
Python Version: 3.7
"""

def search_element(in_array,in_element):
    """
    This is a function for searching element in provided list.
    Input 1: Sorted Array - Python List
    Input 2: Element which you want to search
    Output : Dict Example -> {'found': True, 'index': 4, 'iter_count': 2}
    """

    res = {}

    last_index =len(in_array)

    if last_index>0:
        fist_index = 0
        last_index = last_index - 1
        iter_cnt = 0

        while (fist_index <= last_index):
            iter_cnt += 1
            mid_index = int((fist_index+last_index)/2)
            # print (f" ********* Ieration {iter_cnt} *************")
            # print (f" fist_index {fist_index}, last_index : {last_index}, mid index : {mid_index}, mid value : {in_array[mid_index]}")

            if in_element == in_array[mid_index]:
                res["found"]=True
                res["index"]=mid_index
                res["iter_count"]=iter_cnt
                return res
            elif in_element<in_array[mid_index]:
                last_index = mid_index- 1
            elif in_element>in_array[mid_index]:
                fist_index = mid_index + 1

        res["found"]=False
        res["index"]=None
        res["iter_count"]=iter_cnt        
        return res

    return "Array is empty!"

if __name__ == "__main__":
    x = [1,2,3,4,5,6,7,8,9,10,15,18,26,28,30,33,55,101]
    # print(search_element(x,102))
    # print(search_element(x,10))
    print(search_element([],10))


