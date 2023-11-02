# Pair of gloves
# Winter is coming, you must prepare for your ski holidays. The objective of this kata is to determine 
# the number of pair of gloves you can combine from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can combine, 
# assuming that only gloves of the same color can form pairs. 

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# output = 2 
# explanation = 1 red pair + 1 blue pair

# input = ["red", "red", "red", "red", "red", "red"]
# output = 3 
# explanation = 3 red pairs

def glove_get(glove_list):
    pair_count = 0
    glove_dict = {}
    # for glove in range(len(glove_list)):
    #     if glove_list[glove] not in glove_dict:
    #         glove_dict[glove_list[glove]] = 1
    #     print(glove_dict)
    #     for extra_glove in range(glove + 1, len(glove_list)):
    #         if glove_list[glove] == glove_list[extra_glove]:
    #             glove_dict[glove_list[glove]] += 1
    #         break
    for glove in glove_list:
        if glove not in glove_dict:
            glove_dict[glove] = 1
        elif glove in glove_dict:
            glove_dict[glove] += 1
    for glove_pair in glove_dict:
        if glove_dict[glove_pair] >= 2:
            pair_count += glove_dict[glove_pair] // 2
    return pair_count
print(f"You have {glove_get(input)} pairs of gloves")