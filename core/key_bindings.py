class KeyBindings:
    __bindings = {}

    @staticmethod
    def register(key, value):
        dir(KeyBindings)
        KeyBindings.__bindings[key] = value

    @staticmethod
    def exec(keys):
        for key in KeyBindings.__bindings:
            if keys[key]:
                KeyBindings.__bindings[key]()
