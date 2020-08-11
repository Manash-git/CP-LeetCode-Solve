# citations = [3,0,6,1,5]

def hIndex(citations):
        citations.sort(reverse=True)
        for i,value in enumerate(citations):
            if i>=value:
                return i
        return len(citations)

print(hIndex([3,0,6,1,5]))
print(hIndex([]))
print(hIndex([0]))
print(hIndex([1]))