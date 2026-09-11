#!/usr/bin/env python3

class CashRegister:
    """Represents a cash register for an e-commerce store."""

    def __init__(self, discount=0):
        # Store the discount through the property setter for validation.
        self._discount = 0
        self.discount = discount

        # Start the register with no total or items.
        self.total = 0
        self.items = []

        # Transactions are stored so the latest one can be voided.
        self.previous_transactions = []

    @property
    def discount(self):
        """Return the current discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Validate and set the discount percentage."""
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        """Add an item and its transaction details to the register."""

        # Increase the total based on the item's price and quantity.
        self.total += price * quantity

        # Store each purchased item in the items list.
        for _ in range(quantity):
            self.items.append(item)

        # Save the transaction so it can be reversed later.
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """Apply the current percentage discount to the total."""

        # There is nothing to apply when the discount is zero.
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate the amount after applying the percentage discount.
        self.total = self.total * (1 - self.discount / 100)

        # Display whole-number totals without a decimal.
        if self.total == int(self.total):
            self.total = int(self.total)

        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        """Remove the most recent transaction from the register."""

        # Stop if there are no transactions to remove.
        if not self.previous_transactions:
            return

        # Retrieve and remove the most recent transaction.
        transaction = self.previous_transactions.pop()

        item = transaction["item"]
        price = transaction["price"]
        quantity = transaction["quantity"]

        # Subtract the transaction amount from the register total.
        self.total -= price * quantity

        # Remove the purchased items from the items list.
        for _ in range(quantity):
            self.items.remove(item)