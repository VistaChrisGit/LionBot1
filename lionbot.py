from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hi %1']], #order is input, response
    ['(hi|hello|hey|hola|howdy)', ['hey there', 'hey', 'howdy!']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    ['(.*)(location|city) ?', ['Tokyo, Japan']],
    ['(.*) created you?', ['VistaChris did using NLTK']],
    ['how is the weather in (.*)', ['the weather in %1 is alright']],
    ['(.*) your name ?', ['My name is LionBot']]
  
]

chat = Chat(pairs, reflections)
chat.converse()
