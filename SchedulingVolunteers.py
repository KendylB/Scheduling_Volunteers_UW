import pulp as pl
import collections as cl
import itertools


def findDigits(s):
    timer = 0
    while not s.isdigit():
        s = s[1:]
        timer += 1
        if timer > 100:
            print("There is an error with the availabilities data")
            exit()
    return int(s)


def findDay(s):
    timer = 0
    while not s.isalpha():
        s = s[:len(s)-1]
        timer += 1
        if timer > 100:
            print("There is an error with the availabilities data")
            exit()
    return s


def find_poss_shifts_today(all_week, day):
    today = []
    for p in all_week:
        if findDay(p) == day:
            today.append(findDigits(p))
    return today


def delete_empty_avail(work):
    for nam in work:
        if not work[nam]["availability"]:
            temp = work[nam]
    del temp
    return work


def fixing_availability(avail):
    if all(elem in Food_Bank_Hours for elem in avail):
        return avail
    else:
        new_avail = []
        for elem in avail:
            if elem in Food_Bank_Hours:
                new_avail.append(elem)
        return new_avail


# Data
# Shifts that need volunteers
Food_Bank_Hours = ["M0", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12", "M13", "M14", "M15",
                   "T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12", "T13", "T14", "T15",
                   "T16", "T17",
                   "W0", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10", "W11", "W12", "W13", "W14", "W15",
                   "Th0", "Th1", "Th2", "Th3", "Th10", "Th11", "Th12", "Th13", "Th14", "Th15", "Th16", "Th17"]
