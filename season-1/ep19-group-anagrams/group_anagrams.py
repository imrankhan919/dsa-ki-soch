# Group Anagrams (DSA ki SOCH, Ep 19). LeetCode 49:
# https://leetcode.com/problems/group-anagrams/


# H: sorted letters are the key; anagrams share it. Time O(n * k log k).
def group_anagrams(words):
    groups = {}
    for w in words:
        key = "".join(sorted(w))
        groups.setdefault(key, []).append(w)
    return list(groups.values())


# O: compare every word with every group's first word. Time O(n^2 * k).
def group_anagrams_brute(words):
    groups = []
    for w in words:
        for g in groups:
            if sorted(g[0]) == sorted(w):
                g.append(w)
                break
        else:
            groups.append([w])
    return groups
