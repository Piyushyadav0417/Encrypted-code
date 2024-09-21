
try:
    choice = int(input("1 for Code:\n2 for Decode:\n3 for exit:\nEnter Your choice: "))


    if choice == 1:
            word = input("Enter Your msg: ")
            if len(word) >= 3:
                randome = "abc"
                lword = " ".join(word).split()
                lastchar = lword[0]
                lword.remove(lastchar)
                lword.append(lastchar)
                lword.insert(0, randome)
                lword.append(randome)
                final_code = "".join(lword)
                print(final_code)

            else:
                print(word[::-1])
                
    elif choice == 2:
            word = input("Enter code here: ")
            if len(word) >= 3:
                lword = " ".join(word).split()
                del lword[:3]
                del lword[-3:]
                lastchar = lword[-1]
                lword.remove(lastchar)
                lword.insert(0, lastchar)
                
                realmsg = "".join(lword)
                print(realmsg)
            else:
                print(word[::-1])
except ValueError:
    print("Please Enter a vailid choice: ")