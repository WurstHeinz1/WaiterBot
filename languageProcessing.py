import Levenshtein

def checkIntent(input, keywords, margin):
    try:
        for word in input.lower().split(" "):
            for keyword in keywords:
                if Levenshtein.distance(word, keyword.lower()) <= margin:
                    return True
                    break
        return False
    except:
        return False


def analyzeIntent(input, keywords, margin):
    recognizedWords = []
    try:
        for word in input.lower().split(" "):
            for keyword in keywords:
                if Levenshtein.distance(word, keyword.lower()) <= margin:
                    recognizedWords.append(word)
        return recognizedWords
    except:
        return []