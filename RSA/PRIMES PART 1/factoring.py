from factordb.factordb import FactorDB
f = FactorDB(510143758735509025530880200653196460532653147)
print(f.get_factor_list())
print(f.connect())
print(f.get_factor_list()) 

# This script retrieves the prime factors of a given number using the FactorDB API. It connects to the database, fetches the factorization of the input number, and prints the list of factors. The challenge focuses on leveraging external resources for factorization, which is essential for breaking RSA when N is factorable.