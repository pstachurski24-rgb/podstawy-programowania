translations = {'computer':'komputer','mouse':'myszka','keyboard':'klawiatura','printer':'drukarka'}
word = input('English word: ').strip().lower()
print(translations.get(word, 'Translation unavailable'))
