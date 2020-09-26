#Program on count_frequency that takes a list of words as an argument, and count how many times it appears in the list.
def Count_frequency(mylist):
    freq = {}
    for i in ['one','two','eleven','one','three','two','eleven','three','seven','eleven']:
        freq[i] = freq.get(i, 0) + 1
    return freq
    

if __name__ == "__main__":
    mylist = ['one','two','eleven','one','three','two','eleven','three','seven','eleven']
    print(Count_frequency(mylist))
