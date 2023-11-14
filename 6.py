# 1. Skapa din första def-funktion som kan plussa två tal och returnerar summan med return-kommandot
# def math(x):
#    return x + 10
# print(math(2))
# 2. Gör en def-funktion som skriver ut ditt namn
# def my_name():
#     print("My name is Artem")
# my_name()
# 3. Gör en loop som skriver ut resultatet av en def 10 gånger
# def math(x):
#     return 2*10
# for x in range (1,11):
#     print(math(2))

# 4. Skapa ett program som kan ändra/lägga till/ta bort namn i en lista med olika funktioner

# Funktion som visar meny

# def display_menu():
#     print("\nMenu:")
#     print("1. Display Names")
#     print("2. Add Name")
#     print("3. Edit Name")
#     print("4. Remove Name")
#     print("5. Quit")

# # Funktion som visar alla namn som finns i listan
# def display_names(names):
#     print("\nCurrent Names:")
#     for index, name in enumerate(names):
#         print(f"{index + 1}.) {name}")

# # Funktion som lägger till ett namn i listan
# def add_name(names):
#     new_name = input("\nEnter the name to add: ")
#     names.append(new_name)
#     print(f"{new_name} has been added to the list.")

# # Funktion som kan ändra ett visst namn i listan
# def edit_name(names):
#     display_names(names)
#     while True:
#         try:
#             index = int(input("\nEnter the index of the name you want to edit: "))
#             index = index - 1
#             if 0 <= index < len(names):
#                 new_name = input("Enter the new name: ")
#                 names[index] = new_name
#                 print(f"Name at index {index} has been updated.")
#                 break
#             else:
#                 print("Invalid index. Please try again.")
#         except ValueError:
#             print("Invalid index. Please try again")

# # Funktion som kan ta bort ett namn från listan
# def remove_name(names):
#     display_names(names)
#     while True:
#         try:
#             index = int(input("\nEnter the index of the name you want to remove: "))
#             index = index-1
#             if 0 <= index < len(names):
#                 removed_name = names.pop(index)
#                 print(f"{removed_name} has been removed from the list.")
#                 break
#             elif index is not names:
#                 print("Invalid index. Please try again.")
#         except ValueError:
#                 print("Invalid index. Please try again.")

# # Main program loop
# names = ["Artem"]

# while True:
#     display_menu()
#     choice = input("\nEnter your choice (1-5): ")

#     if choice == "1":
#         display_names(names)
#     elif choice == "2":
#         add_name(names)
#     elif choice == "3":
#         edit_name(names)
#     elif choice == "4":
#         remove_name(names)
#     elif choice == "5":
#         print("\nGoodbye!")
#         break
#     else:
#         print("\nInvalid choice. Please try again.")

# 5. Bygg vidare på din miniräknare (med fyra räknesätt) så den använder en def som gör alla sorts beräkningar och ger tillbaka svar

def calculator():
    firstValue = float(input("Type in first number: "))
    secondValue = float(input("Type in second number: "))
    operation = input("Type in operation +, -, /, * ")
    if operation == '+':
        print(f"The answer is {firstValue + secondValue}")

calculator()