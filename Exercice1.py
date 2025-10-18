"""
TP2 - Exercice 1 : Gestion du Menu
"""

def analyser_menu(menu):
    """
    Analyse le menu du restaurant pour extraire des statistiques importantes.
    
    Args:
        menu (dict): Dictionnaire avec nom_plat: (prix, temps_preparation, popularité)
    
    Returns:
        dict: Dictionnaire contenant:
            - 'plat_plus_rentable': Le plat avec le meilleur ratio popularité/temps
            - 'prix_moyen': Le prix moyen de tous les plats
            - 'temps_moyen': Le temps de préparation moyen
    """
    stats = {}
    
    # TODO: Calculer le plat le plus rentable (ratio popularité/temps_preparation)
    # Attention: gérer le cas où temps_preparation pourrait être 0

    plat_rentable = None

    for plat, valeurs in menu.items():
        if valeurs[1] != 0:
            if plat_rentable is None or valeurs[2] / valeurs[1] > menu[plat_rentable][2] / menu[plat_rentable][1]:
                plat_rentable = plat

    stats["plat_plus_rentable"] = plat_rentable
            
    # TODO: Calculer le prix moyen du menu

    prix_moyen = 0
    if len(menu) != 0:
        for valeurs in menu.values():
            prix_moyen += valeurs[0]
        
        prix_moyen /= len(menu)

    stats["prix_moyen"] = prix_moyen

    # TODO: Calculer le temps de préparation moyen

    temps_moyen = 0
    if len(menu) != 0:
        for valeurs in menu.values():
            temps_moyen += valeurs[1]

        temps_moyen /= len(menu)

    stats["temps_moyen"] = temps_moyen

    return stats


def filtrer_menu_par_categorie(menu, categories):
    """
    Filtre le menu par catégories de plats.
    
    Args:
        menu (dict): Menu complet
        categories (dict): Dictionnaire nom_plat: catégorie
    
    Returns:
        dict: Menu organisé par catégories
    """
    menu_filtre = {}
    
    # TODO: Organiser les plats par catégorie
    # Exemple: {'entrées': [...], 'plats': [...], 'desserts': [...]}

    ordre_categories = ["entrées", "plats", "desserts"]

    for i in range(len(ordre_categories)):
        menu_filtre[ordre_categories[i]] = []
        for plat in menu:
            if categories.get(plat, "") == ordre_categories[i]:
                menu_filtre[ordre_categories[i]].append(plat)

    return menu_filtre


def calculer_profit(menu, ventes_jour):
    """
    Calcule le profit total de la journée.
    
    Args:
        menu (dict): Menu avec prix
        ventes_jour (dict): Nombre de ventes par plat
    
    Returns:
        float: Profit total
    """
    profit = 0
    
    # TODO: Calculer le profit total
    # profit = somme(prix_plat * nombre_ventes) pour chaque plat vendu

    for plat, valeurs in menu.items():
        profit += valeurs[0] * ventes_jour.get(plat, 0)
    
    return profit


if __name__ == '__main__':
    # Test de la fonction analyser_menu
    menu_test = {
        'Pizza Margherita': (12.50, 15, 8),
        'Pâtes Carbonara': (14.00, 12, 9),
        'Salade César': (9.50, 5, 6),
        'Tiramisu': (6.00, 3, 10),
        'Burger Classique': (11.00, 10, 7),
        'Soupe du jour': (5.50, 8, 5)
    }
    
    resultats = analyser_menu(menu_test)
    print("Analyse du menu:")
    print(f"  Plat le plus rentable: {resultats.get('plat_plus_rentable')}")
    print(f"  Prix moyen: {resultats.get('prix_moyen'):.2f}€")
    print(f"  Temps de préparation moyen: {resultats.get('temps_moyen'):.1f} min")
    
    # Test de la fonction filtrer_menu_par_categorie
    categories_test = {
        'Pizza Margherita': 'plats',
        'Pâtes Carbonara': 'plats',
        'Salade César': 'entrées',
        'Tiramisu': 'desserts',
        'Burger Classique': 'plats',
        'Soupe du jour': 'entrées'
    }
    
    menu_filtre = filtrer_menu_par_categorie(menu_test, categories_test)
    print("\nMenu par catégories:")
    for categorie, plats in menu_filtre.items():
        print(f"  {categorie}: {plats}")
    
    # Test de la fonction calculer_profit
    ventes_test = {
        'Pizza Margherita': 15,
        'Pâtes Carbonara': 20,
        'Salade César': 10,
        'Tiramisu': 25
    }
    
    profit_jour = calculer_profit(menu_test, ventes_test)
    print(f"\nProfit du jour: {profit_jour:.2f}€")
