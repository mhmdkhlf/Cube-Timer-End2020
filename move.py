class Move:
    def __init__(self, axis, layer, turn):
        self.axis = axis
        self.layer = layer
        self.turn = turn
    
    def get_axis(self):
        return self.axis
    
    def get_layer(self):
        return self.layer
    
    def get_turn(self):
        return self.turn
    
    def same_axis(self, *scramble_moves):
        for move in scramble_moves:
            if self.get_axis() != move.get_axis():
                return False
        return True
    
    def same_layer(self, *scramble_moves):
        for move in scramble_moves:
            if self.get_layer() != move.get_layer():
                return False
        return True