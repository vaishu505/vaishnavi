def get_person_details():
   """
   function to read a person's deails from the keyboard.
    """
   name=input("enter your name:")
   address=input("enter your address:")
   email=input("enter your email:")
   phone=input ("enter your phone number:")
   return name,address,email,phone

def print_person_details(name,address,email,phone):
    """
    function to print a persons detals.
    """
    print("\n--person details--")
    print(f"name:{name}")
    print(f"address:{address}")
    print(f"email:{email}")
    print(f"phopne number:{phone}")

#get details from the user
name,address,email,phone=get_person_details()
#print the details
print_person_details(name,address,email,phone)
