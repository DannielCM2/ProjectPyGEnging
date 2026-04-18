class Input:
    def __init__(self):
        self._keys_down = set()
        self._keys_pressed = set()
        self._keys_released = set()
        self._prev_keys = set()

    def update(self, current_keys):
        self._keys_pressed = current_keys - self._keys_down
        self._keys_released = self._keys_down - current_keys
        self._keys_down = current_keys

    def key_down(self, key):
        return key in self._keys_down

    def was_pressed(self, key):
        return key in self._keys_pressed

    def was_released(self, key):
        return key in self._keys_released