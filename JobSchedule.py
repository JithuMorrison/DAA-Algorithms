def jobschedule(arr):
	n = len(arr)
	arr.sort(key=lambda x:x[2],reverse = True)
	slots = max(a[1] for a in arr)
	slot = [False for i in range(slots)]
	job = []
	for i in range(n):
		deadline = arr[i][1]
		for j in range(deadline-1,-1,-1):
			if slot[j]==False:
				slot[j]=True
				job.append(arr[i][0])
				break
	print(job)

jobs = [
    ['a', 2, 100],
    ['b', 1, 19],
    ['c', 2, 27],
    ['d', 1, 25],
    ['e', 3, 15]
]

for i in jobs:
	print(i)
print("Job Scehduling for the above jobs : ")
jobschedule(jobs)
