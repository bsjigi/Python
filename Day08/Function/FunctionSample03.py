def programInfo(**information):
    for name in information.keys():
        value = information[name]
        print('{} : {}'.format(name,value))

programInfo(Version='1.x', Author='kim')