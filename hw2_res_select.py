# Name : Moosa Abbasi
#UID: U37033529
#Program description: Restaurant Selector


restaurants = {
    "Council Oak Steaks and Seafood": {"Vegetarian": "no", "Vegan": "no", "Gluten-Free": "no"},
    "Wood Fired Pizza Wine Bar": {"Vegetarian": "yes", "Vegan": "no", "Gluten-Free": "yes"},
    "Villaggio’s Ristorante Italiano": {"Vegetarian": "yes", "Vegan": "no", "Gluten-Free": "no"},
    "Farmacy Vegan Kitchen": {"Vegetarian": "yes", "Vegan": "yes", "Gluten-Free": "yes"}
}


vegetarian_input = input("Are any members of your party vegetarian? (yes/no): ").lower()
vegan_input = input("Are any members of your party vegan? (yes/no): ").lower()
gluten_free_input = input("Are any members of your party gluten-free? (yes/no): ").lower()


valid_restaurants = []

for restaurant, restrictions in restaurants.items():
    if (vegetarian_input == restrictions["Vegetarian"] or restrictions["Vegetarian"]=="yes") and (vegan_input == restrictions["Vegan"] or restrictions["Vegan"]=="yes")and (gluten_free_input == restrictions["Gluten-Free"] or restrictions["Gluten-Free"]=="yes"):
        valid_restaurants.append(restaurant)

if valid_restaurants:
    print("You can take your group to the following restaurants:")
    for restaurant in valid_restaurants:
        print(restaurant)
else:
    print("I'm sorry, there are no suitable restaurants for your group's dietary restrictions.")
