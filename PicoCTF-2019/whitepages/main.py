import codecs

characters_dict = {}
lines = []
character_list = []

with open("./whitepages/whitepages.txt", "r") as f:
    for line in f:
        lines.append(line)
        for ch in line:
            character_list.append(ch)
            if ch not in characters_dict:
                characters_dict[ch] = []
            characters_dict[ch].append((ch, line.index(ch)))

with codecs.open("./whitepages/utf_8_file.txt", "w", "utf-8") as f:
    f.write("".join(lines))

print(character_list)
