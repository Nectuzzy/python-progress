# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    file_content=open(filename)
    words=file_content.read()
    return words
    

def count_words():
    text = read_file_content("./story.txt")
    new_text=text.replace('.','').replace(',','').replace('?','')
    # [assignment] Add your code here
    nectuzzy_dict={}
    for word in new_text.split():
        if word not in nectuzzy_dict:
            nectuzzy_dict[word]=1
        else:
            nectuzzy_dict[word]+=1
    return nectuzzy_dict

print(read_file_content("story.txt"))

print(count_words())
