from microprediction import new_key, MicroWriter

write_key = new_key(difficulty=9)

mw = MicroWriter(write_key=write_key)

print(write_key)

print(mw.shash(write_key))

print(mw.animal_from_key(write_key))

import requests
res = requests.put('https://devapi.microprediction.org/email/4c7b09f29b8b7eb580b48ada674142cd', params={'email': 'YOUR EMAIL HERE'})
res.json()

from microprediction import MicroCrawler
crawler = MicroCrawler(write_key)
crawler.run()