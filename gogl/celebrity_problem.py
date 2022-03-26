"""
In a party of N people, only one person is known to everyone.
Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party.
We can only ask questions like “does A know B? “. Find the stranger (celebrity) in the minimum number of questions.
We can describe the problem input as an array of numbers/characters representing persons in the party.
We also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B, false otherwise.
How can we solve the problem.
Examples

Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 0, 0, 0},
           {0, 0, 1, 0} }
Output:id = 2
Explanation: The person with ID 2 does not
know anyone but everyone knows him

Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 1, 0, 0},
           {0, 0, 1, 0} }
Output: No celebrity
Explanation: There is no celebrity.
"""


def find_celebrity(persons):
    members = dict()
    potential_celebrity = -1
    i = 0
    for acquaintance in persons:
        acquaintance_set = set()
        j = 0
        for acquaintance_id in acquaintance:
            if acquaintance_id == 1:
                acquaintance_set.add(j)
            j += 1
        if len(acquaintance_set) == 0:
            potential_celebrity = i
        else:
            members[i] = acquaintance_set
        i += 1

    if potential_celebrity == -1:
        return "No celebrity present in party."
    else:
        for acquaintance_set in members.values():
            if potential_celebrity not in acquaintance_set:
                return "No celebrity present in party."

    return potential_celebrity


def find_celebrity_v2(persons):
    n = len(persons)
    i = 0
    j = n-1
    while i < j:
        if persons[j][i] == 1:
            j -= 1
        else:
            i += 1
    candidate = i
    for k in range(n):
        if candidate != k:
            if persons[candidate][k] == 1 or persons[k][candidate] == 0:
                return "Celebrity not present in party."

    return candidate


if __name__ == "__main__":
    persons1 = [[0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 1, 0]]
    persons2 = [[0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0]]
    persons3 = [[0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 1, 0]]

    print("Celebrity Id is: ", find_celebrity(persons1))
    print("Celebrity Id is: ", find_celebrity(persons2))
    print("Celebrity Id is: ", find_celebrity(persons3))

    print("Celebrity Id is: ", find_celebrity_v2(persons1))
    print("Celebrity Id is: ", find_celebrity_v2(persons2))
    print("Celebrity Id is: ", find_celebrity_v2(persons3))
