# Authors: Caden Rothzeid


# uses sieve of eratosthenes because it's the fastest but requires more memory than other options
# for modern computers and the side of the primes it's not an issue
# calculate primes
def sieve_of_eratosthenes(num):
    prime = [True for _ in range(num + 1)]
    # boolean array
    p = 2
    while p * p <= num:

        # If prime[p] is not
        # changed, then it is a prime
        if prime[p]:

            # Updating all multiples of p
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    final = []
    # Print all prime numbers
    for p in range(2, num + 1):
        if prime[p]:
            final.append(p)
    return final


def main():
    # Banner
    print("AutoRSA v2.0.0")
    print("Created for NCL")

    # Get user input for the given values provided by NCL
    try:
        n = int(input('Enter n: '))

    except ValueError:
        print("Invalid input for n. Please enter an integer.")

    # get n value
    input_valid = False
    # start n outside the while loop's scope
    n = None
    while not input_valid:
        try:
            n = int(input('Enter n: '))
            input_valid = True
        except ValueError:
            print("Invalid input for n. Please enter an integer.")

    input_valid = False
    # start e outside the while loop's scope
    e = None
    while not input_valid:
        try:
            e = int(input('Enter e: '))
            input_valid = True
        except ValueError:
            print("Invalid input for e. Please enter an integer.")

    input_valid = False
    # start c outside the while loop's scope
    while not input_valid:
        try:
            c = input('Enter c: ').split()
            c = [int(m) for m in c]
            input_valid = True
        except ValueError:
            print("Invalid input for c. Please enter a space-separated list of integers.")

    # calculate all primes up to n
    primes = sieve_of_eratosthenes(n)

    # setup finding p (lower prime) and q (higher prime)
    run = False
    p = 0
    q = 0
    # Find p & q
    for primeP in primes:
        # exit if found
        if run:
            break
        for primeQ in primes:
            # check if p & q found
            if primeP * primeQ == n:
                run = True

                # smaller prime
                p = primeP
                # larger prime
                q = primeQ
                # early exit
                break

    # intermediate value
    t = (p - 1) * (q - 1)
    # private key
    d = pow(e, -1, t)

    # display p & q
    print(f'(smaller prime) p = {p}\n(larger prime) q = {q}')
    # decode each message in cipher text
    plaintext = ""
    for m in c:
        # add each decrypted character to plaintext
        plaintext += chr(int(m) ** d % n)
    # display plaintext
    print(f"plaintext = {plaintext}")


if __name__ == '__main__':
    main()
