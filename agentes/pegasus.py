from typing import Literal

from pydantic import BaseModel, Field

from langchain_core.messages import HumanMessage, SystemMessage

from llm import LLMService


PROMPT_AGENTE_PEGASUS = """
Eres un especialista en las políticas de desarrollo back-end y front-end,
arquitectura de microservicios y conoces el mapa de dominios de la empresa
Santos Pegasus Soluciones.

Devuelve ÚNICAMENTE un JSON con el siguiente formato:

{
  "decision": "AUTO_RESOLVER" | "PEDIR_INFO" | "ABRIR_TICKET",
  "urgencia": "BAJA" | "MEDIANA" | "ALTA",
  "campos_faltantes": []
}

Reglas:

- AUTO_RESOLVER:
  Cuando la pregunta puede responderse consultando las políticas.

- PEDIR_INFO:
  Cuando falta información para entender la solicitud.

- ABRIR_TICKET:
  Cuando el usuario solicita una excepción,
  autorización, aprobación o abrir un ticket.
"""


class PegasusDecision(BaseModel):

    decision: Literal[
        "AUTO_RESOLVER",
        "PEDIR_INFO",
        "ABRIR_TICKET"
    ]

    urgencia: Literal[
        "BAJA",
        "MEDIANA",
        "ALTA"
    ]

    campos_faltantes: list[str] = Field(default_factory=list)


class PegasusAgent:

    def __init__(self):

        llm = LLMService()

        self.chain = llm.model.with_structured_output(
            PegasusDecision
        )

    def analyze(self, question: str) -> PegasusDecision:

        return self.chain.invoke(
            [
                SystemMessage(content=PROMPT_AGENTE_PEGASUS),
                HumanMessage(content=question)
            ]
        )