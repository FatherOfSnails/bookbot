def get_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.split()    
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def get_character_count(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    characters = {}
    character_count = 1
    for character in file_contents:
        character = character.lower()
        if character not in characters:
            characters[character] = 1
        elif character in characters:
            characters[character] += 1
    return characters

def sort_stats(stats):
    stat_list = []
    for k in stats:
        v = stats[k]
        stat_list.append({'char': k, 'num': v})
    stat_list.sort(reverse=True, key= lambda stat_list: stat_list['num'])
    return stat_list
