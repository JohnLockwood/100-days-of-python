# -*- coding: utf-8 -*-

def block1():
    string = "Hello"
    same_string = "Hello"
    number = 3
    same_number = 3
    boolean = True
    same_boolean = True
    
    print(string == same_string)
    print(number == same_number)
    print(boolean == same_boolean)



def block2():
    dictionary = {"favorite_website": "https://codesolid.com", "attempts": 1}
    same_dictionary = dictionary.copy()
    
    # Comparing simply a matter of using ==, same with other Python types
    print(dictionary == same_dictionary)
    
    # Change type of attempts -- keep value similar:
    #s3 = standard.copy()
    # s3["attempts"] = 1.0
    
    #print(s3 == standard)
    
    #print(type(s3["attempts"]))
    
    #print(1.0 == 1)

def block3():
    pass
