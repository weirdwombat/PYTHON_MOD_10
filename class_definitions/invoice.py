class Invoice:
    def __init__(self, iid, cid, lname, fname, phone, address, items_with_price=0):
        self.invoice_id = iid
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = phone
        self.address = address
        self.items_with_price = items_with_price

    def set_items_with_price(self, items_with_price):
        items_with_price = {}

    def display(self):
        pass

if __name__ == '__main__':
    invoice = Invoice(891, 1235, 'Mouse', 'Minnie', '555-867-5309', '1313 Disneyland Dr, Anaheim, CA 92802')
