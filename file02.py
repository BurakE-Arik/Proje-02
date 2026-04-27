#harf counter

alphabet_lower_case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","x","w",]
alphabet_upper_case = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","X","W"]


def case_sensitive_counter(word,char):
    char_count = 0
    
    for i in word:
        if char == i:
            char_count += 1
            
    return f"{char} char found {char_count} times in {word}"

def not_case_sensitive_counter(word,char):
    char_count = 0
    
    word, char = word.lower(), char.lower()
    
    for i in word:
        if char == i:
            char_count += 1
            
    return f"{char} char found {char_count} times in {word}"

if __name__ == "__main__":
    print("=== Char Counter ===")
    answer = input("Case sensitive or not (y/n):")
    
    answer = answer.strip().lower()
    
    word = input("Word:")
    char = input("Char that you want to count:")
    
    word, char = word.strip(), char.strip()
    
    if answer == "y":
        print(case_sensitive_counter(word,char))
    elif answer == "n":
        print(not_case_sensitive_counter(word,char))
    else:
        print("Something went wrong")
        
        
"""Need exception handling and error detecting. Also I want to add sometihng that I don't know"""