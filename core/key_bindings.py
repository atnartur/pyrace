class KeyBindings:
    __bindings = {}

    @staticmethod
    def register(key, value):
        KeyBindings.__bindings[key] = value

    @staticmethod
    def deregister(key):
        newDict = KeyBindings.__bindings.copy()
        del newDict[key]
        KeyBindings.__bindings = newDict

    @staticmethod
    def exec(keys):
        for key in KeyBindings.__bindings:
            if keys[key]:
                KeyBindings.__bindings[key]()
