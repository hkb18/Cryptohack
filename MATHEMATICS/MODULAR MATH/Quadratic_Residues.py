p = 29
ints = [14, 6, 11]

def find_quadratic_residues(p, values):
    residues_with_roots = {}
    
    for a in range(1, p):
        a_squared_mod_p = (a * a) % p
        if a_squared_mod_p in values:
            if a_squared_mod_p not in residues_with_roots:
                residues_with_roots[a_squared_mod_p] = []
            residues_with_roots[a_squared_mod_p].append(a)
    
    return residues_with_roots

residues_with_roots = find_quadratic_residues(p, ints)

for residue, roots in residues_with_roots.items():
    print(f"Quadratic residue: {residue}, Roots: {roots}")

# This script identifies quadratic residues from a given list of integers modulo a prime p and computes their corresponding roots. It iterates through possible values a modulo p and checks whether a^2 mod p matches any value in the list, storing the roots for each residue. The challenge highlights understanding quadratic residues and efficiently finding their roots modulo a prime.