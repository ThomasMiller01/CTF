from string import ascii_lowercase

normal_alph = ascii_lowercase
rotated_alph = [normal_alph[(i + 13) % len(normal_alph)]
                for i in range(0, len(normal_alph))]

code = 'cvpbPGS{guvf_vf_pelcgb!}'

flag = ''
for c in code:
    character = normal_alph[rotated_alph.index(
        c.lower())] if c.lower() in rotated_alph else c
    flag += character if c.islower() else character.upper()

print(flag)
