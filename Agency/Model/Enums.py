from enum import Enum


class UserType(Enum):
    REGULAR = 0
    AGENT = 1
    OWNER = 2
    ADMIN = 3

class SearchData(Enum):
    ALL = (0, "SVE")
    LOCATION = (1, "LOKACIJA")
    PRICE = (2, "CENA")
    SALE = (3, "PRODAJA")
    RENT = (4, "IZDAVANJE")
    AREA = (5, "POVRŠINA")
    TYPE = (6, "TIP")

class Rate(Enum):
    LIKE = 0
    DISLIKE = 1

class ValidType(Enum):
    USER_ADDED = (1, "REGISTRACIJA KORISNIKA", "USPESNO REGISTROVAN KORISNIK")
    AGENT_ADDED = (2, "REGISTRACIJA AGENTA", "USPESNO REGISTROVAN AGENT")
    OWNER_ADDED = (3, "REGISTRACIJA VLASNIKA", "USPESNO REGISTROVAN VLASNIK")
    REAL_ESTATE_ADDED = (4, "DODAVANJE NEKRETNINE", "USPESNO DODANA NEKRETNINA")
    LOGIN_SUCCESS = (5, "PRIJAVA", "USPESNA PRIJAVA")
    USER_NOT_ADDED = (-1, "REGISTRACIJA KORISNIKA", "NEUSPESNO REGISTROVAN KORISNIK")
    AGENT_NOT_ADDED = (-2, "REGISTRACIJA AGENTA", "NEUSPESNO REGISTROVAN AGENT")
    OWNER_NOT_ADDED = (-3, "REGISTRACIJA VLASNIKA", "NEUSPESNO REGISTROVAN VLASNIK")
    REAL_ESTATE_NOT_ADDED = (-4, "DODAVANJE NEKRETNINE", "NEUSPESNO DODANA NEKRETNINA")
    LOGIN_NOT_SUCCESS = (-5, "PRIJAVA", "NEUSPESNA PRIJAVA")