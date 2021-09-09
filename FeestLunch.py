Aantalcroissantjes = 17
CroissantjesPrijs = 0.39

Aantalstokbroden = 2
StokbrodenPrijs = 2.78

Aantalkortingsbonnen = 3
kortingsbonnen = 1.50

print(f'‘De feestlunch kost je bij de bakker {round(Aantalcroissantjes*CroissantjesPrijs + Aantalstokbroden*StokbrodenPrijs - Aantalkortingsbonnen*kortingsbonnen, 2)} euro voor de {Aantalcroissantjes} croissantjes en de {Aantalstokbroden} stokbroden als de {Aantalkortingsbonnen} kortingsbonnen nog geldig zijn!’')
