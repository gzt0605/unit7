# unit7.py
# Ryan Ge
# October 18, 2016

def coprime(a, b, c):
    '''
    This function chooses a value for e
    :param a: the upper limit
    :param b: the first prime number
    :param c: the second prime number
    :return: chosen value for e
    '''

    # Fill up the number pool
    number = []
    for i in range(2, a + 1):
        number.append(i)

    # Keep the prime numbers

    # j is the index of each "announced" prime number
    j = 0
    while j <= a:

        # Remove multiples of j
        for i in number[j + 1:]:
            if i % number[j] == 0:
                number.remove(i)

    # Move on to the next prime number
        j += 1

    if b in number:
        number.remove(b)
    if c in number:
        number.remove(c)

    # Return to a random number in the prime number list
    import random
    return random.choice(number)

def encode(letter):
    '''
    This function encode a letter
    :param letter: the letter to encode
    :return: returns the encoded value
    '''
    # Set the alphabet for letter-number conversion
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    global e, n

    # Calculate the encoded value
    return alphabet.index(letter) ** e % n

def decode(value):
    '''
    This function decode the given value
    :param value: the value to decode
    :return: returns the decoded letter
    '''

    # Set the alphabet for letter-number conversion
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    global d, n

    # Find the decoded letter
    return alphabet[value ** d % n]

def key(p, q):
    '''
    This function produces the keys for encryption
    :param p: the first prime number
    :param q: the second prime number
    :return: returns nothing, all keys are set global
    '''

    global e, d, n

    # Calculate the modulus
    n = p * q

    # Calculate the totient
    t = (p - 1) * (q - 1)

    # Use the function coprime to find a value for e
    e = coprime(t, p, q)

    # Find value of d
    d = 1
    while (e * d - 1) % t != 0:
        d += 1

    # Print the keys
    print('Public key is:', e, n)
    print('Private key is:', d, n)

# Get input for value of p and q
p = int(input('Please enter a prime number:'))
q = int(input('Please enter another prime number:'))

# Generate keys
key(p, q)

# Let the user choose to encode, decode, or quit
while True:

    # Input command from user
    command = input('Enter e to encode, d to decode, or q to quit:')

    # Perform corresponding procedures
    if command == 'q':
        print('Thanks for playing. Have a nice day!')
        break
    elif command == 'e':
        letter = input('Please enter a letter to encode:')
        print('Encoded value:', encode(letter))
    elif command == 'd':
        message = int(input('Please enter a value to decode:'))
        pring('Decoded letter:' + decode(message))




