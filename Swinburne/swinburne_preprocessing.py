swinfile = open("swinburne_poems.txt", mode='r')

sonnets = []
building = ''
for line in swinfile:
    if line[0] == '_':
        sonnets.append(building)
        building = ''
    else:
        if len(line) > 2:
            building += line


i = 0
for sonnet in sonnets:
    file = open("Swin_works/p"+str(i)+".txt", mode='w+')
    file.write(sonnet)
    file.close()
    i += 1
