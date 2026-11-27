countries = [{"name":"Poland","population":38000000},{"name":"Germany","population":83200000},{"name":"France","population":68000000},{"name":"Italy","population":59000000},{"name":"Spain","population":48000000}]
print(f"{'COUNTRY':<15} POPULATION")
for country in countries:
    print(f"{country['name']:<15} {country['population']}")
