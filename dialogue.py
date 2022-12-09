import random
import speechProcessing
import languageProcessing

menu = ["Pizza", "Burger", "Salat", "Müsli"]
menuWords = ["karte", "speisekarte", "geben", "gibt"]
answerUnknownIntent = ["Tut mir leid, das habe ich leider nicht verstanden.", "Ich weiß nicht genau, was sie meinen."]
offerHelp = ["Wie kann ich ihnen helfen?", "Was kann ich für sie tun.?", "Womit kann ich ihnen helfen?"]
positiveAnswers = ["ja", "genau", "natürlich", "exakt"]
negativeAnswers = ["nein"]


def start():
    speechProcessing.say(offerHelp[random.randint(0, len(offerHelp)-1)])
    intent = speechProcessing.recognizeLanguage()

    if languageProcessing.checkIntent(intent, menuWords, 1):
        showMenu()
    elif languageProcessing.checkIntent(intent, ["bestellen", "bestellung"], 1):
        order()
    else:
        unknownIntent()


def showMenu():
    menuText = "Für sie haben wir heute "
    for meal in range(len(menu)):
        if meal > len(menu)-2:
            menuText += "und "
            menuText += menu[meal]
        else:
            menuText += (menu[meal] + ", ")
    menuText += " im Angebot."
    speechProcessing.say(menuText)

    speechProcessing.say("Möchten sie etwas bestellen?")
    intent = speechProcessing.recognizeLanguage()
    if languageProcessing.checkIntent(intent, positiveAnswers, 1):
        order()
    elif languageProcessing.checkIntent(intent, negativeAnswers, 1):
        start()
    else:
        unknownIntent()


def order():
    speechProcessing.say("Was möchten sie gerne bestellen?")
    intent = speechProcessing.recognizeLanguage()

    wishes = languageProcessing.analyzeIntent(intent, menu + menuWords, 1)

    for element in wishes:
        for menuWord in menuWords:
            if element == menuWord:
                showMenu()
                break

    if wishes != []:
        orderConfirmationText = "Sie möchten also "
        for wish in range(len(wishes)):
            if wish > len(wishes)-2:
                orderConfirmationText += "und "
                orderConfirmationText += wishes[wish]
            else:
                orderConfirmationText += (wishes[wish] + ", ")
        orderConfirmationText += " bestellen?"
        print(orderConfirmationText)
        speechProcessing.say(orderConfirmationText)

        confirmation = speechProcessing.recognizeLanguage()
        if languageProcessing.checkIntent(confirmation, positiveAnswers, 1):
            speechProcessing.say("Danke für ihre Bestellung!")

        elif languageProcessing.checkIntent(confirmation, negativeAnswers, 1):
            speechProcessing.say("In Ordnung.")
            order()
        else:
            unknownIntent()

    else:
        unknownIntent()



def unknownIntent():
    speechProcessing.say(answerUnknownIntent[random.randint(0, len(answerUnknownIntent)-1)])
    start()

### Main ###

speechProcessing.say("Herzlich willkommen in diesem Restaurant!")

start()





