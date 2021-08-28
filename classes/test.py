obj = [
    {
        "id": '/16',
        "size": 1256
    },
    {
        "id": '/19',
        "size": 256
    },
    {
        "id": '/19',
        "size": 128
    },
    {
        "id": '/16',
        "size": 1156
    },
]

obj.sort(key=lambda x: (x['id'], -x['size']), reverse=True)

print(str(obj))

print(sum([1, 2, 3, 4]))


arr = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(sum([(i in a) - (i in b) for i in arr]))
