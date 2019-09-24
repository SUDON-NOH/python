# hash
# collections


A = ['a', 'b', 'c', 'd']
B = ['a', 'b', 'c']



def solution(participant, completion):

    participant.sort()
    completion.sort()

    for i in range(len(participant)) :

        try:

            if participant[i] != completion[i] :

                return participant[i]

        except IndexError:

            return participant[i]

print(solution(A,B))


import collections

a = collections.Counter(A) #
b = collections.Counter(B) #


print("A:", a)
print("B:", b)

answer = a - b

print(answer)

print(list(answer)[0])

