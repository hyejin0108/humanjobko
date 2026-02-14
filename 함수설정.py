# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 16:28:32 2026

@author: svivs
"""
#%% default, annotation, docstring
def prod_list(iter:list=[2,3,4,5]) -> float:
    # docstring - 함수 설명
    """
    Parameters
    ----------
    iter : list, optional
        this argument is producted. The default is [2,3,4,5].

    Returns
    -------
    float
        result of producting.

    """
    ans = 1
    for i in iter:
        ans *= i
    return ans

