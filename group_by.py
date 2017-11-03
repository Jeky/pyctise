#
# Group By is a useful operation. Usually we have a list containing some course and student pairs:
# [('CSC108', 'Jeky'),
#  ('CSC207', 'Tim'),
#  ('CSC108', 'James'),
#  ('CSC108', 'Alex')] 
# We can group them by course:
# {
#   'CSC108' : ['Jeky', 'James', 'Alex'],
#   'CSC207' : ['Tim']
# }
#

from typing import List, Dict

def group_by(lst: List[tuple]) -> Dict[str, list]:
    ### Group items in the list by the first element
    ###
    group = {}
    for key, item in lst:       # elements in tuple will be automatically assigned to these two variables. 
                                # key is the first element in tuple and item is the second one in tuple.
        if key not in group:
            group[key] = []

        group[key].append(item)

    return group


if __name__ == '__main__':
    group = group_by([('CSC108', 'Jeky'), ('CSC207', 'Tim'), ('CSC108', 'James'), ('CSC108', 'Alex')])
    print(group)