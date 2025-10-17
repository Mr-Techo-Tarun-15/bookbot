def word_counter(words):
    return len(words)

character_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ".", ",", "'", ";", ":", "!", "?", "-", "(", ")"]
character_dict = {}

def character_counter(path):
    with open(path) as f:
        frankenstein_contents = f.read()
    
    for char in character_list:
        character_dict[char] = frankenstein_contents.lower().count(char)
    return character_dict

def merger(dictionary):
    I_C_D_List = []
    for char in dictionary:
        individual_character_dict = {}
        individual_character_dict["char"] = char
        individual_character_dict["num"] = dictionary[char]
        I_C_D_List.append(individual_character_dict)
    return I_C_D_List
    
def sorter(dictionary):
    return dictionary["num"]
