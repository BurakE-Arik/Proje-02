#harf counter

#alphabet_lower_case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","x","w",]
#alphabet_upper_case = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","X","W"]


def char_counter(word,char):
    
    char_count = word.count(char)
        
    return f"'{char}' char found /{char_count}/ times in {word}"


def main():
    print("=== Char Counter ===")
    while True:  
        answer = input("Case sensitive or not (y/n):").strip().lower()
        
        if answer not in ["y","n"]:
            print("Please enter y or n")
            continue
        
        word = input("Word:").strip()
        char = input("Char:").strip()
        
        if answer == "n":
            print(char_counter(word.lower(),char.lower()) + " (Not case sensitive)")
        else:
            print(char_counter(word,char))
            
        repeat = input("Any more words? (y/n) :").strip().lower() 
        if repeat != "y":
            print("Goodbye !")
            break   

if __name__ == "__main__":
    main()
        
"""Need exception handling and error detecting. Also I want to add sometihng that I don't know"""
""" Only works with 1 char not more need to fix"""