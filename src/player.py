# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room=''):
        self.current_room = current_room

    def move(self):
        direction = {}
# hasattr() method returns true if an object has the given named attribute and false if it does not.
#takes two parameters:
# object - object whose named attribute is to be checked
# name - name of the attribute to be searched

        if hasattr(self.current_room, 'n_to'):
            direction['n'] = self.current_room.n_to.name

        if hasattr(self.current_room, 's_to'):
            direction['s'] = self.current_room.e_to.name

        if hasattr(self.current_room, 'e_to'):
            direction['e'] = self.current_room.s_to.name

        if hasattr(self.current_room, 'w_to'):
            direction['w'] = self.current_room.w_to.name

        return direction

    def __str__(self):
        return (f'{self.current_room}')
