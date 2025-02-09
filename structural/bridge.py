from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotification(NotificationSender):
    def send_notification(self, message):
        return f"Отправлено email-уведомление: {message}"


class PushNotification(NotificationSender):
    def send_notification(self, message):
        return f"Отправлено push-уведомление: {message}"


class NotificationManager:
    def __init__(self, sender: NotificationSender):
        self._sender = sender

    def notify(self, message):
        return self._sender.send_notification(message)


class AdvancedNotificationManager(NotificationManager):
    def notify_with_priority(self, message, priority):
        if priority == "high":
            return f"Важное уведомление: {self.notify(message)}"
        else:
            return f"Обычное уведомление: {self.notify(message)}"




if __name__ == "__main__":
    email_sender = EmailNotification()
    push_sender = PushNotification()

    basic_manager = NotificationManager(email_sender)
    print(basic_manager.notify("Привет! Это ваше первое уведомление."))

    advanced_manager = AdvancedNotificationManager(push_sender)
    print(advanced_manager.notify_with_priority("Срочное сообщение!", "high"))
    print(advanced_manager.notify_with_priority("Не очень важное сообщение.", "low"))