import string

#Words to ignore in the user input
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']

#Removes the unnecessary words from the user's input
def filter_words(words, skip_words):
    filtered_list = []
    for x in words:
        if x not in skip_words:
            filtered_list.append(x)
    return filtered_list

#Remove punctuation from the user's input    
def remove_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct

#Removes punctuation and filters the skip words from the user input
def normalise_input(user_input):
    no_punct = remove_punct(user_input).lower()
    word_list = filter_words(no_punct.split(), skip_words)       
    return word_list