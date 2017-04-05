from compareImage import *
from smsTwilio import *

comparaison = compare("images/Image5.jpg","images/Image6.jpg")

if comparaison > 25:
    sendSms("+33644644866","+33699045380","Il s'est passé quelque chose chez vous !!!")
    print(comparaison)
else:
    print("Aucun message envoyé")