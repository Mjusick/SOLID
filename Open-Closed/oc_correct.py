"""
Principle: Open-Closed Principle
Rule: Objects or entities should be open for extension but closed for modification
Example: By creating a layer of abstraction we allow separate classes to be open for extensions without need to modify existing methods.
"""
from abc import ABC, abstractmethod


class BaseMessageSender(ABC):

    @abstractmethod
    def send_message(self, message_content):
        raise NotImplementedError("Method is not implemented")


class EmailSender(BaseMessageSender):
    def send_message(self, message_content):
        print(f"Email: '{message_content}' has been sent.")


class SlackSender(BaseMessageSender):
    def send_message(self, message_content):
        print(f"Slack message: '{message_content}' has been sent")
