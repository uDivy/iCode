def nextGreaterElement(array):
    # Write your code here.
    out = [0]*len(array)
    for i in range(len(array)):
        if array[i] == max(array):
            out[i] = -1
            continue
        sub_arr = array[i+1:len(array)] + array[0:i]
        for ele in sub_arr:
            if ele > array[i]:
                out[i] = ele
                break
	return out