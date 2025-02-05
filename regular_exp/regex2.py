# import re
# pattern = re.compile(r'^[a-z][0369][a-zA-Z0-9]*')
# str = [
#     "7376563478",
#     "b6",
#     "c9",
#     "d0",
#     "e4",  
#     "A3", 
#     "a33",
#     "b63",
#     "B93",
#     "d03"
# ]
# for string in str:
#     match = pattern.match(string)
#     if match:
#         print(f"{string} : Matched")
#     else:
#         print(f"{string} : Not matched")




# import re
# pattern = re.compile(r'^[a-z]+\.[0-9]+@[a-z]+\.[a-z]{2,}$')
# emails = ["shivamsingh.181002@gmail.com",
#     "Abc21@gmail.com", 
#     "abc.22@yahoo.com", 
#     "abc#22@gmailcom",  
#     "abc@22@gmail.com",  
#     "abc.22@domain.co",  
#     "abc.22@domain.info",  
#     "abc.22@domain.co.uk",  
#     "abc.22@domain",  
#     "abc.22@domain.c"  
# ]
# for email in emails:
#     match = pattern.match(email)
#     if match:
#         print(f"{email} : Matched")
#     else:
#         print(f"{email} : Not matched")





# import re, urllib
# import urllib.request
# u=urllib.request.urlopen("https://www.redbus.in/info/contactus")
# data=u.read().decode('utf-8')
# pattern = re.compile(r'\+?\d{1,3}?\d{10}')
# phone_numbers = pattern.findall(data)
# for phone_number in phone_numbers:
#     print(phone_number)




import re
pattern = re.compile(r'^https://fidelity//rest//v[1-9](\.\d+)+$')
# test_strings = [
#     "https://fidelity//rest//v1.0.0",
#     "http://fidelity-123//rest/1",
#     "https://fidelity//rest//v1.2.3"
# ]

with open('regex.txt', 'r') as file:
    test_strings = file.read().splitlines()
for string in test_strings:
    match = pattern.match(string)
    if match:
        print(f"{string} : Matched")
    else:
        print(f"{string} : Not matched")

