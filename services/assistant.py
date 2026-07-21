from agentes import PegasusAgent
from rag.service import RAGService


class AssistantService:

    def __init__(self, vectorstore):

        self.agent = PegasusAgent()

        self.rag = RAGService(vectorstore)

    def ask(self, question: str):

        decision = self.agent.analyze(question)

        if decision.decision == "AUTO_RESOLVER":

            respuesta = self.rag.ask(question)

            return {
                "tipo": "RESPUESTA",
                "decision": decision.model_dump(),
                "respuesta": respuesta
            }

        if decision.decision == "PEDIR_INFO":

            return {
                "tipo": "PEDIR_INFO",
                "decision": decision.model_dump(),
                "mensaje": (
                    "Necesito un poco más de información para ayudarte."
                )
            }

        return {
            "tipo": "ABRIR_TICKET",
            "decision": decision.model_dump(),
            "mensaje": (
                "La solicitud requiere abrir un ticket."
            )
        }