# Volunteer availability
workers = {
    "Tauson":{
     "availability":[ "T8", "T9", "Th8", "Th9", "T10", "T11", "Th10", "Th11"],
     "points":2,
     "Hours":2,
    },
    "Harie":{
     "availability":[ "M14", "M15", "T14", "T15", "W14", "W15", "Th14", "Th15", "F14", "F15"],
     "points":2,
     "Hours":1,
    },
    "Addie":{
     "availability":[ "M0", "M1", "W0", "W1", "M2", "M3", "W2", "W3", "T4", "T5", "Th4", "Th5", "T6", "T7", "Th6", "Th7", "T8", "T9", "Th8", "Th9", "T10", "T11", "Th10", "Th11"],
     "points":2,
     "Hours":3
    },
    "Anna":{
     "availability":[ "M0", "M1", "W0", "W1", "M2", "M3", "W2", "W3"],
     "points":2,
     "Hours":2
    },
    "Camila":{
     "availability":[ "M4", "M5", "W4", "W5", "M6", "M7", "W6", "W7", "M8", "M9", "W8", "W9", "M10", "M11", "W10", "W11", "M12", "M13", "W12", "W13"],
     "points":2,
     "Hours":4
    },
    "Bella":{
     "availability":[ "M0", "M1", "T6", "T7", "T8", "T9", "T10", "T11", "M12", "M13", "F12", "F13"],
     "points":2,
     "Hours":2
    },
    "Lizzy":{
     "availability":[ "T4", "T5", "M6", "M7", "T6", "T7", "F6", "F7", "M8", "M9", "T8", "T9", "F8", "F9", "M10", "M11", "T10", "T11", "F10", "F11", "T12", "T13"],
     "points":2,
     "Hours":2
    },
    "Rakka":{
     "availability":[ "T12", "T13", "F12", "F13", "T14", "T15", "F14", "F15"],
     "points":2,
     "Hours":1,
    },
    "Sophie":{
     "availability":[ "Th4", "Th5", "M6", "M7", "W6", "W7", "Th6", "Th7", "F6", "F7", "Th8", "Th9", "F8", "F9", "F10", "F11"],
     "points":2,
     "Hours":2,
    },
    "Kaylee":{
     "availability":[ "M0", "M1", "M2", "M3", "W2", "W3", "Th2", "Th3", "M4", "M5", "W4", "W5", "Th4", "Th5", "W6", "W7", "Th6", "Th7", "F6", "F7", "W8", "W9", "Th8", "Th9", "F8", "F9", "T10", "T11", "Th10", "Th11", "F10", "F11", "T12", "T13", "Th12", "Th13", "F12", "F13", "T14", "T15", "Th14", "Th15", "F14", "F15"],
     "points":1,
     "Hours":1,
    },
    "Micheal":{
     "availability":[ "Th2", "Th3"],
     "points":2,
     "Hours":1,
    },
    "Zinny":{
     "availability":[ "M14", "M15", "T14", "T15", "W14", "W15"],
     "points":2,
     "Hours":1,
    },
    "Sally":{
     "availability":[ "Th4", "Th5", "M6", "M7", "T6", "T7", "Th6", "Th7", "M8", "M9", "T8", "T9", "Th8", "Th9", "M10", "M11", "T10", "T11", "W10", "W11", "M12", "M13", "T12", "T13", "W12", "W13", "M14", "M15", "T14", "T15", "W14", "W15"],
     "points":2,
     "Hours":2,
    },
    "Tansy":{
     "availability":[ "T4", "T5", "M6", "M7", "T6", "T7", "W6", "W7", "M8", "M9", "W8", "W9", "M10", "M11", "W10", "W11"],
     "points":2,
     "Hours":2,
    },
    "Carson":{
     "availability":[ "Th8", "Th9", "Th10", "Th11", "M12", "M13", "W12", "W13", "Th12", "Th13", "F12", "F13", "M14", "M15", "W14", "W15", "Th14", "Th15", "F14", "F15"],
     "points":2,
     "Hours":2,
    },
    "Kelly":{
     "availability":[ "T8", "T9", "M10", "M11", "T10", "T11", "Th10", "Th11", "M12", "M13", "Th12", "Th13", "M14", "M15", "Th14", "Th15"],
     "points":2,
     "Hours":2,
    },
    "Taylor":{
     "availability":[ "M10", "M11", "T10", "T11", "Th10", "Th11", "M12", "M13", "Th12", "Th13", "M14", "M15", "Th14", "Th15"],
     "points":2,
     "Hours":2
    },
    "Baider":{
     "availability":[ "M10", "M11", "Th10", "Th11", "M12", "M13", "T12", "T13", "Th12", "Th13", "M14", "M15", "T14", "T15", "Th14", "Th15"],
     "points":2,
     "Hours":2,
    },
    "Carry":{
     "availability":[ "W6", "W7", "F6", "F7", "Th8", "Th9"],
     "points":1,
     "Hours":3,
    },
    "Jimmy":{
     "availability":[ "F4", "F5", "W6", "W7", "F6", "F7"],
     "points":1,
     "Hours":3,
    },
    "Nate":{
     "availability":[ "M2", "M3", "F2", "F3", "Sa4", "Sa5", "Sa6", "Sa7", "T12", "T13", "T14", "T15"],
     "points":1,
     "Hours":4,
    },
    "Kelsey":{
     "availability":[ "M4", "M5", "W4", "W5", "Th4", "Th5", "M10", "M11", "W10", "W11", "Th10", "Th11", "F10", "F11", "M12", "M13", "W12", "W13", "Th12", "Th13", "F12", "F13", "M14", "M15", "W14", "W15", "Th14", "Th15", "F14", "F15"],
     "points":1,
     "Hours":3,
    },
    "Osvaldo":{
     "availability":[ "Th8", "Th9", "F8", "F9", "Th10", "Th11", "F10", "F11"],
     "points":1,
     "Hours":4,
    },
    "Brad":{
     "availability":[ "F0", "F1", "F2", "F3", "M10", "M11", "M12", "M13", "W12", "W13", "M14", "M15", "W14", "W15"],
     "points":2,
     "Hours":4,
    },
    "Addy":{
     "availability":[ "T10", "T11", "W10", "W11", "Th10", "Th11", "W12", "W13", "Th12", "Th13", "M14", "M15", "T14", "T15", "Th14", "Th15", "M16", "M17", "T16", "T17", "Th16", "Th17"],
     "points":1,
     "Hours":1,
    },
    "Ashley":{
     "availability":[ "M4", "M5", "W4", "W5", "M6", "M7", "W6", "W7", "M8", "M9", "W8", "W9"],
     "points":2,
     "Hours":3,
    },
    "Hoffman":{
     "availability":[ "W4", "W5", "W6", "W7"],
     "points":2,
     "Hours":2,
    },
    "Ben":{
     "availability":[ "T0", "T1", "Th0", "Th1", "F0", "F1", "T2", "T3", "Th2", "Th3", "F2", "F3", "T4", "T5", "Th4", "Th5", "T6", "T7", "Th6", "Th7"],
     "points":2,
     "Hours":2,
    },
    "Grace":{
     "availability":[ "M0", "M1", "F0", "F1", "M2", "M3", "F2", "F3", "M4", "M5", "F4", "F5", "W6", "W7", "F6", "F7", "T8", "T9", "Th8", "Th9", "F8", "F9", "T10", "T11", "Th10", "Th11", "F10", "F11", "T12", "T13", "Th12", "Th13", "F12", "F13", "T14", "T15", "Th14", "Th15", "F14", "F15"],
     "points":2,
     "Hours":4,
    },
    "Prim":{
     "availability":[ "M0", "M1", "T0", "T1", "W0", "W1", "Th0", "Th1", "T2", "T3", "Th2", "Th3", "T10", "T11", "Th10", "Th11", "M12", "M13", "W12", "W13"],
     "points":1,
     "Hours":1,
    },
    "Gabe":{
     "availability":[ "Sa0", "Sa1", "F4", "F5", "M6", "M7", "T6", "T7", "W6", "W7", "Th6", "Th7"],
     "points":1,
     "Hours":1,
    },
    "Kitty":{
     "availability":[ "M0", "M1", "W0", "W1", "M2", "M3", "W2", "W3"],
     "points":2,
     "Hours":3,
    },
    "Pullman":{
     "availability":[ "M0", "M1", "W0", "W1", "M2", "M3", "W2", "W3"],
     "points":2,
     "Hours":3,
    },
    "Ron":{
     "availability":[ "T2", "T3", "Th2", "Th3", "T4", "T5", "Th4", "Th5"],
     "points":2,
     "Hours":2,
    },
    "Liz":{
     "availability":[ "T6", "T7", "Th6", "Th7", "T8", "T9", "W8", "W9", "Th8", "Th9", "M10", "M11", "W10", "W11", "M12", "M13"],
     "points":2,
     "Hours":2,
    },
    "Cameron":{
     "availability":[ "M0", "M1", "T0", "T1", "W0", "W1", "F0", "F1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "Th10", "Th11", "M12", "M13", "T12", "T13", "W12", "W13", "Th12", "Th13", "T14", "T15", "W14", "W15", "Th14", "Th15", "T16", "T17", "W16", "W17", "Th16", "Th17"],
     "points":2,
     "Hours":1,
    },
    "Sam":{
     "availability":[ "M2", "M3"],
     "points":2,
     "Hours":1,
    },
    "Kate":{
     "availability":[ "T0", "T1", "Th0", "Th1", "T2", "T3", "Th2", "Th3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12", "T13", "T14", "T15", "T16", "T17"],
     "points":2,
     "Hours":2,
    },
    "Cleve":{
     "availability":[ "T2", "T3", "Th2", "Th3", "M4", "M5", "F4", "F5", "M6", "M7", "F6", "F7"],
     "points":2,
     "Hours":1,
    },
    "Sophy":{
     "availability":[ "F8", "F9", "F10", "F11"],
     "points":1,
     "Hours":2,
    },
    "Smith":{
     "availability":[ "T0", "T1", "Th0", "Th1", "F0", "F1", "T2", "T3", "Th2", "Th3", "F2", "F3", "F4", "F5", "F6", "F7", "M12", "M13", "T12", "T13", "M14", "M15", "T14", "T15", "M16", "M17", "T16", "T17"],
     "points":2,
     "Hours":2,
    },
    "Bub":{
     "availability":[ "M12", "M13", "T12", "T13", "W12", "W13", "Th12", "Th13", "M14", "M15", "T14", "T15", "W14", "W15", "Th14", "Th15", "M16", "M17", "W16", "W17"],
     "points":2,
     "Hours":2,
    },
    "Leroy":{
     "availability":[ "Th0", "Th1", "F0", "F1", "F2", "F3", "F4", "F5", "M10", "M11", "W10", "W11", "Th10", "Th11", "M12", "M13", "W12", "W13", "Th12", "Th13", "W14", "W15"],
     "points":2,
     "Hours":2,
    },
    "Jackson":{
     "availability":[ "W4", "W5"],
     "points":2,
     "Hours":1,
    },
    "Billy":{
     "availability":[ "W4", "W5", "W6", "W7"],
     "points":2,
     "Hours":2,
    },
    "Reynolds":{
     "availability":[ "T8", "T9", "T10", "T11", "T12", "T13"],
     "points":2,
     "Hours":2,
    },
    "Kat":{
     "availability":[ "Sa0", "Sa1", "Sa2", "Sa3", "Sa4", "Sa5", "Sa6", "Sa7", "T14", "T15", "Th14", "Th15", "T16", "T17", "Th16", "Th17", "F16", "F17"],
     "points":2,
     "Hours":2,
    },
    "Mike":{
     "availability":[ "M4", "M5", "M6", "M7"],
     "points":2,
     "Hours":2,
    },
    "Pam":{
     "availability":[ "M4", "M5", "M6", "M7"],
     "points":1,
     "Hours":2,
    },
    "Kimmy":{
     "availability":[ "F0", "F1", "T4", "T5", "T6", "T7", "M8", "M9", "T8", "T9", "W8", "W9", "T10", "T11", "T12", "T13", "M14", "M15"],
     "points":1,
     "Hours":2,
    },
    "Shek":{
     "availability":[ "W8", "W9", "W10", "W11", "W12", "W13", "W14", "W15", "W16", "W17"],
     "points":2,
     "Hours":4,
    },
    "Emm":{
     "availability":[ "M12", "M13", "M14", "M15", "T14", "T15"],
     "points":2,
     "Hours":2,
    },
    "Frank":{
     "availability":[ "Sa0", "Sa1", "Sa2", "Sa3", "Sa4", "Sa5", "M6", "M7", "T6", "T7", "W6", "W7", "Th6", "Th7", "M8", "M9", "T8", "T9", "W8", "W9", "Th8", "Th9", "M10", "M11", "T10", "T11", "W10", "W11", "Th10", "Th11", "M12", "M13"],
     "points":2,
     "Hours":2,
    },
    "Rishika":{
     "availability":[ "Th4", "Th5", "Th6", "Th7", "M8", "M9", "W8", "W9", "Th8", "Th9", "M10", "M11", "W10", "W11", "Th10", "Th11", "M12", "M13", "W12", "W13", "Th12", "Th13"],
     "points":2,
     "Hours":2,
    },
    "Beatrix":{
     "availability":[ "M6", "M7", "T6", "T7", "W6", "W7", "Th6", "Th7", "F6", "F7", "M8", "M9", "W8", "W9", "F8", "F9"],
     "points":2,
     "Hours":1,
    },
    "Sunny":{
     "availability":[ "Sa0", "Sa1", "Sa2", "Sa3", "Sa4", "Sa5", "M6", "M7", "T6", "T7", "W6", "W7", "Th6", "Th7", "M8", "M9", "T8", "T9", "W8", "W9", "Th8", "Th9", "T10", "T11", "Th10", "Th11", "T12", "T13", "Th12", "Th13", "T14", "T15", "Th14", "Th15", "F14", "F15", "F16", "F17"],
     "points":2,
     "Hours":2,
    },
    "Gracey":{
     "availability":[ "Sa2", "Sa3", "Sa4", "Sa5", "F6", "F7", "Sa6", "Sa7", "M8", "M9", "W8", "W9", "F8", "F9", "Sa8", "Sa9", "M10", "M11", "W10", "W11", "F10", "F11", "Sa10", "Sa11", "M12", "M13", "W12", "W13", "F12", "F13", "Sa12", "Sa13", "M14", "M15", "W14", "W15", "F14", "F15", "Sa14", "Sa15"],
     "points":2,
     "Hours":2,
    },
    "Ronald":{
     "availability":[ "M12", "M13", "W12", "W13", "M14", "M15", "W14", "W15", "W16", "W17"],
     "points":2,
     "Hours":2,
    },
    "Catherine":{
     "availability":[ "T2", "T3", "T4", "T5"],
     "points":2,
     "Hours":2,
    },
    "Eddy":{
    "availability":[ "M11", "M12"],
    "points":2,
    "Hours":1,
    },
    "Jax":{
    "availability":[ "M13", "M14", "M15", "M16", "M17"],
    "points":2,
    "Hours":2,
    },
    "Ash":{
    "availability":[ "M0", "M1"],
    "points":2,
    "Hours":1,
    },
    "Bran":{
    "availability":[ "M2", "M3", "M4", "M5"],
    "points":2,
    "Hours":2,
    },
    "Jazzy":{
    "availability":[ "M0", "M1"],
    "points":2,
    "Hours":1,
    },
    "Francis":{
    "availability":[ "M8", "M9"],
    "points":2,
    "Hours":1,
    },
    "Alison":{
    "availability":[ "M16", "M17"],
    "points":2,
    "Hours":1,
    },
    "Kelsey":{
    "availability":[ "M16", "M17"],
    "points":2,
    "Hours":1,
    },
    "Lee":{
    "availability":[ "M0", "M1"],
    "points":2,
    "Hours":1,
    },
    "Carley":{
    "availability":[ "M8", "M9"],
    "points":2,
    "Hours":1,
    },
    "Emma":{
    "availability":[ "M0", "M1"],
    "points":2,
    "Hours":1,
    },
    "Kayla":{
    "availability":[ "T2", "T3", "T4", "T5"],
    "points":2,
    "Hours":2,
    },
    "Jenny":{
    "availability":[ "T6", "T7"],
    "points":2,
    "Hours":1,
    },
    "Lemmy":{
    "availability":[ "T4", "T5"],
    "points":2,
    "Hours":1,
    },
    "Laruen":{
    "availability":[ "T10", "T11"],
    "points":2,
    "Hours":1,
    },
    "Jaz":{
    "availability":[ "T12", "T13"],
    "points":2,
    "Hours":1,
    },
    "Kim":{
    "availability":[ "T18", "T19"],
    "points":2,
    "Hours":1,
    },
    "Xander":{
    "availability":[ "T10", "T11", "T12", "T13", "T14", "T15"],
    "points":2,
    "Hours":3,
    },
    "Hope":{
    "availability":[ "W10", "W11"],
    "points":2,
    "Hours":1,
    },
    "Ammy": {
        "availability": ["W14", "W15", "W13", "W12"],
        "points": 2,
        "Hours": 2,
    },
    "Kendall": {
        "availability": ["W0", "W1"],
        "points": 2,
        "Hours": 1,
    },
    "Anon": {
        "availability": ["W6", "W7"],
        "points": 2,
        "Hours": 1,
    },
    "Benjamin": {
        "availability": ["W14", "W12", "W15", "W13"],
        "points": 2,
        "Hours": 2,
    },
    "Nilly": {
        "availability": ["Th2", "Th3"],
        "points": 2,
        "Hours": 1,
    },
    "Cassy": {
        "availability": ["Th10", "Th13", "Th11", "Th12"],
        "points": 2,
        "Hours": 2,
    },
    "Harry": {
        "availability": ["Th16", "Th17"],
        "points": 2,
        "Hours": 1,
    },
    "Polly": {
        "availability": ["Th0", "Th1", "Th2", "Th3"],
        "points": 2,
        "Hours": 2,
    },
    "Bob": {
        "availability": ["Th10", "Th11"],
        "points": 2,
        "Hours": 1,
    },
    "Denny": {
        "availability": ["Th14", "Th15", "Th16"],
        "points": 2,
        "Hours": 1.5,
    },
    "Wyatt": {
        "availability": ["Th0", "Th3", "Th1", "Th2"],
        "points": 2,
        "Hours": 2,
    },
    "Manny": {
        "availability": ["Th10", "Th13", "Th11", "Th12"],
        "points": 2,
        "Hours": 2,
    },
    "Christan": {
        "availability": ["Th16", "Th17"],
        "points": 2,
        "Hours": 1,
    },
    "Sarah": {
        "availability": ["Th10", "Th11", "Th12", "Th13", "Th14", "Th15"],
        "points": 2,
        "Hours": 3,
    },
    "Bobby": {
        "availability": ["Th16", "Th17"],
        "points": 2,
        "Hours": 1,
    },
    "Amber": {
        "availability": ["M0", "M1"],
        "points": 2,
        "Hours": 1,
    }
}
# Cleaning the Data
for name in workers:
    volunteer = workers[name]
    volunteer["availability"] = fixing_availability(volunteer["availability"])

workers = delete_empty_avail(workers)

# Friend Pairs
Friend_list = [ ["Addie","Beatrix"], ["Bella","Hoffman"],
                ["Kaylee","Hope"], ["Kaylee"," Rishika "],
                ["Kelly","Taylor"], ["Kelly"," Baider"],
                ["Taylor","Kelly"], ["Baider","Kelly"],
                ["Addy","Grace"], ["Kitty","Pullman"],
                ["Pullman ","Kitty "], ["Kate","Cleve"],
                ["Kate"," "], ["Cleve","Kate "],
                ["Sophy","Osvaldo"], ["Jackson","Billy"],
                ["Billy","Jackson"], ["Mike","Pam"],
                ["Pam","Mike"], ["Emm","Jax"],
                ["Hope","Rishika"], ["Hope"," Kaylee"],
                ["Rishika","Hope"], ["Rishika"," Kaylee"]]

# define the model: we want to maximize friendship points and shifts with 4 volunteers
prob = pl.LpProblem("scheduling", pl.LpMaximize)
# some model variables
points = []
vars_by_shift = cl.defaultdict(list)
vars_by_hours = []
vars_by_worker = cl.defaultdict(list)
worker_shifts = []
returning = []
# Setting up variables and dictionaries and lists
for worker, info in workers.items():
    # I want the workers name, and the amount of hours they work
    vars_by_hours.append([worker, info["Hours"]])
    worker_shifts.append(([worker, info['availability']]))
    for shift in info['availability']:
        worker_var = pl.LpVariable("%s_%s" % (worker, shift), 0, 1, pl.LpInteger)
        # store some variable data so we can implement the ban constraint
        var_data = (worker,)
        vars_by_shift[shift].append((worker_var, var_data))
        # store vars by variable so we can implement the max shift constraint
        vars_by_worker[worker].append(worker_var)
        points.append(worker_var * info['points'])
        if info['points'] == 2:
            returning.append(worker_var.name)
# Take all [a,b] in Friend_List
# Find out if a,b is new or returning or mixed called H
# Find every shift a and b can both work called i
# Make a new array Friend_Knowledge containing [a,b,i,H]
Friend_Knowledge = []
for i in range(len(Friend_list)):
    a = Friend_list[i][0]
    b = Friend_list[i][1]
    # if a and b do not exist in workers continue
    if (a not in workers) or (b not in workers):
        continue
    a_shifts = workers[a]["availability"]
    b_shifts = workers[b]["availability"]
    # Find the shifts that overlap
    shifts = list(set(a_shifts) & set(b_shifts))
    a_status = workers[a]["points"]
    b_status = workers[b]["points"]
    H = 0
    if a_status == b_status == 1:
        H = 2
    elif a_status == b_status == 2:
        H = 4
    else:
        H = 3
    Friend_Knowledge.append([a, b, shifts, H])
# Make new variables for each element in Friend_Knowledge
friendR_array = []
friendM_array = []
friendN_array = []
for i in range(len(Friend_Knowledge)):
    a = Friend_Knowledge[i][0]
    b = Friend_Knowledge[i][1]
    shifts = Friend_Knowledge[i][2]
    H = Friend_Knowledge[i][3]
    if H == 4:
        for j in range(len(shifts)):
            friendR_var = pl.LpVariable("%s_%s_%s" % (a, b, shifts[j]), 0, 1, pl.LpInteger)
            friendR_array.append(friendR_var)
    elif H == 3:
        for j in range(len(shifts)):
            friendM_var = pl.LpVariable("%s_%s_%s" % (a, b, shifts[j]), 0, 1, pl.LpInteger)
            friendM_array.append(friendM_var)
    else:
        for j in range(len(shifts)):
            friendN_var = pl.LpVariable("%s_%s_%s" % (a, b, shifts[j]), 0, 1, pl.LpInteger)
            friendN_array.append(friendN_var)

# Preference Towards 4 volunteers working
num_working_array = []
for i in range(len(Food_Bank_Hours)):
    num_working_shift = pl.LpVariable("%s_%d" % ("num_working", i), None, None, pl.LpInteger)
    num_working_array.append(num_working_shift)

# Add all friendH_var to objective function
prob += pl.lpSum(4*friendR_array+3*friendM_array+2*friendN_array+5*num_working_array)

# Add constraints for friendH_var
R = 0
N = 0
M = 0
for i in range(len(Friend_Knowledge)):
    # find worker_var corresponding to a_i and b_i
    a = vars_by_worker[Friend_Knowledge[i][0]]
    b = vars_by_worker[Friend_Knowledge[i][1]]
    shifts = Friend_Knowledge[i][2]
    for j in range(len(shifts)):
        r = shifts.index(shifts[j])
        a_i = a[r-1]
        b_i = b[r-1]
        if Friend_Knowledge[i][0] == 4:
            prob += friendR_array[R] >= a_i + b_i - 1
            prob += friendR_array[R] <= a_i
            prob += friendR_array[R] <= b_i
            R += 1
        elif Friend_Knowledge[i][0] == 3:
            prob += friendM_array[M] >= a_i + b_i - 1
            prob += friendR_array[M] <= a_i
            prob += friendR_array[M] <= b_i
            M += 1
        elif Friend_Knowledge[i][0] == 2:
            prob += friendN_array[N] >= a_i + b_i - 1
            prob += friendR_array[N] <= a_i
            prob += friendR_array[N] <= b_i
            N += 1

# # Add constraints for num_working_shift -|sum(of all s) v_js-4|=num_working_s
days = ["M", "T", "W", "Th", "F", "Sa"]
abs_1_array = []
abs_2_array = []
x = 0
for i in Food_Bank_Hours:
    abs_1_array.append(pl.LpVariable("abs_1_%d" % x, 0, None))
    abs_2_array.append(pl.LpVariable("abs_2_%d" % x, 0, None))
    prob += sum([var[0] for var in vars_by_shift[i]]) - 4 <= abs_1_array[x] - abs_2_array[x]
    prob += -1 * (sum([var[0] for var in vars_by_shift[i]]) - 4) <= abs_1_array[x] - abs_2_array[x]
    prob += -1 * abs_1_array[x] + abs_2_array[x] + 1 == num_working_array[x]
    x += 1
# # set the shift requirements, 3 to 5 people per shift
for i in Food_Bank_Hours:
    prob += sum([var[0] for var in vars_by_shift[i]]) <= 5
    prob += sum([var[0] for var in vars_by_shift[i]]) >= 3
# Take a worker : amount_shifts_worker[0]
# look at how many shifts they want to work : amount_shifts_worker[1]
# sum of all shifts they work = how many shifts they want to work
for i in range(len(vars_by_hours)):
    amount_shifts_worker = vars_by_hours[i]
    amount_shifts = amount_shifts_worker[1]
    if vars_by_worker[amount_shifts_worker[0]]:
        prob += sum(vars_by_worker[amount_shifts_worker[0]]) <= 2*amount_shifts # Each shift is a half hour
        #prob += sum(vars_by_worker[amount_shifts_worker[0]]) >= 2*amount_shifts # No idea why this doesn't work
        # Want to cap number of hours worked
        prob += sum(vars_by_worker[amount_shifts_worker[0]]) >= 2

# No split shifts
# Take every worker
for i in workers:
    poss_shifts = workers[i]["availability"]
    # Compare all shifts
    for u, v in itertools.combinations(poss_shifts, 2):
        a = findDigits(u)
        b = findDigits(v)
        num_1 = poss_shifts.index(u)
        num_2 = poss_shifts.index(v)
        John_a = vars_by_worker[i][num_1]
        John_b = vars_by_worker[i][num_2]
        if findDay(u) != findDay(v):
            prob += John_a + John_b <= 1
            continue
        if abs(a-b) == 1:
            continue
        # All shifts that would need to exist for John to work a and b
        if b >= a:
            needed_shifts = list(range(a, b))
        else:
            needed_shifts = list(range(b, a))
        # Find variable corresponding to i_a and i_b
        # If every element in needed_shifts is in poss_shifts then move to else,
        # If not then add constraint that John can't work both a and b
        poss_shifts_per_day = find_poss_shifts_today(poss_shifts, findDay(u))
        if not all(elem in poss_shifts_per_day for elem in needed_shifts):
            # Find elements not in poss_shifts
            prob += John_a + John_b <= 1
        # If John works a and b then John must work c, for all c between a and b
        else:
            for j in needed_shifts:
                num_3 = poss_shifts_per_day.index(j)
                John_c = vars_by_worker[i][num_3]
                prob += John_c >= John_a + John_b - 1


status = prob.solve()
print("Result:", pl.LpStatus[status])
results = []
for shift, varis in vars_by_shift.items():
    results.append({
        "shift": shift,
        "workers": [var[1][0] for var in varis if var[0].varValue == 1],
    })

for result in sorted(results, key=lambda x: x['shift']):
    print("Shift:", result['shift'], 'workers:', ', '.join(result['workers']))

one = []
two = []
for shift in results:
    for workers in shift:
        if isinstance(shift[workers], list):
            for person in shift[workers]:
                if person not in one:
                    one.append(person)
                else:
                    two.append(person)
print(list(set(one).difference(two)))
print(len(list(set(one).difference(two))))



