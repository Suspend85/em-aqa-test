from enum import Enum


class AllureTag(str, Enum):
    REGRESSION = 'REGRESSION'
    USER_LOGIN = 'USER_LOGIN'
    AUTHORIZATION = 'AUTHORIZATION'
