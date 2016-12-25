#!/usr/bin/python

import csv

questionsListe = ["Nervosité ou sensation de tremblements intérieurs  ",
                  "Nausées, douleurs ou malaises d’estomac  ",
                  "Impression d’être effrayé subitement et sans raison  ",
                  "Palpitations ou impression que votre cœur bat fort ou plus vite  ",
                  "Difficulté importante à vous endormir  ",
                  "Difficulté à vous détendre  ",
                  "Tendance à sursauter facilement  ",
                  "Tendance à être facilement irritable ou importuné  ",
                  "Incapacité à vous libérer de pensées obsédantes  ",
                  "Tendance à vous éveiller très tôt le matin et à rester éveillé  ",
                  "Vous sentir nerveux lorsque vous êtes seul  "
                 ]


totalQuestions = len(questionsListe)    #calcule le nombre de questions offertes

reponsesListe = []    #cree la liste des reponses et initialise chaque position a 0
for i in range(totalQuestions):
    reponsesListe.append(0)
#print(reponsesListe)



print ("Je vais vous poser ",totalQuestions, "questions.\n\n")

departQuestionnaire = input("Êtes-vous  prêts? 1 pour Oui \n")
if departQuestionnaire == "1":
    pass
else:
    print("Merci et à la prochaine")
    exit()

print ("Dans quelle mesure chacun de ces symptômes vous a dérangé ou inquiété\n")
print("1-Pas du tout, 2-Un peu, 3-Modérément, 4-Beaucoup, 5-Extrêmement\n")



numeroQuestion = 0     #initialise le compteur a la premiere question
compteurAnxiete = 0    #compteur des reponses elevees
while numeroQuestion <= totalQuestions - 1:    

    reponse = int(input (questionsListe[int(numeroQuestion)]))
    if reponse >= 4:
        compteurAnxiete + 1 
    print ("1:Pas du tout, 2:Un peu, 3:Modérément, 4:Beaucoup, 5:Extrêmement")

    if reponse >= 1 and reponse <= 5:
        print ("votre reponse est: ",reponse)
        reponsesListe[numeroQuestion] = reponse
        print ("c'etait la question ",numeroQuestion,"maintenant la suivante")
        numeroQuestion = numeroQuestion + 1
    else:
        print("erreur - la reponse doit etre entre 1 et 5")
        reponse = 0     #wrong answer

print ("Voici vos reponses:  ", reponsesListe)
print (compteurAnxiete)

if compteurAnxiete >= 5 and compteurAnxiete <= 7:
    print ("votre niveau d'anxieté est un peu élevé")
elif compteurAnxiete > 7:
    print ("votre niveau d'anxieté est élevé")


"""

import csv
b = open('ReponsesQuestionaireAnx.csv', 'w')
a = csv.writer(b)
a.writerows(reponsesListe)
b.close()


"""






"""

reponse2 = int(input (questions["Question2"]))
if reponse2 >= 3:
    compteurAnxiete + 1
print ("Merci")


reponse3 = int(input (questions["Question3"]))
if reponse3 >= 3:
    compteurAnxiete + 1
print ("Merci")

reponse4 = int(input (questions["Question4"]))
if reponse4 >= 3:
    compteurAnxiete + 1
print ("Merci")

reponse5 = int(input (questions["Question5"]))
if reponse5 >= 3:
    compteurAnxiete + 1
print ("Merci")

reponse6 = int(input (questions["Question6"]))
if reponse6 >= 3:
    compteurAnxiete + 1
print ("Merci")

reponse7 = int(input (questions["Question7"]))
if reponse7 >= 3:
    compteurAnxiete + 1
print ("Merci")

reponse8 = int(input (questions["Question8"]))
if reponse8 >= 3:
    compteurAnxiete + 1
print ("Merci")

reponse9 = int(input (questions["Question9"]))
if reponse9 >= 3:
    compteurAnxiete + 1
print ("Merci")

reponse10 = int(input (questions["Question10"]))
if reponse10 >= 3:
    compteurAnxiete + 1
print ("Merci")

reponse11 = int(input (questions["Question11"]))
if reponse11 >= 3:
    compteurAnxiete + 1
print ("Merci")


total = reponse1 + reponse2 + reponse3 + reponse4 + reponse5 + reponse6 + reponse7 + reponse8 + reponse9 + reponse10 + reponse11
print ("Votre total des points", total)

"""












"""

question1 = "Nervosité ou sensation de tremblements intérieurs.  "
question2 = "Nausées, douleurs ou malaises d’estomac.  "
question3 = "Impression d’être effrayé subitement et sans raison.  "
question4 = "Palpitations ou impression que votre cœur bat fort ou plus vite.  "
question5 = "Difficulté importante à vous endormir.  "
question6 = "Difficulté à vous détendre.  "
question7 = "Tendance à sursauter facilement.  "
question8 = "Tendance à être facilement irritable ou importuné.  "
question9 = "Incapacité à vous libérer de pensées obsédantes.  "
question10 = "Tendance à vous éveiller très tôt le matin et à rester éveillé.  "
question11 = "Vous sentir nerveux lorsque vous êtes seul.  "



nombreQuestions = 11
compteQuestions = 1

while compteQuestions <= nombreQuestions:
    temp = ("question" + str(compteQuestions))
    print (temp)
    print(question1)
    compteQuestions = compteQuestions + 1
    continue
print ("fin")





departQuestionnaire = input("Vous êtes prêts? 1 pour Oui ")
if departQuestionnaire == "1":
    pass
else:
    print("Merci et à la prochaine")
    exit()
print("\n")
print ("Dites moi dans quelle mesure chacun de ces symptômes vous a dérangé ou inquiété")
print("1-Pas du tout, 2-Un peu, 3-Modérément, 4-Beaucoup, 5-Extrêmement")
print("\n")

options = [1,2,3,4,5]

print(options)
reponse1 = input (question1)

if int(reponse1) in options:
    print("merci")
else:
    print("repondez 1-Pas du tout, 2-Un peu, 3-Modérément, 4-Beaucoup, 5-Extrêmement")
    quit()
print(reponse1)

print("\n")
reponse2 = input (question2)
print(reponse2)

"""





"""
print("\n")
reponse3 = input (question3)
print(reponse3)
print("\n")
reponse4 = input (question4)
print(reponse4)
print("\n")
reponse5 = input (question5)
print(reponse5)
print("\n")
reponse6 = input (question6)
print(reponse6)
print("\n")
reponse7 = input (question7)
print(reponse7)
print("\n")
reponse8 = input (question8)
print(reponse8)
print("\n")
reponse9 = input (question9)
print(reponse9)
print("\n")
reponse10 = input (question10)
print(reponse10)
print("\n")
reponse11 = input (question11)
print(reponse11)
"""
