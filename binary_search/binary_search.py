def binary_search(arr, target):
    # Set boundaries for low and high marks to search
    lo = 0
    hi = len(arr)
    # while low and high do not overlap..
    while lo < hi:
        # check the midpoint
        mid = (lo + hi) // 2
        # If it's equal, return True
        if arr[mid] == target:
            return True
        # Else, if target is smaller
        elif target < arr[mid]:
            # set the high to midpoint value
            hi = mid - 1
        # Else if target is bigger
        else:
            # set the low to midpoint value
            lo = mid + 1
        # if we get to the end return false
        return False
