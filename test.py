from lib import compareImage
from lib import smsTwilio

comparaison = compareImage.compare("images/Image5.jpg","images/Image6.jpg")

if comparaison > 25:
    smsTwilio.sendSms("+33644644866","+33699045380","Il s'est passé quelque chose chez vous !!!")
    print(comparaison)
else:
    print("Aucun message envoyé")