from abc import ABC, abstractmethod

# Абстрактный класс обработчика
class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        pass

# Конкретный обработчик 1: Базовая скидка
class BasicDiscountHandler(Handler):
    def handle(self, request):
        if request == "basic":
            print("Применена базовая скидка!")
        elif self.next_handler:
            self.next_handler.handle(request)
        else:
            print("Нет подходящей скидки.")

# Конкретный обработчик 2: Специальное предложение
class SpecialOfferHandler(Handler):
    def handle(self, request):
        if request == "special":
            print("Применено специальное предложение!")
        elif self.next_handler:
            self.next_handler.handle(request)

# Конкретный обработчик 3: VIP-скидка
class VipDiscountHandler(Handler):
    def handle(self, request):
        if request == "vip":
            print("Применена VIP-скидка!")
        elif self.next_handler:
            self.next_handler.handle(request)

# Создание цепочки обработчиков
def setup_chain():
    basic_handler = BasicDiscountHandler()
    special_handler = SpecialOfferHandler()
    vip_handler = VipDiscountHandler()

    # Устанавливаем последовательность обработчиков
    basic_handler.set_next(special_handler).set_next(vip_handler)
    return basic_handler

# Тестирование
if __name__ == "__main__":
    chain = setup_chain()

    print("Запрос 'basic':")
    chain.handle("basic")  # Обрабатывается BasicDiscountHandler

    print("\nЗапрос 'special':")
    chain.handle("special")  # Обрабатывается SpecialOfferHandler

    print("\nЗапрос 'vip':")
    chain.handle("vip")  # Обрабатывается VipDiscountHandler

    print("\nЗапрос 'none':")
    chain.handle("none")  # Нет подходящей скидки