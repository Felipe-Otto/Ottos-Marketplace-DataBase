class Position:
    def __init__(self, position_key, position_name):
        self.position_key = position_key
        self.position_name = position_name

    def __str__(self):
        return f'Position [Primary Key: \033[1;32m{self.position_key}\033[0m, ' \
               f'Name: \033[1;32m{self.position_name}\033[0m]'

    def get_position_key(self):
        return self.position_key

    def set_position_key(self, position_key):
        self.position_key = position_key

    def get_position_name(self):
        return self.position_name

    def set_position_name(self, position_name):
        self.position_name = position_name
