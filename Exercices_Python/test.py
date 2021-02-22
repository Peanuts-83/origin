# Creation de classe avec passage d'attributs et évaluat°
class User:

    def check_pwd(self, password):
        print(password, '-', self.password == password)


tom = User()
tom.id = 1
tom.name = 'tom'
tom.password = 'azerty'
tom.check_pwd('lulu')
tom.check_pwd('azerty')

# Le password est privatisé avec _ (reste accessible par obj._attr) ou __ (accessible par obj._Class__attr)
# crypt >> module de cryptage du password
import crypt
class User1:

    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self._salt = crypt.mksalt() # sel utilisé pour le hash du password
        self._password = self._crypt_pwd(password)

    def _crypt_pwd(self, password):
        return crypt.crypt(password, self._salt)

    def check_pwd(self, password):
        print(self._password == password)

tom = User1(2, 'tomtom', 'qsdfgh')


