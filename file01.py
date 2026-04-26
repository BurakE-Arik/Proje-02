# Fact Generator

def nope_action():
    global nope_counter
    nope_counter = 0
    real_answer = input("Do you REALLY want to quit ?? :")
    
    if real_answer.lower() == "yes":
        print("Okay okay see you next time !")
        return True
    else:
        print("YAY !")
        return False

            


if __name__ == "__main__":
    nope_counter = 0
    print("========================")
    print("    FACT GENERATOR")
    print("=======say 'no' to close==========")
    while True:
        answer = input("Do you want a FACT :")
        if answer.lower() == "yes":
            print("""
                  987654321 
                  ---------  = 8,0000000729000006633900060368491
                  123456789\n""")
        elif answer.lower() == "no":
            print("WHY ???")
            continue
        elif answer.lower() == "nope":
            print("AAAh Goodbye :)")
            break
        else:
            print("NOPE!")
            nope_counter += 1
            
            if nope_counter > 5:
                if nope_action():
                    break
                else:
                    continue
            continue
        
        
# İhtiyaçlar;
    """Daha fazla fact içeren json dosyası
    Kolay editlenebilirlik
    Fonksiyonalra ayırma
    ve biraz daha düzgün  çalışma
    """