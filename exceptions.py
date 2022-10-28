class BaseError(Exception):
    message = 'Что то пошло не так'


class NotEnoughSpaceError(BaseError):
    message = 'недостаточно места'


class NotEnoughProductError(BaseError):
    message = 'Недостаточно места'


class TooManyDifferentProductsError(BaseError):
    message = 'Слишком много товаров'


class InvalidRequestError(BaseError):
    message = 'Неправильный запрос'


class UnknownStorageError(BaseError):
    message = 'Неизвестный склад'


class UnknownProductError(BaseError):
    message = 'Неизвестный товар'
