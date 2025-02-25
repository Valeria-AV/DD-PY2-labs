discount = 10
class Jewelry:
    """Класс, описывающий объект Украшение, который будет использоваться для украшений, которые хранятся в магазине."""

    def __init__(self, unique_number: int, material: str, price: int):
        """
        Создание объекта Украшение

        :param unique_number: Уникальный номер изделия
        :param material: Материал изделия
        :param price: Цена изделия
        """

        self._unique_number = unique_number
        self._material = material
        self._price = price
    @property
    def unique_number(self) -> int:
        """Возвращает уникальный номер изделия."""

        return self._unique_number

    @unique_number.setter
    def unique_number(self, new_number: int) -> None:
        """Устанавливает новый номер изделия."""

        ...  # Проверки нового значения
        self._unique_number = new_number

    @property
    def material(self) -> str:
        """Возвращает материал изделия."""

        return self._material

    @material.setter
    def material(self, new_material: str) -> None:
        """Устанавливает новый материал изделия."""

        ...  # Проверки нового значения
        self._material = new_material

    @property
    def price(self) -> int:
        """Возвращает цену изделия."""

        return self._price

    @price.setter
    def price(self, new_price: int) -> None:
        """Устанавливает новую цену изделия."""

        ...  # Проверки нового значения
        self._price = new_price

    def __str__(self) -> str:
        return f'Украшение № {self.unique_number}, {self.material}, {self.price}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.unique_number!r}, {self.material!r}, {self.price!r})'


class Chain(Jewelry):
    """Класс, описывающий объект Цепочка."""

    def __init__(self, unique_number: int, material: str, price: int, length: int):
        """
        Создание объекта Цепочка

        :param unique_number: Уникальный номер изделия
        :param material: Материал изделия
        :param price: Цена изделия
        :param length: Длина изделия
        """

        super().__init__(unique_number, material, price)
        self._length = length
        self._price = None  # Для инициализация атрибута в сеттере, для учета скидки
        self.price = price

    @property
    def length(self) -> int:
        """Возвращает длину цепочки."""

        return self._length

    @length.setter
    def length(self, new_length: int) -> None:
        """Устанавливает новую длину изделия."""

        ...  # Проверки нового значения
        self._length = new_length

    @property
    def price(self) -> int:
        """Возвращает цену изделия."""

        return self._price

    @price.setter
    def price(self, new_price: int) -> None:
        """Устанавливает новую цену изделия с учетом скидки на цепочки."""

        ...  # Проверки нового значения
        self._price = round(new_price - (new_price * discount / 100))

    def __str__(self) -> str:
        """Перегружаем метод str, меняем название на "Цепочка" и добавляем новую характеристику: длину изделия."""

        return f'Цепочка № {self.unique_number}, {self.material}, {self.price}, длиной {self.length} см'

    def __repr__(self) -> str:
        """Перегружаем метод repr, добавляем новую характеристику: длину изделия."""

        return f'{self.__class__.__name__}({self.unique_number!r}, {self.material!r}, {self.price!r}, {self.length!r})'
