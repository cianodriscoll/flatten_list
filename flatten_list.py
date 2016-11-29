import sys

input_pass_1 = [[1, 2, [3]], 4]
input_pass_2 = [[1, 2, [3, 4, [5, 6]]], 7]
input_pass_3 = [[1, 2, [3, 4, [5, 6, [7, 8, 9]]]], 10]
input_err_1 = None
input_err_2 = []
input_err_3 = 5
input_err_4 = [[1, 2, [3, 4, [5, 6, [7, 8, 'X']]]], 9]

inputs_pass = [input_pass_1, input_pass_2, input_pass_3]
inputs_fail = [input_err_1, input_err_2, input_err_3, input_err_4]


def flatten_list(input, output):
    '''
    Takes a input list of list and flattens into one list.
    Uses recursion to achieve this
    '''
    if not isinstance(input, list):
        raise ValueError('Expected list, found %s' % type(input))
    elif not input:
        raise ValueError('List empty, list (%s)' % input)

    for item in input:
        if isinstance(item, list):
            flatten_list(item, output)
        elif isinstance(item, int):
            output.append(item)
        else:
            raise ValueError('Expected int, found %s' % type(item))

    return output


def run_tests():
    '''
    Tests flatten_list function. Runs a list of tests
    that expected to pass and a set expected to fail
    '''
    for input in inputs_pass:
        output = []
        flatten_list(input, output)

    err_count = 0
    for input in inputs_fail:
        output = []
        try:
            flattened = flatten_list(input, output)
        except ValueError:
            err_count += 1

    if err_count != len(inputs_fail):
        print "Did not hit error count, expected (%s) errors got (%s)" \
            % (len(inputs_fail), err_count)
        sys.exit(1)

    print "Pass!!!"

if __name__ == "__main__":
    run_tests()
