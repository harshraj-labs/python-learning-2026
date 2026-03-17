#Build a Travel Weather Planner

distance_mi = 1
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

if distance_mi:
    if distance_mi<=1 and is_raining:
        print("False")
    if distance_mi<=1 and (not is_raining):
        print("True")
    elif distance_mi>1 and distance_mi<=6   and (not has_bike) and is_raining:
        print("False")
    elif distance_mi>1 and distance_mi<=6   and (not has_bike) and (not is_raining):
        print("False")
    elif distance_mi>1 and distance_mi<=6   and has_bike and (not is_raining):
        print("True")
    elif distance_mi>6 and (has_car or has_ride_share_app):
        print("True")
    elif distance_mi>6 and not(has_car or has_ride_share_app):
        print("False")
else:
    print("False")