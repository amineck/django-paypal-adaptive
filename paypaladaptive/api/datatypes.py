from errors import ReceiverError


class Receiver():
    email = None
    amount = None

    def __init__(self, email=None, amount=None):
        self.email = email
        self.amount = amount

    def to_dict(self):
        obj = {'email': self.email,
                'amount': self.amount}
        return obj

    def __unicode__(self):
        return self.email


class ReceiverList():
    receivers = None

    def __init__(self, receivers=None):
        self.receivers = []
        if receivers is not None:
            for receiver in receivers:
                self.append(receiver)

    def append(self, receiver):
        if not isinstance(receiver, Receiver):
            raise ReceiverError("receiver needs to be instance of Receiver")
        self.receivers.append(receiver)

    def to_dict(self):
        return [r.to_dict() for r in self.receivers]

    def __len__(self):
        return len(self.receivers)

    @property
    def total_amount(self):
        return sum([r.amount for r in self.receivers])
