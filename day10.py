def bubble_sort(a_list):
    list_length = len(a_list)-1
    for i in range (list_length):
        for j in range (list_length):
            if a_list[j] > a_list[i]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
        return a_list

