char = input("Enter an alphabet: ")

if len(char) == 1 and char.isalpha():
    if char=="A" or char=="E" or char=="I" or char=="O" or char=="U" or char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
        print(f'The {char} is vowel')
    else:
        print(f'The {char} is consonant')
else:
    print("Invalid input! Please enter only one alphabet.")