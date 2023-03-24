from gato.gato import Gato
from cachorro.cachorro import Cachorro

gato = Gato('Zezinho', 'bege', 'macho', 'siamês')
cachorro = Cachorro('Marley', 'marrom', 'macho', 12.5)
print(gato)
gato.comer()
gato.miar()
print(cachorro)
cachorro.comer()
cachorro.latir()
