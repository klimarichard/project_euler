def find_before_and_after(logins):
    """
    Finds numbers, that come before and after each number
    in the logins.
    :param logins: list of successful logins
    :return: numbers before and after each number
    """
    before = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
    after = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
    logins = list(map(str, sorted(set(logins))))

    for k in range(len(logins)):
        before[int(logins[k][1])] |= {int(logins[k][0])}
        before[int(logins[k][2])] |= {int(logins[k][1])}
        after[int(logins[k][0])] |= {int(logins[k][1])}
        after[int(logins[k][1])] |= {int(logins[k][2])}

    keys = list(before.keys())

    # exclude numbers, that are not in any successful login
    for k in keys:
        if before[k] == set() and after[k] == set():
            before.pop(k)
            after.pop(k)

    return before, after


def construct_possible_passcodes(before, after):
    """
    Construct lists of possible numbers in password with respect
    to before values and after values respectively
    :param before: before values
    :param after: after values
    :return: lists of possible numbers at each positions
    """
    passcode_after = [[]] * len(afters)
    passcode_before = [[]] * len(befores)
    passcode_after[0] = [k for k in afters.keys() if befores[k] == set()]
    passcode_before[0] = passcode_after[0]
    passcode_after[len(befores) - 1] = [k for k in afters.keys() if afters[k] == set()]
    passcode_before[len(befores) - 1] = passcode_after[len(befores) - 1]

    for i in range(1, len(befores) - 1):
        x_i = list(set([k for m in passcode_after[i - 1] for k in afters[m]]))
        y_i = list(set([k for m in passcode_before[len(befores) - i] for k in befores[m]]))
        passcode_after[i] = x_i
        passcode_before[len(befores) - (i + 1)] = y_i

    return passcode_before, passcode_after


logins = []

with open('../../res/p079_keylog.txt', 'r') as f:
    line = f.readline()

    while line:
        logins.append(int(line.strip()))
        line = f.readline()

befores, afters = find_before_and_after(logins)
pass_before, pass_after = construct_possible_passcodes(befores, afters)

passcode = []
for i in range(len(pass_before)):
    pass_i = [str(x) for x in pass_before[i] if x in pass_after[i]]
    passcode += pass_i

print(''.join(passcode))
