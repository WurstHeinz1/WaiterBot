import Levenshtein

def checkIntent(input, keywords, margin):
    for word in input.lower().split(" "):
        for keyword in keywords:
            if Levenshtein.distance(word, keyword.lower()) <= margin:
                return True
                break


def analyzeIntent(input, keywords, margin):
    recognizedWords = []

    for word in input.lower().split(" "):
        for keyword in keywords:
            if Levenshtein.distance(word, keyword.lower()) <= margin:
                recognizedWords.append(word)
    return recognizedWords