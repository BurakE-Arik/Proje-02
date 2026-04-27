# Fact Generator
def fact_generator():
    """Take facts from json file and print"""
    pass

               

def main():
    print("====FACT GENERATOR====")
    
    while True:
        start_command = input("Do you want a fact? (y/n): ").strip().lower()
        
        if start_command not in ["y","n"]:
            print("Please enter y or n")
            continue
        
        if start_command == "n":
            print("Goodbye!")
            break

        fact_generator()

if __name__ == "__main__":
    main()
        
# İhtiyaçlar;
    """Daha fazla fact içeren json dosyası
    Kolay editlenebilirlik
    Fonksiyonalra ayırma
    ve biraz daha düzgün  çalışma
    """