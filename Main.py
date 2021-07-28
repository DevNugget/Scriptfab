# Variables
player_scripts = ["Platformer2D", ""] # Put string here to keep in mind of the command at 1.f

# Main menu
def menu(item1, item2):
	print("############");
	print("# >" + item1 + " #");
	print("# >" + item2 + " #");
	print("############");

# Calling menu
menu("scripts", "quit   ");

# Platformer2D script creator
def platformer_2d():
	platformer_script = """
# Script from https://kidscancode.org/godot_recipes/2d/platform_character/ and modified by DevNugget
extends KinematicBody2D

# Variables (can be changed in inspector)
export (int) var speed = 100
export (int) var jump_speed = -240
export (int) var gravity = 10

# Velocity
var velocity = Vector2.ZERO

# Taking input
func get_input():
    velocity.x = 0
    if Input.is_action_pressed("walk_right"): # Add in Input Map
        velocity.x += speed
    if Input.is_action_pressed("walk_left"): # Add in Input Map
        velocity.x -= speed

func _physics_process(delta):
    get_input() # Applying movement input
    velocity.y += gravity * delta # Applying gravity
    velocity = move_and_slide(velocity, Vector2.UP)
    if Input.is_action_just_pressed("jump"):
        if is_on_floor():
            velocity.y = jump_speed
	"""
	script = open("Platformer2DScript.gd", "x");
	script.write(platformer_script);
	print("Script Created");
	script.close();

# 1.e :: 
def script_demo():
	script_content = """
# Delete this comment and copy paste/write the script you want to re-use here
"""
	script = open("file_name.file_extention", "x"); # Put the filename and file extention ex: main.py (don't touch "x")
	script.write(script_content);
	print("Script Created");
	script.close();

# Wanted script for user
def action(option1, option2):
	action = input("What do you want to do? (" + option1 + "/" + option2 + "): ");

	# Displaying available scripts
	if action.lower().strip() == "scripts":
		print(player_scripts);
		action = input("Input a value from the above list of scripts (no need for caps): ");
		if action.lower().strip() == "platformer2d":
			platformer_2d();
		# 1.f :: un-comment the elif statement
		#        then type the name of script in ""

		#elif action.lower().strip() == "":
			#script_demo(); 
	else:
		quit();


# Calling action
action("scripts", "quit");

