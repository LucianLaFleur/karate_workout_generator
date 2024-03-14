import random

# Define the arrays of exercise moves
step_moves = [
    # "step forward", 
    "side-turn", # 90-degree turn
    "V-pattern", # 45-degree v shape in front
    # "step-back",
    "side step",
    # quarter turn is always inwards! meant to be done on the space of a towel or a yoga mat
    "side-step, quarter turn inward",
# legs_intense 
    'squat', 
    'lunge', 
    'side lunge', 
    "half-backstep squat" # three-quarter lunge, like for goblin squat
]

# legs_atk = [
    # "straight knee", 
    # "hooking knee", 
    # "downward stomp",
    # "side stomp"
    # "soccer kick", 
    # "finisher's heel"
# ]

def_moves = [
    "boxer's roll", 
    "standing sway", 
    "shoulder-turning sway", 
    "stepping sway",
    "outward parry", 
    "inward parry",
    "lower sweeping parry",
    "upward sweeping parry"
]

atk_moves = [
    "backhand",
    "chain punch",
    "downward chop",
    "downward elbow",
    "gut punch",
    "hook",
    "jab",
    "side axe handle",
    "upper axe handle",
    "falling axe handle",
    "palm strike",
    "side-chop",
    "uppercut",
    "ear clap",
# legs
    "straight knee", 
    "hooking knee", 
    "downward stomp",
    "side stomp"
    ]

bread_and_butter_moves = [
    # classic one-two punch
    "jab-cross",
    "outward parry, step to palm-strike",
    "body jab to chain punch",
    "body hook, face jab",
    "grasping downward elbow",
    "elbow-jab, side-chop",
    "downward chop, knee strike",
    "inward parry, elbow"
]

# if chosen item is in special combo, ignore all other random gen factors and use it straight
special_combo_moves = [
    "Torso twist side, jabs",
    "backhand, outer parry",
    "jab, stepping cross",
    "elbow, backhand, stepping cross",
    "inner parry, step-forward elbow",
    "stepping uppercut, cross",
    "basic karate punches"
]

back_of_the_mat_starting_position_moves = [
    "backhand, outer parry",
    "jab, stepping cross",
    "elbow, backhand, stepping cross",
    "inner parry, step-forward elbow"
    "elbow-jab, side-chop",
    "stepping uppercut, cross",
    "outward parry, step to palm-strike"
]

full_random_move_list_of_lists = [bread_and_butter_moves, def_moves, atk_moves]
all_individual_moves = []
for sub_arr in full_random_move_list_of_lists:
    for move_name in sub_arr:
        all_individual_moves.append(move_name)

all_basic_moves = []
all_basic_motion_list_of_lists = [def_moves, atk_moves]
for basic_sub_arr in all_basic_motion_list_of_lists:
    for basic_move_name in basic_sub_arr:
        all_basic_moves.append(basic_move_name)

# Function to generate a random exercise combination
def generate_combo_exercise():
    selected_motions = []

    # make an array of 100 items with a number relating to the percentage for each target int
    # - 1, 2, 3 are used to determine if there will be 1, 2, or 3 moves involved in the compound exercise.
    motion_combo_spread = [1] * 20 + [2] * 45 + [3] * 35
    # print(motions_distribution)
    num_of_motions_for_current_exercise = random.choice(motion_combo_spread)

    #                   1 = random step motion, 2 = special arr 3 = no step
    step_chance_spread = [1] * 45 + [2] * 30 + [3] * 25 
    step_flag = random.choice(step_chance_spread)

    # 45% chance add a random step motion to the start of the move-set
    if step_flag == 1:
        print("random step added to motion")
        # Roll for the random step from the arr and put it first
        chosen_step_motion = random.choice(step_moves)
        selected_motions.append(chosen_step_motion)
        # if 2, so 55% chance for just adding 1 random move to the deal
        if num_of_motions_for_current_exercise == 2:
            chosen_second_motion = random.choice(all_individual_moves)
            selected_motions.append(chosen_second_motion)
        # if 2 or 3, so 45% chance for this below
        else:
            chosen_second_motion = random.choice(all_basic_moves)
            selected_motions.append(chosen_second_motion)
            chosen_third_motion = random.choice(all_basic_moves)
            selected_motions.append(chosen_third_motion)
    # special combo moves ignore steps and combinations with other movements 
    elif step_flag == 2:
        print("[+] Special arr rolled!!!")
        chosen_special_move = random.choice(special_combo_moves)
        selected_motions.append(chosen_special_move)
    elif step_flag == 3:
        print("basic, non-stepping move")
        if num_of_motions_for_current_exercise == 1:
            chosen_first_motion = random.choice(all_basic_moves)
            selected_motions.append(chosen_first_motion)
        elif num_of_motions_for_current_exercise == 2:
            chosen_first_motion = random.choice(all_basic_moves)
            selected_motions.append(chosen_first_motion)
            chosen_second_motion = random.choice(all_basic_moves)
            selected_motions.append(chosen_second_motion)
        else: # must be flag 3, so generate 3 motions for the current exercise 
            chosen_first_motion = random.choice(all_basic_moves)
            selected_motions.append(chosen_first_motion)    
            chosen_second_motion = random.choice(all_basic_moves)
            selected_motions.append(chosen_second_motion)
            chosen_third_motion = random.choice(all_basic_moves)
            selected_motions.append(chosen_third_motion)
    else:
        input("unexpected step flag error encountered")
# more than one thing generated, join the moves with a comma, otherwise return the exercise straight, no frills
    if len(selected_motions) > 1:
        output_string_of_motions = ', '.join(selected_motions)
        return output_string_of_motions
    else:    
        return selected_motions[0]
        # output_combo_exercises.append()

def get_array_of_combo_exercises(num):
    total_list_of_exercises_arr = []
    for x in range(num):
        fresh_exercise = generate_combo_exercise()
        print(f"Exercise #{x}: {fresh_exercise}")
        total_list_of_exercises_arr.append(fresh_exercise)
    return total_list_of_exercises_arr

indicated_num = input("State a number of exercises to make:\n\t>> ")
total_list_for_workout = get_array_of_combo_exercises(int(indicated_num))
print(total_list_for_workout)

# setpiece exercise list, then X random moves around it, so like main, secondary workout in X rounds for Y number of sets in a workout

#  rules: intended for area of a towel or yoga mat, rectangle. Intended for limted space.
#  We are NOT fighting, this is about focusing on controlling your muscles and being aware of bodily movement.
#  Check your surroundings before starting; motions are selected to minimize other movement during exercise.
#  recommend using a towel on the floor and being barefoot so you can feel where your intended movement space is.
# ---------------------------
# personally selected cool collection:
#  Start at the back of the mat.
#  Set yourself up at the edge of the mat.
# ...
