from string import ascii_lowercase

def viter():

    ids = []
    for num in range(1,101):

        if num % 10 == 0:
            for c in ascii_lowercase[0:6]:
                if num == 10:
                    ids.append(c)
                    continue

                ids.append(str(num-10)[0]+c)

        if num == 100:
            break
        ids.append(str(num))

    for c in ascii_lowercase[0:6]:
        for num in range(0,10):
            ids.append(c + str(num))
            if c + str(num) == "f8":
                break
        
        if c + str(num) == "f8":
            break

        for c2 in ascii_lowercase[0:6]:
            ids.append(c+c2)
    
    return ids