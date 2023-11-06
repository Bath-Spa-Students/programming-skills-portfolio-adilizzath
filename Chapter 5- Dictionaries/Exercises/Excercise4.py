#create a dictionary of rivers and the countries they run through

rivers={
    'Amazon':'Brazil',
    'nile':'Egypt',
    'mississippi':'United States'
}

#print a sentence about each river
for river,country in rivers.items():
    print(f"the {river} runs through {country}.")

#print the names of each river
print("\nRivers:")
for river in rivers.keys():
    print(river)

#print the names of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
