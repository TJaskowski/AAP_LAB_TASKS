# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.quantity += amount

    def remove_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if amount > self.quantity:
            raise ValueError("Not enough stock available")
        self.quantity -= amount

    def is_available(self) -> bool:
        return self.quantity > 0        

    def total_value(self) -> float:
        return self.price * self.quantity
    
    def apply_discount(self, discount_percentage: float):
        """Obniza cene o podany procent (0-100)."""
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Percent must be between 0 and 100")
        self.price = self.price * (1 - discount_percentage / 100)