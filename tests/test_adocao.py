from adocao.adocao import filtrar_por_especie, pode_adotar
from adocao.pet import Pet


def test_maior_de_idade_pode_adotar():
    assert pode_adotar(18)


def test_menor_de_idade_nao_pode_adotar():
    assert not pode_adotar(17)


def test_filtra_pets_por_especie():
    pets = [Pet("Rex", "cachorro"), Pet("Mia", "gato"), Pet("Bob", "Cachorro")]
    assert len(filtrar_por_especie(pets, "cachorro")) == 2
