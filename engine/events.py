class Input:
    def __init__(self):
        self._keys_down = set()
        self._keys_pressed = set()
        self._keys_released = set()
 
    def key_down(self, key):
        if key not in self.keys_down:
            self._keys_down.add(key)
            self._keys_pressed.add(key)
            
    def key_up(self, key):
        if key in self.keys_down:
            self._keys_down.remove(key)
            self._keys_released.add(key)

    def is_down(self, key):
        return key in self._keys_down
    
    @property
    def keys_pressed(self):
        return self._keys_pressed
    
    @property
    def keys_down(self):
        return self._keys_down

    def was_pressed(self, key):
        return key in self._keys_pressed

    def was_released(self, key):
        return key in self._keys_released

    def reset(self):
        self._keys_pressed.clear()
        self._keys_released.clear()