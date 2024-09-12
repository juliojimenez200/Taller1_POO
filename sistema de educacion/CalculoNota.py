from abc import ABC, abstractmethod

class ICalculo(ABC):
    @abstractmethod
    def calcular(self, nota1: float, nota2: float, examen: float) -> float:
        # """
        # Método abstracto que calculará el promedio de dos notas.
        # """
        pass

    @abstractmethod
    def cal_status(self, promedio: float) -> str:
        # """
        # Método abstracto que determinará el estado del estudiante (aprobado, recuperación o reprobado).
        # """
        pass


class CalculoNotas:
    @staticmethod
    def calcular_promedio(parcial1: float, parcial2: float, examen: float) -> tuple:
        promedio = (parcial1  + parcial2  + examen )
        estado = CalculoNotas.cal_status(promedio)
        return promedio, estado

    @staticmethod
    def cal_status(promedio: float) -> str:
        if promedio >= 70:
            return "Aprobado"
        elif 40 <= promedio <= 69:
            return "Recuperación"
        else:
            return "Reprobado"
