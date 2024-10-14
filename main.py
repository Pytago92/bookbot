def main():
    path = "/home/pytago/Workspace/github.com/Pytago92/bookbot/books/frankenstein.txt"
    text = book_text(path)
    number = counted_words(text)
    letters = total_letters(text)
    alphabet_letters = sorting_dic(letters)
    print(f"--- Begin report of {path} ---")
    for i in range(len(alphabet_letters)):
        if i == 0:
            print(f"{number} words found in the document")
    for a in alphabet_letters:
        print(f"The {a} character was found {alphabet_letters[a]} times")
        
    print("--- End report ---")

def book_text(path):
    with open(path) as f:
        return f.read()

    
def counted_words(text):
    words = text.split()
    return len(words)

def total_letters(text):
    letters = {}
    for l in sorted(text.lower()):
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

def sorting_dic(letters):
    
    dic = {}
    for a in letters:
        if a in letters and a.isalpha():
            dic[a] = letters[a]
    return dic

















main()