from solution1_classes import Car, Ride

ride1 = Ride((0, 0), (1, 3), 2, 9, "R1")
ride2 = Ride((1, 2), (1, 0), 0, 9, "R2")
ride3 = Ride((2, 0), (2, 2), 0, 9, "R3")
ride4 = Ride((0, 0), (1, 3), 2, 20, "R4")


# car1 = Car(10, "C1")

# car1.move_to(ride1.stop_pos)
# print("({}, {})".format(car1.x_pos, car1.y_pos))
#
# car1.move_to((4, 4))
# print("({}, {})".format(car1.x_pos, car1.y_pos))

# print(ride1.get_score())
# print(ride2.get_score())
# print(ride3.get_score())

print("=" * 60)

# TODO: Assign rides to cars
# Create a function to assign rides to cars
# To check if the car has enough steps left for the ride = steps remaining for the car to move - total steps needed to complete the ride
# total steps needed to complete the ride = steps from current position of the car to starting point of the ride + return value of get_distance method
def take_ride(car, ride):
    car.steps_taken = 0
    cars_original_pos = (car.x_pos, car.y_pos)
    # Check if the car has enough steps left for the ride
    steps_remaining = car.max_steps - car.total_steps_taken
    # if yes:
    if steps_remaining >= ride.stop_step:
        # move to the starting point of the ride
        car.move_to(ride.start_pos)
        # check if current step == starting step of the ride
        if car.steps_taken >= ride.start_step:
            # if yes:
            # move to end point of the ride
            car.move_to(ride.stop_pos)
        # else:
        else:
            # add the steps to wait to the steps taken by the car
            wait_time = ride.start_step - car.steps_taken
            car.steps_taken += wait_time
            # move to end point of the ride
            car.move_to(ride.stop_pos)
        # total_steps_taken = car.get_distance(cars_original_pos)
        print("Car's original co-ordinates: {}. Moved from {} to {}. I took {} steps".format(cars_original_pos, ride.start_pos, ride.stop_pos, car.steps_taken))
    # else: pass the ride to another car
    else:
        print("This car cannot take this ride!!!")


car2 = Car(10, "C2")
take_ride(car2, ride2)
# print(car2.x_pos)
# print(car2.y_pos)
# print(car2.steps_taken)

