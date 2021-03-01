user = input("Anna merkkijono: ")
user_length = len(user)
for string_index in range(user_length - 1, -1, -1):
    character = user[string_index]
    print(character)