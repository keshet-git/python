capitals = {'USA':'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russisa':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China')
capitals.clear()
#print(capitals[Germeny])
#print(capitals.get('Germeny'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())


for key,value in capitals.items():
    print(key, value)