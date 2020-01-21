import numpy as np

class IterativeMap():
    """
    This is a class for defining generic iterative maps
    """
    def __init__(self, map_, **map_args, initial_value):
        """
        ---------
        Arguments
        ----------
        map_ = family of iterative maps with the parameters not set
        map_args = dictionary of parameters for our map
        initial_value = initial value for iteration
        """
        self.map_ =  map_
        self.map_args = map_args
        self.map = lambda x: self.map_(x, **self.map_args)
        self.initial_value = initial_value
        self.current_value = initial_value

    def reset_params(self, **new_map_args, new_initial_value = None):
        self.map_args = new_map_args
        self.map = lambda x: self.map_(x, **self.map_args)
        if new_initial_value is not None:
            self.initial_value = new_initial_value

    def generate_path(iterations):
        self.path = np.zeros(iterations)
        for itr in range(iterations):
            self.current_value = self.map(self.current_value)
            self.path[itr] = self.current_value
        return self.path
