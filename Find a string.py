def count_substring(string, sub_string):
    
    counter = 0
    for i in range(len(string)):
        if i == string.find(sub_string,i,len(string)):
            counter += 1
        else:
            pass
    return counter