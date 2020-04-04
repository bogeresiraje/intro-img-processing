
'''
    This module defines elementwise addition of two or more matrices.
'''
import numpy as np


def elementwise_addition(*args):
    '''
        This function returns elementwise addition of two or more matrices.
        Currently, this function only accepts a maximum of ten matrices.
    '''

    # If not  two or more matrices are  passed, raise exception
    if len(args) < 2:
        raise Exception('Two or more arguments are required.')

    # Check the shape of input arguments, if one mismatches from the rest,
    # Raise an exception
    # This statement runs in O(n): Improvement recommended
    # Perceived shape
    perc_shape = None
    for matrix in args:
        if perc_shape is None:
            perc_shape = matrix.shape
        
        else:
            if matrix.shape != perc_shape:
                raise Exception('Passed arrays do not have similar shapes')

    # Perform elementwise addition
    ans = np.zeros(perc_shape)
    for arg in args:
        ans + arg

    return ans