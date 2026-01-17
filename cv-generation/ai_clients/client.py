from abc import ABC, abstractmethod

class AiClient(ABC):

    def __init__(self, model: str):
        self.model = model

    @abstractmethod
    def create(self, prompt: str) -> str:
        pass
