class Employee:
    """
    Doc
    """
    def __init__(self, name, email_address, title, phone_number=''):
        self.name = name
        self.title = title
        self.email_address = email_address
        self.phone_number = phone_number

    def email_signature(self, include_phone=False):
        signature = f"{self.name} - {self.title}\n{self.email_address}"
        if include_phone and self.phone_number:
            signature += f" ({self.phone_number})"
        return signature

