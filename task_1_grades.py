def calculate_grade(home, raw_number, type):
    if type == "Pass/fail":
        if raw_number > 49:
            home.alert("Info", "You have passed", 'info')
        else:
            home.alert("Info", "You have failed", 'info')
    else:
        if raw_number >=85:
            home.alert("Info", "High distinction", 'info')
        elif raw_number >=75:
            home.alert("Info", "Distinction", 'info')
        elif raw_number >=65:
            home.alert("Info", "Credit", 'info')
        elif raw_number >=50:
            home.alert("Info", "Pass", 'info')
        else:
            home.alert("Info", "You have failed", 'info')