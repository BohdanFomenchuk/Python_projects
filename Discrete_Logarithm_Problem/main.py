# Discrete_Logarithm_Problem encryption is a public-key crypto-system. It uses asymmetric key encryption for a safe communication between
# two people.
# Let us assume that Alice wants to communicate with Bob. Alice generates three large random integers:
# - Q a prime used as the order of the key
# - 0 < G < Q a generator
# - X Alice's secret key
# Alice computes H = G^X mod Q and publicly shares with Bob the public key (G, H, Q). As an attacker, you intercept
# this key and decide to spy on their communications. To do so, you need to find Alice's secret key X. This can be
# done by performing a discrete logarithm attack on this key.
# Given the public key (G, H, Q), you are asked to perform this attack: find the lowest integer X such that G^X mod Q
# = H.
# The rest of this protocol is not explained to avoid overload, but it can be found on
# https://en.wikipedia.org/wiki/ElGamal_encryption

import time

G = 49999999961
H = 42
Q = 49999999967
start = time.time()

def crack(G, H, Q):
    # Baby-Step Giant-Step algorithm
    m = int(Q ** 0.5) + 1
    baby_steps = {}
    # Precompute the baby steps
    for j in range(m):
        baby_steps[pow(G, j, Q)] = j
    # Giant step: G^(-m)
    gm = pow(G, -m, Q)
    print(gm)
    # Search for a match
    for i in range(m):
        target = (H * pow(gm, i, Q)) % Q

        if target in baby_steps:
            return i * m + baby_steps[target]

    # If no match is found
    return None


# Public key values

# Perform the attack
X = crack(G, H, Q)
end = time.time()
if X is not None:
    print(f"Found X: {X}, Execution time = {end-start}")
else:
    print("No X found")