
def count_word_frequency(words):
    # TODO
    my_dict={}
    for i in words:
        
        if i not in my_dict:
            my_dict[i]=words.count(i)
    return my_dict


def main():
    words=['apple','juice','apple']
    print(count_word_frequency(words))

if __name__ == '__main__':
    main()