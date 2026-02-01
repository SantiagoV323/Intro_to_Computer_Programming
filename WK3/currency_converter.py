def main():
    # Welcome user and ask user for an amount in USD, taking the amount from input parsing as a float, saving it in the usd variable
    usd = float(input("Hello user, please type the amount of USD you want to convert: "))

    # Converting the USD to different currencies multiplying the amount desired by the currency exchange rate
    euro = usd * 0.84353747
    cad = usd * 1.36208058
    aud = usd * 1.43663427

    # Print the converted amounts with 2 decimal places
    print(f"Good! Your amount of ${usd:.2f} USD is equivalent to €{euro:.2f} Euro, ${cad:.2f} CAD, and ${aud:.2f} AUD.")

main()