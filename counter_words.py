def removeSpecialChars(word):
  for char in word:
    if char.isdigit():
      word = word.replace(char,'')

    if not char.isalnum():
      word = word.replace(char,'')

  return word

def removeSpecialCharsFromText(words:list)->list:
  count = 0

  for word in words:
    words.remove(word)
    word = removeSpecialChars(word)
    words.insert(count,word)

    count += 1
    
  return words

def deleteEmptyWords(words:list)->list:
  for word in words:
    if(word == ""):
      words.remove(word)

  return words

def countWordsFrequency(words:list)->list:
  frequency = dict();

  for word in words:
    frequency[word] = frequency.get(word, 0) + 1
    
  return frequency

def countTotalWords(words:dict)->int:
  number_of_words = 0

  for repetitions in words.values():
    number_of_words += repetitions

  return number_of_words

def countUniqueWords(words:dict)->int:
  number_of_words = 0

  for repetitions in words.values():
    if repetitions == 1:
      number_of_words += 1

  return number_of_words

def getMostRepeatedWords(words:dict,top_number:int)->list:

  ordered_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
  top_repeated = ordered_words[:top_number]

  return [(word, repetitions) for word, repetitions in top_repeated]

def percentage(repetitions:int,total:int)->float:  
  return round((repetitions/total)*100,2)

text = '''
Nur für mich bist du am Leben
Ich steck dir Orden ins Gesicht
Du bist mir ganz und gar ergeben
Du liebst mich, denn ich lieb dich nicht

Du blutest für mein Seelenheil
Ein kleiner Schnitt und du wirst geil
Der Körper schon total entstellt
Egal, erlaubt ist, was gefällt
'''

text = text.lower().split()

text = removeSpecialCharsFromText(text)
text = deleteEmptyWords(text)

words_freq = countWordsFrequency(text)

words_number = countTotalWords(words_freq)
words_unique = countUniqueWords(words_freq)
top_words = getMostRepeatedWords(words_freq,5)
all_words_with_repetitions = getMostRepeatedWords(words_freq,len(words_freq))

print(f"\nO número total de palavras é:\t\t{words_number}")
print(f"O número total de palavras únicas é:\t{words_unique}\n")
print(f"As 5 palavras que mais se repetiram no texto foram (em percentual de ocorrência):")

for words in top_words:
  print(f"-{words[0]}:\t\t{percentage(words[1],words_number)} %")

see_list = input("\nDeseja ver a lista com as repetições (em percentual de ocorrência) de TODAS as palavras do texto? (s)im)/(n)ão?\n")
if(see_list == 's'):
  print(f"\nLista com todas as palavras e suas repetições (em percentual de ocorrência):")
  for words in all_words_with_repetitions:
    print(f"{words[0]}:\t\t{percentage(words[1],words_number)} %")