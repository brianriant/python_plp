"""This module implements a smartphone class hierarchy."""

class Smartphone:
    """
    A base class representing a generic smartphone.
    
    Attributes:
        _brand (str): The brand of the smartphone
        _model (str): The model of the smartphone
        _battery_level (int): Current battery level as a percentage
        _battery_capacity (int): Maximum battery capacity in mAh
        _is_powered_on (bool): Power state of the phone
    """
    def __init__(self, brand, model, battery_capacity):
        self._brand = brand
        self._model = model
        self._battery_level = 100
        self._battery_capacity = battery_capacity
        self._is_powered_on = False

    def power_button(self):
        """Toggle the power state of the smartphone.

        Returns:
            str: A message indicating the new power state of the phone
        """
        self._is_powered_on = not self._is_powered_on
        return f"{self._brand} {self._model} is {'on' if self._is_powered_on else 'off'}"

    def charge(self, amount):
        """Charge the smartphone's battery.

        Args:
            amount (int): The amount of charge to add to the battery level

        Returns:
            str: A message indicating the current battery level
        """
        self._battery_level = min(100, self._battery_level + amount)
        return f"Battery level: {self._battery_level}%"

    def use_feature(self):
        """Use a generic feature of the smartphone.

        Returns:
            str: A message indicating the result of using the feature
        """
        if not self._is_powered_on:
            return "Phone is powered off"
        if self._battery_level < 5:
            return "Low battery!"
        self._battery_level -= 5
        return "Using generic feature"

class IPhone(Smartphone):
    """A class representing an iPhone smartphone.
    
    This class extends the Smartphone base class and adds Face ID functionality.
    """
    def __init__(self, model, battery_capacity):
        super().__init__("Apple", model, battery_capacity)
        self._face_id_enabled = True

    def use_feature(self):
        """Use Face ID authentication feature.

        Returns:
            str: A message indicating the result of using Face ID
        """
        if super().use_feature() == "Using generic feature":
            return "Using Face ID for authentication"
        return super().use_feature()

class AndroidPhone(Smartphone):
    """A class representing an Android smartphone.
    
    This class extends the Smartphone base class and adds fingerprint scanner functionality.
    """
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model, battery_capacity)
        self._fingerprint_enabled = True

    def use_feature(self):
        """Use fingerprint scanner feature.

        Returns:
            str: A message indicating the result of using the fingerprint scanner
        """
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
