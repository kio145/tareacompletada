from typing import List

def regresion(x):
    """
    wx + b
    """
    w = 1
    return x * w



class Neurona:

    def __init__(self, dendritas) -> None:
        self.dendritas = dendritas

    def sinapis(self, señales: List):
        assert len(señales) == len(self.dendritas)
        results = []
        for señal, dendrita in zip(señales, self.dendritas):
            results.append(señal * dendrita)
        nueva_señal = 1
        for result in results:
            nueva_señal = nueva_señal