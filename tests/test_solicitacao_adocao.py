import pytest

from adocao.pet import Pet
from adocao.solicitacao_adocao import SolicitacaoAdocao, Status

rex = Pet("Rex", "cachorro")
mia = Pet("Mia", "gato")


def test_nova_solicitacao_comeca_pendente():
    assert SolicitacaoAdocao(rex, "Ana", 18).status == Status.PENDENTE
    assert SolicitacaoAdocao(mia, "Carlos", 40).status == Status.PENDENTE


def test_aprovar_solicitacao_pendente():
    s = SolicitacaoAdocao(rex, "Ana", 25)
    s.aprovar()
    assert s.status == Status.APROVADA
    with pytest.raises(RuntimeError):
        s.aprovar()


def test_recusar_solicitacao_pendente():
    s = SolicitacaoAdocao(mia, "Bruno", 30)
    s.recusar()
    assert s.status == Status.RECUSADA
    with pytest.raises(RuntimeError):
        s.recusar()


def test_nao_permite_mudar_decisao_ja_tomada():
    aprovada = SolicitacaoAdocao(rex, "Ana", 25)
    aprovada.aprovar()
    with pytest.raises(RuntimeError):
        aprovada.recusar()

    recusada = SolicitacaoAdocao(mia, "Bruno", 30)
    recusada.recusar()
    with pytest.raises(RuntimeError):
        recusada.aprovar()


def test_menor_de_idade_nao_pode_solicitar():
    with pytest.raises(ValueError):
        SolicitacaoAdocao(rex, "Joao", 17)
    with pytest.raises(ValueError):
        SolicitacaoAdocao(mia, "Pedro", 10)


def test_guarda_dados_da_solicitacao():
    s1 = SolicitacaoAdocao(rex, "Ana", 25)
    assert s1.nome_adotante == "Ana"
    assert s1.pet.nome == "Rex"
    s2 = SolicitacaoAdocao(mia, "Carlos", 40)
    assert s2.nome_adotante == "Carlos"
    assert s2.pet.nome == "Mia"
