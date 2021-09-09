AantalPersonen = 4
Toegangsticket = 7.45

VRtijd = 45
Kostenper5minuten = 0.37

print(f'‘Dit geweldige dagje-uit met {AantalPersonen} mensen in de Speelhal met {VRtijd} minuten VR kost je maar {round(Toegangsticket + VRtijd*(Kostenper5minuten*AantalPersonen), 2)} euro’')