from db import Base
from sqlalchemy import Column, Float, Integer, DateTime, String

class vra(Base):
    """
    Model for VRA json data files
    """
    __tablename__ = 'vra'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    icao_empresa_aerea = Column(String,nullable=True)
    numero_voo = Column(String,nullable=True)
    codigo_autorizacao = Column(String,nullable=True)
    codigo_tipo_linha = Column(String,nullable=True)
    icao_aerodromo_origem = Column(String,nullable=True)
    icao_aerodromo_destino = Column(String,nullable=True)
    partida_prevista = Column(DateTime,nullable=True)
    partida_real = Column(DateTime,nullable=True)
    chegada_prevista = Column(DateTime,nullable=True)
    chegada_real = Column(DateTime,nullable=True)
    situacao_voo = Column(String,nullable=True)
    codigo_justificativa = Column(String,nullable=True)