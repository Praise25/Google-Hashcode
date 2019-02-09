class Ride:
    def __init__(self, start_pos, stop_pos, start_step, stop_step, _id):
        self.start_pos = start_pos
        self.stop_pos = stop_pos
        self.start_step = start_step
        self.stop_step  = stop_step
        self.id = _id
        self.is_taken = False

    def get_score(self):
        score = abs(self.start_pos[0] - self.stop_pos[0]) + abs(self.start_pos[1] - self.stop_pos[1])
        return score

    def get_distance(self):
        dist = abs(self.start_pos[0] - self.stop_pos[0]) + abs(self.start_pos[1] - self.stop_pos[1])
        return dist


class Car:
    def __init__(self, total_steps, _id):
        self.total_steps_taken = 0
        self.steps_taken = 0
        self.max_steps = total_steps
        self.x_pos = 0
        self.y_pos = 0
        self.is_busy = False
        self._id = _id
        self.rides_taken = []

    def move_to(self, position):
        current_x = self.x_pos
        current_y = self.y_pos
        end_x = position[0]
        end_y = position[1]
        distance = abs(current_x - end_x) + abs(current_y - end_y)
        self.steps_taken += distance
        self.total_steps_taken += self.steps_taken
        self.x_pos = end_x
        self.y_pos = end_y
        # print("Moved from {} to {}. I took {} steps".format((current_x, current_y), (end_x, end_y), distance))

        return distance

    def get_distance(self, position):
        current_x = self.x_pos
        current_y = self.y_pos
        end_x = position[0]
        end_y = position[1]
        distance = abs(current_x - end_x) + abs(current_y - end_y)

        return distance


# def parser(file):
#     # with open(file, "r") as input_file:
#         pass
