def main():
    """Hovedfunktion for simpel lommeregner"""
    print("Simpel lommeregner - Addition")
    print("=" * 30)

    # Bed brugeren om at indtaste to tal
    tal1 = float(input("Indtast det første tal: "))
    tal2 = float(input("Indtast det andet tal: "))

    # Beregn summen
    resultat = tal1 + tal2

    # Vis resultatet
    print(f"\n{tal1} + {tal2} = {resultat}")


if __name__ == "__main__":
    main()