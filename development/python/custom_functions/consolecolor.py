
# The original function name was console color, but I changed it to 'p' for quicker coding.

def p(text,type="step",tabs = 0):  
    
    # declared color variables
    tab = "    " # 4 spaces
    step = "\033[1m[+]\033[22m "  # Default - Use for showing action, like starting a service
    backstep = "\033[1m[-]\033[22m " # Used for showing negative action, live stopping a service
    success = "\033[32;1m[\u0394]\033[22m " # Used to show something was successful
    error = "\033[31;1m[!]\033[22m " # Used for error messages
    reset = "\033[0m" # This is required to reset the terminal colors after a custom message is printed
    flag = "\33[34;1m[\\O/]"  # Use for flags or major objectives

    text = str(text)

    if type == "success":
        text = success+text
    if type == "error":
        text = error+text
    if type == "step":
        text = step+text
    if type == "back_step":
        text = backstep+text
    if type == "flag":
        text = flag+text
    else:
        text = text
    if not tabs == 0:
        text = (tab*tabs) + text
    
    print(text+reset)
    return
