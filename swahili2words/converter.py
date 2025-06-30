# swahili2words/converter.py

units = [
    "sifuri", "moja", "mbili", "tatu", "nne", "tano",
    "sita", "saba", "nane", "tisa"
]

tens = [
    "", "kumi", "ishirini", "thelathini", "arobaini",
    "hamsini", "sitini", "sabini", "themanini", "tisini"
]

def convert_hundreds(n):
    result = []

    if n >= 100:
        hundreds = n // 100
        result.append("mia " + units[hundreds])
        n %= 100

    if n >= 20:
        ten = n // 10
        unit = n % 10
        result.append(tens[ten])
        if unit:
            result.append("na " + units[unit])
    elif n >= 10:
        if n == 10:
            result.append("kumi")
        else:
            result.append("kumi na " + units[n % 10])
    elif n > 0:
        result.append(units[n])
    elif not result:
        result.append(units[0])

    return " ".join(result)

def number_to_swahili(n, as_currency=False):
    if n < 0:
        return "hasi " + number_to_swahili(-n, as_currency)

    if isinstance(n, float):
        whole = int(n)
        decimal = int(round((n - whole) * 100))
        whole_part = number_to_swahili(whole)
        decimal_part = number_to_swahili(decimal)
        return (
            f"shilingi {whole_part} na senti {decimal_part}"
            if as_currency else
            f"{whole_part} nukta {decimal_part}"
        )

    if n == 0:
        return units[0]

    parts = []

    billions = n // 1_000_000_000
    if billions:
        parts.append("bilioni moja" if billions == 1 else number_to_swahili(billions) + " bilioni")
        n %= 1_000_000_000

    millions = n // 1_000_000
    if millions:
        parts.append("milioni moja" if millions == 1 else number_to_swahili(millions) + " milioni")
        n %= 1_000_000

    thousands = n // 1000
    if thousands:
        parts.append("elfu moja" if thousands == 1 else number_to_swahili(thousands) + " elfu")
        n %= 1000

    if n > 0:
        parts.append(convert_hundreds(n))

    return " ".join(parts)
