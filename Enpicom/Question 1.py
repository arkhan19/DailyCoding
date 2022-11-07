
def read_data(file_name):
    with open(file_name, 'r') as file:
        str1 = file.readline().rstrip()
        str2 = file.readline().rstrip()
    return str1, str2


def minimum_edit_distance(s1, s2):
    # if length of second string is zero, insertions (OPs) of length of s1 will occur.
    if len(s2) == 0:
        return len(s1)
    # Creating the MATRIX of edit distance

    # previous row with length of second string + 1 (from null) to go through entire second string
    # Null + Entire length of first string = Number of OPs to get s1 = s2.
    previous_row = range(len(s2) + 1)

    # Going through entire S2 for each c1 in S1.
    for i, c1 in enumerate(s1):
        # New row of length + 1 to accomodate for Null value.
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            # Matrix row being created to represent Ops to be done to convert each C1 to chars of S2
            insertions = previous_row[j + 1] + 1  # +1 and then same as previous row
            deletions = current_row[j] + 1  # +1 and move on next character
            substitutions = previous_row[j] + (c1 != c2)  # +1 to substitute and same ops as previous row
            current_row.append(min(insertions, deletions, substitutions))  # current row = min of OPs done on S2
            # Row element for c1vc2 created
        previous_row = current_row
    # return last element of last row = total operations done to convert S1 to S2
    return previous_row[-1]


if __name__ == "__main__":
    a, b = read_data('filename.txt')
    best_matching = {}
    for s1 in a:
        for s2 in b:
            # length of first string has to be greater for second -for- loop.
            if len(s1) > len(s2):
                # get edit score for s1 and s2
                score = minimum_edit_distance(s1, s2)
                best_matching[score] = s1 + '+' + s2
        # search dict with best score key
        best_score = min(best_matching, key=best_matching.get)
        # Best S2 for S1.
        print("Best Matching Sequence with score {} : {}".format(best_score, best_matching[best_score]))