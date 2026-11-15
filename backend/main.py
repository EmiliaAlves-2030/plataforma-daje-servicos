from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
import math

app = FastAPI(title="DAJE Servicos - Apoio em Campo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VistoriaSchema(BaseModel):
    comprimento: float
    largura: float
    tem_desnivel: bool = False
    tem_umidade: bool = False

    @field_validator("comprimento", "largura", mode="before")
    def tratar_virgula(cls, v):
        if isinstance(v, str):
            v = v.replace(",", ".").strip()
        try:
            valor = float(v)
            if valor <= 0:
                raise ValueError
            return valor
        except (ValueError, TypeError):
            raise HTTPException(status_code=400, detail="Medida informada e invalida")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/vistoria")
def calcular_vistoria(dados: VistoriaSchema):
    area = dados.comprimento * dados.largura
    
    # 10% de folga para recortes de piso
    area_total = area * 1.10
    
    # Cada caixa de vinilico cobre em media 3.34 m2
    caixas_piso = math.ceil(area_total / 3.34)
    
    # Argamassa de regularizacao (aprox. 4kg por m2 se houver desnível)
    kg_argamassa = math.ceil(area * 4) if dados.tem_desnivel else 0
    
    aprovado = not (dados.tem_desnivel or dados.tem_umidade)
    
    msg = "Contrapiso aprovado para instalacao."
    
    if dados.tem_desnivel and dados.tem_umidade:
        msg = "Regularizar desnivel com argamassa e tratar umidade antes de instalar."
    elif dados.tem_desnivel:
        msg = f"Aplicar aprox. {kg_argamassa}kg de argamassa de regularizacao antes da colagem."
    elif dados.tem_umidade:
        msg = "Contrapiso com umidade. Necessario secagem/impermeabilizacao."
        
    return {
        "area_m2": round(area, 2),
        "caixas_piso": caixas_piso,
        "kg_argamassa": kg_argamassa,
        "aprovado": aprovado,
        "mensagem": msg
    }
