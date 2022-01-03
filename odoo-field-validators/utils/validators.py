import re

from .exception import ValidateFieldException


class BaseValidator:
    default_message = "Value {} is invalid. Enter valid value"

    def __init__(self, message=None):
        self._message = message if message is not None else self.default_message

    def __call__(self, value):
        compared_value = self._get_value(value)
        is_valid_value = self._is_valid_value(compared_value)
        if not is_valid_value:
            raise ValidateFieldException(self._format_error_message(value))

    def _is_valid_value(self, value):
        raise NotImplementedError()

    def _format_error_message(self, value):
        return self._message.format(value)

    def _get_value(self, value):
        return value


class RegexValidator(BaseValidator):
    def __init__(self, regex, message=None):
        self._regex = regex
        super().__init__(message)

    def _is_valid_value(self, value):
        return bool(re.match(self._regex, value))


class EmailValidator(RegexValidator):
    EMAIL_REGEX = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    def __init__(self, message=None):
        super().__init__(self.EMAIL_REGEX, message)


class TelegramLinkValidator(RegexValidator):
    TELEGRAM_LINK_REGEX = (
        r"^(http(s)?:\/\/)?(t(elegram)?\.me|telegram\.org)\/[A-z0-9\_]{5,32}\/?$"
    )
    default_message = (
        "Link {} is invalid. Telegram link could be like https://t.me/<channel name>/"
    )

    def __init__(self, message=None):
        super().__init__(self.TELEGRAM_LINK_REGEX, message)


class LimitValueValidator(BaseValidator):
    def __init__(self, limit_value, message=None):
        self._limit_value = limit_value
        super().__init__(message)

    def _format_error_message(self, value):
        return self._message.format(value, self._limit_value)


class MinValueValidator(LimitValueValidator):
    default_message = "Value {} is less than or equal to {}."

    def _is_valid_value(self, value):
        return value > self._limit_value


class MaxValueValidator(LimitValueValidator):
    default_message = "Value {} is greater than or equal to {}."

    def _is_valid_value(self, value):
        return value < self._limit_value


class LimitLengthValidator(LimitValueValidator):
    def _get_value(self, value):
        return len(value)


class MinLengthValidator(LimitLengthValidator):
    default_message = "Length of {} is less than or equal to {}."

    def _is_valid_value(self, value):
        return value > self._limit_value


class MaxLengthValidator(LimitLengthValidator):
    default_message = "Length of {} is greater than or equal to {}."

    def _is_valid_value(self, value):
        return value < self._limit_value
