from getpass import getpass
import hashlib

password = getpass()
print(password)

"""
liste des alogo compatibles toutes plateformes:
>>> hashlib.algorithms_guaranteed
{'sha384', 'shake_256', 'sha3_384', 'blake2s', 'sha3_256', 'blake2b', 'sha224', 'sha3_224', 'sha3_512', 'shake_128', 'sha512', 'sha256', 'sha1', 'md5'}
"""

# demo avec algo sha1 (prend chaine de bytes d'octets)
mdp = hashlib.sha1(b'mot de passe')
print(mdp)
# <sha1 HASH object @ 0x7f030c2ee890>

# chiffrement par digest (b) ou hexdigest (hexa)
mdp = mdp.hexdigest()
# 'b47ea832576a75814e13351dcc97eaa985b9c6b7'

# pas de déchiffrage, verification par encodage new mdp puis comparaison
new_mdp = hashlib.sha1(b'new mot de passe').hexdigest()

print(bool(mdp == new_mdp))

# Generation mdp aleatoire
import secrets

secrets.choice('abcdefghij')
# 'd'
# choisi un élt du str au hasard

secrets.token_hex(16)
# '835b4531d1a4624dc9fdebd80395c620'
# 16 chars de 2 elts