def validate_pin(pin):
    if ("." not in pin) and (len(pin) == 4 or len(pin) == 6) and (pin.isdigit()) and (int(pin) >= 0):
        return True
    else:
        return False
