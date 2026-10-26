import random
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python stk.py PHONE AMOUNT")

    try:
        phone = normalize_phone(sys.argv[1])
    except ValueError:
        sys.exit("Invalid Phone")

    try:
        amount = validate_amount(sys.argv[2])
    except ValueError:
        sys.exit("Invalid Amount")

    ref = ""
    for _ in range(6):
        number = random.randint(0, 9)
        ref += str(number)

    reference = f"TXN{ref}"
    print(f"Reference: {reference}")

    attempt = 0
    while attempt < 3:
        attempt += 1
        try:
            request = send_request(reference, phone, amount)
            if request == "success":
                print(f"Attempt {attempt}: success")
                print(f"Sent KSH {amount} to {phone}")
                break

            elif request == "insufficient funds":
                print(f"Attempt {attempt}: insufficient funds")
                print("Failed: customer has insufficient funds. No retry.")
                break

        except TimeoutError:
            print(f"Attempt {attempt}: timeout, retrying...")

    else:
        print(
            f"Failed: no response after 3 attempts. Reference {reference} - check status before retrying."
        )


# return the phone number in 254XXXXXXXXX format
def normalize_phone(raw):
    if len(raw) == 10:
        if raw[:2] == "07" or raw[:2] == "01":
            if raw.isdecimal() and raw.isascii():
                return f"254{raw[1:]}"
            else:
                raise ValueError
        else:
            raise ValueError

    elif len(raw) == 12:
        if raw[:4] == "2547" or raw[:4] == "2541":
            if raw.isdecimal() and raw.isascii():
                return raw
            else:
                raise ValueError
        else:
            raise ValueError

    else:
        raise ValueError


# return the required amount
def validate_amount(raw):
    if raw.isdecimal() and raw.isascii():
        if 1 <= int(raw) <= 150000:
            return int(raw)
        else:
            raise ValueError
    else:
        raise ValueError


# simulate the network
def send_request(reference, phone, amount):
    network = random.random()
    if network < 0.6:
        return "success"
    elif 0.6 <= network < 0.9:
        raise TimeoutError
    else:
        return "insufficient funds"


if __name__ == "__main__":
    main()
