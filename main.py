while True:
    meme_dict = {
                "КРИНЖ": "Что-то очень странное или стыдное",
                "ЛОЛ": "Что-то очень смешное",
                "РОФЛ": "шутка",
                "ЩИЩ": "одобрение или востор",
                "КРИПОВЫЙ": "страшный, пугающий",
                "АГРИТЬСЯ": "злиться"
                }
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Такого слова нет!!!")
