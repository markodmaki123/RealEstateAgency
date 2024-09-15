from abc import ABC
from RealEstateAgency.Agency.Model.Enums import UserType


class User(ABC):

    def __init__(self, info_dict):
        self._pk = info_dict["pk"]
        self._password = info_dict["password"]
        self._name = info_dict["name"]
        self._surname = info_dict["surname"]
        self._address = info_dict["address"]
        self._email = info_dict["email"]
        self._user_type = UserType(info_dict["user_type"])
        self._phone_number = info_dict["phone_number"]

    @property
    def pk(self):
        return self._pk


    @property
    def password(self):
        return self._password


    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def address_pk(self):
        return self._address[0]

    @property
    def address(self):
        return self._address[1]

    @property
    def email(self):
        return self._email

    @property
    def user_type(self):
        return self._user_type

    @address.setter
    def address(self, a):
        self._address[1] = a

    @password.setter
    def password(self, p):
        self._password = p


    def to_user_dict(self):
        user_dict = {
            "pk": self._pk,
            "password": self._password,
            "name": self._name,
            "surname": self._surname,
            "address": self._address.to_dict() if self._address else None,
            "email": self._email,
            "user_type": self._user_type.value,
            "phone_number": self._phone_number
        }
        return user_dict

    @pk.setter
    def pk(self, value):
        self._pk = value