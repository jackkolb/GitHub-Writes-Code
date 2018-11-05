# several functions interfacing with a settings file:
# - read_settings: read from the settings file into a dictionary
# - write_settings: write from a dictionary into the settings file (not made yet)

# settings file uses the format:
# - "#" at the start of a line disregards that line (for comments)
# - blank lines are disregarded
# - whitespace around "=" is disregarded
# - variable names should be capitalized, but will be in the settings dictionary

# example settings:
# # EXAMPLE SETTINGS FILE
# 
# SOME_VARIABLE = "GitHub"
# ANOTHER_VARIABLE = True
# YET_ANOTHER_VARIABLE = 1234 

# settings dictionary uses the format:
# - key is a capitalized string ("SOME_VARIABLE")
# - value is also a string ("GitHub", "True", "1234")
#   - use int() or other such functions to convert from strings


# read_settings() reads the settings file and returns the settings dictionary
def read_settings():
    settings = {}
    with open("./settings", "r") as settings_file:
        lines = settings_file.readlines()
        for line in lines:
            if line[0] == "#":  # disregard # (comments)
                continue
            if line == "\n" or line == "":  # disregard blank lines
                continue

            first_equal_sign = line.find("=")  # values may have equal signs!
            variable_name = line[0:first_equal_sign]
            # accounts for spacing to the left of the "=" in the settings file
            #   (but not if the variable is a space for some reason)
            if variable_name[-1] == " " and variable_name != " ":
                variable_name = variable_name[:-1]  # removes the last digit from the string
            variable_name = variable_name.upper()
            
            # accounts for spacing to the right of the "=" in the settings file
            #   (but not if the value is a space for some reason)
            value = line[first_equal_sign+1:]
            # removes the newline character from the value if it exists
            if value[-1] == "\n":
                value = value[:-1]
            if value[0] == " " and value != " ":
                value = value[1:]  # removes the last digit from the string
            value = value
            
            settings[variable_name] = value
    
    return settings

# write_settings() takes a settings dictionary and writes it to the settings file         
def write_settings(settings):
    # not yet implemented
    return
           
