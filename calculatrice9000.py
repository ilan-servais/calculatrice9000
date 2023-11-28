historique = []

def ajouter_historique(expression, resultat):
    if not expression.startswith("afficher_historique") and not expression.startswith("effacer_historique"):
        historique.append((expression, resultat))

def afficher_historique():
    if not historique:
        print("Historique vide.")
    else:
        print("Historique :")
        for i, (expression, resultat) in enumerate(historique, 1):
            print(f"{i}. {expression} = {resultat}")

def effacer_historique():
    historique.clear()
    print("Historique effacé.")

def calculatrice():
    while True:
        expression = input("Entrez une expression mathématique (ou 'q' pour quitter): ")
        
        if expression == 'q':
            break
        elif expression == 'afficher_historique()':
            afficher_historique()
        elif expression == 'effacer_historique()':
            effacer_historique()
        else:
            try:
                resultat = eval(expression)
                print(f"Résultat : {resultat}")
                ajouter_historique(expression, resultat)
            except Exception as e:
                print(f"Erreur : {e}")

calculatrice()
