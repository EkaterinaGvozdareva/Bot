import random
import re
import nltk


def filter_text(text):
    text = text.strip()
    expression = r'[^\w\s]'  # Всё что, не слово и не пробел
    text = re.sub(expression, "", text)  # Удалить всё, что не слово и не пробел
    return text


def text_match(user_text, example):
    user_text = user_text.lower()
    example = example.lower()
    user_text = filter_text(user_text)
    if user_text.find(example) != -1:
        return True
    text_len = len(user_text)
    difference = nltk.edit_distance(user_text, example) / text_len
    return difference < 0.4


actions = {
    "hello": {
        "examples": ["привет", "здравствуйте"],
        "bot": ["Привет", "Здравствуйте"],
    },
    "how_are_you": {
        "examples": ["как дела", "че как", "чем занят"],
        "bot": ["Как всегда", "Всё как обычно", "Исполняю обязанности робота"],
    },
    "name": {
        "examples": ["как тебя зовут", "как твоё имя", "как тебя звать"],
        "bot": ["я бот"]
    },
    "joke": {
        "examples": ["расскажи шутку", "расскажи анекдот", "повесели меня", "пошути"],
        "bot": ["Почему шутить можно над всеми, кроме безногих?\nШутки про них обычно не заходят.",
                "Почему в Африке так много болезней?\nПотому что таблетки нужно запивать водой."]
    },
    "300": {
        "examples": ["скажи 300", "сколько 100+200", "сколько 150+150", "сколько 600 разделить на 2"],
        "bot": ["Трактарист сегодня я", "Асталависта", "300"]
    },
    "weight": {
        "examples": ["какой вес", "какой у тебя вес"],
        "bot": ["Такое неприлично спрашивать", "У меня нет весов", "Около 60, наверное"]
    },
    "height": {
        "examples": ["какой рост", "какой у тебя рост"],
        "bot": ["175", "Модельный", ""]
    },
    "no": {
        "examples": ["нет", "не-а"],
        "bot": ["А мне кажется, что да", "Да", "А я думаю да", "Ладно, моя ошибка"]
    }
}
while True:
    text = input()
    for action in actions:
        examples = actions[action]["examples"]
        responses = actions[action]["bot"]
        for example in examples:
            if text_match(text, example):
                print(random.choice(responses))
