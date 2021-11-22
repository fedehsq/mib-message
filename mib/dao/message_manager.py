from mib.dao.manager import Manager
from mib.models.message import Message


class MessageManager(Manager):

    @staticmethod
    def create_message(message: Message):
        Manager.create(message=message)

    @staticmethod
    def retrieve_by_id(id_):
        Manager.check_none(id=id_)
        return Message.query.get(id_)

    @staticmethod
    def retrieve_by_email(email):
        Manager.check_none(email=email)
        return Message.query.filter(Message.email == email).first()

    @staticmethod
    def update_message(message: Message):
        Manager.update(message=message)

    @staticmethod
    def delete_message(message: Message):
        Manager.delete(message=message)

    @staticmethod
    def delete_message_by_id(id_: int):
        message = MessageManager.retrieve_by_id(id_)
        MessageManager.delete_message(message)
