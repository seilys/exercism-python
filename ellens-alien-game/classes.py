"""Solution to Ellen's Alien Game exercise."""

def new_aliens_collection(start_positions):
    return [Alien(position[0], position[1]) for position in start_positions]


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    health = 3
    total_aliens_created = 0
    
    def __init__(self, x_coordinate, y_coordinate):
        Alien.total_aliens_created += 1
        
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


    def is_alive(self):
        return self.health > 0


    def hit(self):
        self.health -= 1


    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate


    def collision_detection(self, other_object):
        pass
