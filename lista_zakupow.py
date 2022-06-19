print("Lista zakupów")
shopping_list_dict = {
    "Piekarnia": ["Chleb","Pączek","Bułki"],
    "Warzywniak": ["Marchew","Seler","Rukola"]
}
Leng = 0
for shop,items in shopping_list_dict.items():
    Leng = Leng + len(items)
    print(f"Idę do {shop.upper()} i kupuję")
    for product in items:
        print(f"{product.upper()} ")
    

print(f"W sumie kupuję {Leng} produktów.")

# Można zmodyfikować słownik na upper i powtórzyć pętle w wersji dla upper.
# Fajne zadanie na listy. Jest kilka możliwości. 
# druga zmiana pliku