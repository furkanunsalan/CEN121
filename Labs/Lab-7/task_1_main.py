from task_1_pet import Pet
    

def main():
    pet_name = input("Enter pet name: ")
    pet_type = input("Enter pet type: ")
    pet_age = int(input("Enter pet age: "))
    
    my_pet = Pet(pet_name, pet_age, pet_type)
    
    print("Here is the data that you entered:")
    print("Pet name: ", my_pet.get_name())
    print("Pet type: ", my_pet.get_animal_type())
    print("Pet age: ", my_pet.get_age())

main()
