def number_to_words(n: int) -> str:
    """Convert an integer 0-99 to its English word representation."""
    ones = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n < 20:
        return ones[n]
    ten_digit = n // 10
    one_digit = n % 10
    if one_digit == 0:
        return tens[ten_digit]
    return f"{tens[ten_digit]}-{ones[one_digit]}"


def amount_to_text(amount_str: str) -> str | None:
    """
    Convert a numerical amount string (e.g., "29.35") to its standard written form.
    Returns None if the amount is $100 or higher (not accepted by the store).
    """

    if "." in amount_str:
        dollar_part, cent_part = amount_str.split(".", 1)

        cent_part = cent_part.ljust(2, "0")[:2]
    else:
        dollar_part = amount_str
        cent_part = "00"

    dollars = int(dollar_part)
    cents = int(cent_part)


    if dollars >= 100:
        return None

    # Build dollar portion (handle singular/plural)
    dollar_word = number_to_words(dollars)
    dollar_suffix = "dollar" if dollars == 1 else "dollars"


    cent_word = number_to_words(cents)
    cent_suffix = "cent" if cents == 1 else "cents"

    return f"only {dollar_word} {dollar_suffix} and {cent_word} {cent_suffix}"


def validate_checks(file_path: str) -> None:
    """Read a check file and validate each line's numerical/text amount match."""
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    print("=" * 55)
    print("CHECK AMOUNT VALIDATION REPORT")
    print("=" * 55)

    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue 


        parts = line.split(maxsplit=1)
        if len(parts) < 2:
            print(f"Line {line_num}: ❌ Invalid format (missing description)")
            continue

        num_str, written_text = parts
        written_text = written_text.strip()


        try:
            float(num_str)
        except ValueError:
            print(f"Line {line_num}: ❌ Invalid number: {num_str}")
            continue


        expected = amount_to_text(num_str)

        if expected is None:
            print(f"Line {line_num}: ❌ ${num_str} exceeds $100 limit (NOT ACCEPTED)")
            continue


        if expected == written_text:
            print(f"Line {line_num}: ✅ ${num_str} → MATCH")
        else:
            print(f"Line {line_num}: ❌ ${num_str} → MISMATCH")
            print(f"    Expected: {expected}")
            print(f"    Found:    {written_text}")



if __name__ == "__main__":
    validate_checks("checks.txt")
