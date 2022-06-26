def cakes(recipe, available):
    result = []
    try:
        for i in recipe:
            if recipe[i] > 0:
                cakes_possible = available[i] / recipe[i]
                result.append(int(cakes_possible))
            else:
                pass
        result.sort()
    except KeyError:
        return 0
    return result[0]

recipe1 = {
    'flour': 500,
    'sugar': 200,
    'eggs': 1,
    'milk': 0
}
available1 = {
    'flour': 1200,
    'sugar': 1200,
    'eggs': 5,
    'milk': 200
}
# cakes(recipe,available)==2

recipe2 = {
    'apples': 3,
    'flour': 300,
    'sugar': 150,
    'milk': 100,
    'oil': 100

}
available2 = {
    'sugar': 500,
    'flour': 2000,
    'milk': 2000
}
# cakes(recipe,available)==0
print(f'Przepis: {recipe1} \nDostepnosc skladnikow: {available1} \nMozemy zrobic {cakes(recipe1, available1)} cakes')
print(f'Przepis: {recipe2} \nDostepnosc skladnikow: {available2} \nMozemy zrobic {cakes(recipe2, available2)} cakes')