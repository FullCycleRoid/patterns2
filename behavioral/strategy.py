import json
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, data: dict):
        pass


class JsonStrategy(Strategy):
    def execute(self, data: dict):
        print("Преобразование данных к json")
        return json.dumps(data)


class HtmlStrategy(Strategy):
    tags = set({"h1", "h2", "p", "div", "span"})

    def execute(self, data: dict):
        _html = ''
        print("\nПреобразование данных к html")
        for key, val in data.items():
            if key in self.tags:
                _html += '<'+key+'>' + val + '</'+key+'>\n'
        return _html


class TextStrategy(Strategy):
    def execute(self, data: dict):
        _text = ''
        print("Преобразование данных к строке")
        for val in data.values():
            _text += " " * 4 + val + "\n"
        return _text


class TextTransformer:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy


    def execute_strategy(self, data: dict):
        result = self.strategy.execute(data)
        print(f'Результат:\n{result}')

data = {
    "h1": "Заголовок",
    "p": "Параграф",
}


context = TextTransformer(TextStrategy())
context.execute_strategy(data)

context.strategy = JsonStrategy()
context.execute_strategy(data)

context.strategy = HtmlStrategy()
context.execute_strategy(data)
