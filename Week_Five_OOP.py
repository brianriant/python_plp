class Smartphone:
    def __init__(self, brand, model, battery_capacity):
        self._brand = brand
        self._model = model
        self._battery_level = 100
        self._battery_capacity = battery_capacity
        self._is_powered_on = False

    def power_button(self):
        """
        Returns:
            _type_: _description_
        """

        self._is_powered_on = not self._is_powered_on
        return f"{self._brand} {self._model} is {'on' if self._is_powered_on else 'off'}"

    def charge(self, amount):
        """
        Args:
            amount (_type_): _description_

        Returns:
            _type_: _description_
        """

        self._battery_level = min(100, self._battery_level + amount)
        return f"Battery level: {self._battery_level}%"

    def use_feature(self):
        """
        Returns:
            _type_: _description_
        """

        if not self._is_powered_on:
            return "Phone is powered off"
        if self._battery_level < 5:
            return "Low battery!"
        self._battery_level -= 5
        return "Using generic feature"

class IPhone(Smartphone):
    """
    Args:
        Smartphone (_type_): _description_
    """

    def __init__(self, model, battery_capacity):
        super().__init__("Apple", model, battery_capacity)
        self._face_id_enabled = True

    def use_feature(self):
        if super().use_feature() == "Using generic feature":
            return "Using Face ID for authentication"
        return super().use_feature()

class AndroidPhone(Smartphone):
    """
    Args:
        Smartphone (_type_): _description_
    """

    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model, battery_capacity)
        self._fingerprint_enabled = True

    def use_feature(self):
        if super().use_feature() == "Using generic feature":
            return "Using Fingerprint Scanner"
        return super().use_feature()

# Example usage
iphone = IPhone("14 Pro", 4000)
samsung = AndroidPhone("Samsung", "S23", 5000)

print(iphone.power_button())
print(iphone.use_feature())
print(samsung.power_button())
print(samsung.use_feature())
