import attack
import client
import constants
import random

def get_countries():
    countries = []
    with open("capitals.txt", "r") as f:
        for line in f:
            countries.append(line.strip())
    return countries

def grade_decrypt():
    raise ValueError("Please test your decryption attack on gradescope")
    
    # The autograder will run the code below to grade your solution

    # countries = get_countries()
    # secret = "{\n"
    # for i in range(3):
    #     secret += '"city%d": "%s",\n' % (i, random.choice(countries))
    # secret += "}\n"

    # print(secret)
    # c = client.Client()

    # def run_client(prefix):
    #     # This is the function that compresses with our compression algorithm
    #     # and sends the message. Returns: (bytes_sent, bytes_received)
    #     return COMPRESS_AND_SEND(prefix + secret)

    # guess = attack.attack_decrypt(run_client)

    # if secret != guess:
    #     raise ValueError("Bad guess")

def grade_tamper(compress=False):
    a = attack.AttackTamper(compress)
    c = client.Client(a.handle_data)
    c.run_client("ls ./files/*", compress)

    if c.message_received != constants.BINGO:
        raise ValueError("Not successful")

def main():
    parts = [
        ('a', grade_decrypt),
        ('b', grade_tamper),
        ('c -- EXTRA CREDIT', lambda: grade_tamper(True)),
    ]

    for p in parts:
        try:
            p[1]()
            print("Part (%s): Pass" % p[0])
        except ValueError:
            print("Part (%s): Fail" % p[0])


if __name__ == "__main__":
    main()
