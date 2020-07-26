def is_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    # O(N log N)
    str1 = sorted(str1)
    str2 = sorted(str2)

    # O(N)
    for i in range(len(str2)):
        if str1[i] != str2[i]:
            return False
    return True
    # overall running time = O(N log N) + O(N) = O(N log N)
str1 = 'restfuz'
str2 = 'fluster'
print(is_anagram(str1, str2))