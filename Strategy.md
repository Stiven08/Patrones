# ESTRATEGIA - (STRATEGY)
Patron de diseño de comportamiento, que define y organiza grupos de algoritmos que
asigna a cada uno de ellos por clases separadas y hace sus objetos intercambiables.

import abc
class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()
    
class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def algorithm_interface(self):
        pass

class ConcreteStrategyA(Strategy):
    def algorithm_interface(self):
        pass

class ConcreteStrategyB(Strategy):
    def algorithm_interface(self):
        pass
    
def main():
    concrete_strategy_a = ConcreteStrategyA()
    context = Context(concrete_strategy_a)
    context.context_interface()
    
if __name__ == "__main__":
    main()
