from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_vistoria_com_virgula_e_aprovada():
    payload = {
        "comprimento": "5,0",
        "largura": "4,0",
        "tem_desnivel": False,
        "tem_umidade": False
    }
    
    res = client.post("/vistoria", json=payload)
    assert res.status_code == 200
    
    dados = res.json()
    assert dados["area_m2"] == 20.0
    assert dados["aprovado"] is True
    assert dados["caixas_piso"] == 7

def test_vistoria_com_desnivel():
    payload = {
        "comprimento": 3.0,
        "largura": 3.0,
        "tem_desnivel": True,
        "tem_umidade": False
    }
    
    res = client.post("/vistoria", json=payload)
    assert res.status_code == 200
    
    dados = res.json()
    assert dados["aprovado"] is False
    assert dados["kg_argamassa"] > 0
