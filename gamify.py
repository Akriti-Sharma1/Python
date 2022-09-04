def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    global elapsed_time
    global offer_time
    global offered_activity

    global did_textbooks
    global did_running

    global checker_run
    global checker_rest
    global checker_textbooks

    did_textbooks = False
    did_running = False

    global last_finished
    global bored_with_stars
    global star_counter

    star_counter = 0
    cur_hedons = 0
    cur_health = 0

    cur_star = None
    cur_star_activity = None
    offered_activity = None
    offer_time = 0

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    global resting_counter, checking_counter
    resting_counter = 0
    checking_counter = 0
    cur_time = 0

    last_finished = -1000

def perform_activity(activity, duration):
    global cur_health, cur_time, cur_activity, last_activity_duration, last_activity, cur_hedons, elapsed_time, resting_counter, offered_activity, did_running, did_textbooks, checking_counter
    cur_time += duration
    if activity == "running":
        if duration <= 180:
            cur_health += duration * 3
            resting_counter = 0
            did_running = True
            did_textbooks = False
        else:
            cur_health += 540 + (duration - 180)
            did_running = True
            did_textbooks = False
    elif activity == "textbooks":
        cur_health += duration * 2
        resting_counter = 0
        did_running = False
        did_textbooks = True
    elif activity == "resting":
        cur_health = cur_health
        resting_counter = duration
        did_running = False
        did_textbooks = False

    offer_star(activity)

    if checking_counter == 0:
        did_textbooks = False
        did_running = False
        checking_counter += 1

    if did_running or did_textbooks and resting_counter < 120:
        offer_star(activity)
        if offered_activity == activity and offer_time == cur_time:
            if duration <= 10:
                if activity == "running":
                    cur_hedons += duration * 2 + 3
                elif activity == "textbooks":
                    cur_hedons += 23 + ((duration-10))-2
        elif activity == "running" or activity == "textbooks":
            cur_hedons += -2 * duration
            offered_activity = None
            star_counter = 0
    else:
        if activity == "running":
            if duration <= 10:
                cur_hedons += duration * 2
                offered_activity = None
                star_counter = 0
            else:
                cur_hedons += 20 + ((duration-10)*-2)
                offered_activity = None
                star_counter = 0
        elif activity == "textbooks":
            if duration <= 20:
                cur_hedons += duration
                offered_activity = None
                star_counter = 0
            else:
                cur_hedons += 20 + (duration - 20)
                offered_activity = None
                star_counter = 0
        elif activity == "resting":
            cur_hedons = cur_hedons
            offered_activity = None
            star_counter = 0

    return cur_health, cur_hedons, did_running, did_textbooks

def get_cur_hedons():
    return cur_hedons

def get_cur_health():
    return cur_health

def get_cur_time():
    return cur_time

def offer_star(activity):
    global offer_time, offered_activity, star_counter, did_textbooks, did_running
    while star_counter < 3:
        offered_activity = activity
        offer_time = cur_time
        star_counter += 1
        if checking_counter > 0:
            if activity == "running":
                did_running = True
            elif activity == "textbooks":
                did_textbooks = True
#         if activity == "running":
#             did_running = False
#             did_textbooks = False
#         elif activity == "textbooks":
#             did_textbooks = False
#             did_running = False

    return offered_activity, did_running, did_textbooks
        #star_can_be_taken(activity)

def star_can_be_taken(activity):
     global offer_time
     if did_running != False and did_textbooks != False:
         return True



def most_fun_activity_minute():
    global cur_hedons, did_running, did_textbooks, offered_activity, checker_run, checker_text, checker_rest
#     if offered_activity == "running":
#         did_running = False
#         did_textbooks = False
#     elif offered_activity == "textbooks":
#         did_textbooks = False
#         did_running = False

    if did_running or did_textbooks:
        checker_run = -2
        checker_text = -2
        checker_rest = 0
    else:
        checker_run = 2
        checker_text = 1
        checker_rest = 0

    if checker_run > checker_text > checker_rest:
        return "running"
    elif checker_text > checker_run > checker_rest:
        return "textbooks"
    else:
        return "resting"

if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                       # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())           # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
# #
