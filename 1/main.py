import re
import collections
strs=["eat","tea","tan","ate","nat","bat"]
liststrs=[tuple(sorted(word)) for word in strs]
strdict=collections.defaultdict(list)
for i in range(len(liststrs)):
    strdict[liststrs[i]].append(strs[i])
values_list = list(strdict.values())
print(values_list)









