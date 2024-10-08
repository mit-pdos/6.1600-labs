import bad_server
import attacker
import secrets

def extract_bytes(n_bytes):
    secret = secrets.token_hex(n_bytes)
    server = bad_server.BadServer(secret)
    attack = attacker.Client(server)
    res = attack.steal_password(n_bytes)
    assert res == secret, f"Result {res} not equal to secret {secret}"

def main():
    bytes_to_test = [
        4,        
        8,
        16,
        32,
    ]

    for byte_to_test in bytes_to_test:
        try:
            extract_bytes(byte_to_test)
            print("Extracting %s bytes: Pass" % byte_to_test)
        except:
            print("Extracting %s bytes: Fail" % byte_to_test)


if __name__ == "__main__":
    main()