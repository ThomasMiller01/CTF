from string import ascii_lowercase

code = 'jyvzzpunaolybipjvunfzpthre'

normal_alph = ascii_lowercase

for j in range(26):
    rotated_alph = [normal_alph[(i + j + 1) % len(normal_alph)]
                    for i in range(0, len(normal_alph))]

    flag = ''
    for c in code:
        flag += normal_alph[rotated_alph.index(c)]

    print("picoCTF{%s}" % flag)
