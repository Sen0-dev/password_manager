import keyboard
import subprocess


class Password_manager:
        def __init__(self):
            self.name= ""
            self.pswd= ""
            self.file= open("exemple.txt", "a")
            self.what_supp= "" 

        #methode de classe pour ajouter un mdps
        def ajt_pswd(self):
            self.name= input("Nom du logiciel : ")
            self.pswd= input("Mot de passe associé : ")
            file= open("exemple.txt", "a")
            file.write(self.name + " : " + self.pswd+"\n")
            file.close()
        
        #voir les mdps (qui sont/seront contenu dans le fichier "exemple.txt")
        def voir_pswd(self):
            self.file= open("exemple.txt", "r")
            for uname_pswd in self.file:
                print(self.file.read())
            print("\nECHAP pour retourner au menu")
            while 1:
                if keyboard.is_pressed("echap"):
                    break
        
        #supprimer un mdps en entrant le nom du logiciel auquel il est associé
        def supp_pswd(self):
            self.what_supp= input("Nom du logiciel : ")
            if self.what_supp in self.list_uname_pswd:
                del self.list_uname_pswd[self.what_supp]
            else:
                print("INTROUVABLE")
                    

password_manag= Password_manager()

#fonction menu, fait appel à une des trois methode de classe
def menu(choix_fonction):
    while True:
        subprocess.call("cls", shell = True)
        choix= input("1= Ajouter un mot de passe\n2= Afficher vos mots de passe\n3= Supp un mot de passe\nq = QUIT\n\n>> ")
        match choix:
            case "1":
                choix_fonction.ajt_pswd()
            case "2":
                choix_fonction.voir_pswd()
            case "3":    
                choix_fonction.supp_pswd()
            case "q":
                break


#appel de la fonction
menu(password_manag)
