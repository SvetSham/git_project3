def str_upper(string):
    """Делает все буквы в строке заглавными"""
    return string.upper()


def all_capitalized_words(string):
    """Делает первые буквы всех слов заглавными"""
    words = string.split()
    res = []
    for word in words:
        res.append(word.capitalize())
    result = ' '.join(res)
    return result

