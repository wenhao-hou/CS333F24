import abc
from datetime import datetime

class AbstractModel(abc.ABC):
    """
    Abstract base class for models in the MVC pattern.
    """

    @abc.abstractmethod
    def select(self):
        """
        Retrieves all entries from the database.

        :return: A list of dictionaries, each representing an entry.
        """
        pass

    @abc.abstractmethod
    def insert(self, name, description, street_address, type_of_service, phone_number, hours_of_operation, reviews):
        """
        Inserts a new entry into the database.

        :param name: The name of the service.
        :param description: A description of the service.
        :param street_address: The street address of the service location.
        :param type_of_service: The type of service offered.
        :param phone_number: Contact phone number for the service.
        :param hours_of_operation: The hours during which the service operates.
        :param reviews: Reviews or feedback for the service.
        """
        pass

# Below is the PyListModel class which is a list-based implementation of the AbstractModel.
class PyListModel(AbstractModel):
    def __init__(self):
        self.entries = []

    def select(self):
        """
        Retrieves all entries from the list.

        :return: A list of dictionaries, each representing an entry.
        """
        return self.entries

    def insert(self, name, description, street_address, type_of_service, phone_number, hours_of_operation, reviews):
        """
        Inserts a new entry into the list.

        :param name: The name of the service.
        :param description: A description of the service.
        :param street_address: The street address of the service location.
        :param type_of_service: The type of service offered.
        :param phone_number: Contact phone number for the service.
        :param hours_of_operation: The hours during which the service operates.
        :param reviews: Reviews or feedback for the service.
        """
        entry = {
            'name': name,
            'description': description,
            'street_address': street_address,
            'type_of_service': type_of_service,
            'phone_number': phone_number,
            'hours_of_operation': hours_of_operation,
            'reviews': reviews,
            'id': len(self.entries) + 1,  # simple incrementing ID, not safe for concurrent use
            'created_at': datetime.now().isoformat()  # timestamp for when the entry was created
        }
        self.entries.append(entry)
