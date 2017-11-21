#
# parse a csv file into a list of list
#
from typing import List, TextIO

def parse_csv(fin: TextIO) -> List[List[str]]:
    """ parse csv file
    """
    values = []
    for l in fin.readlines():
        values.append([data.strip() for data in l.split(',')])

    return values


if __name__ == '__main__':
    import io
    # an IO mock
    with io.StringIO('a,1, 2\nb, 3,  4') as fin_mock:
        values = parse_csv(fin_mock)
        
    print(values)