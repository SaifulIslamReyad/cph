def job_sequencing(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)  # x[2] is profit

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * (max_deadline + 1)  # 0 index is unused

    total_profit = 0
    job_sequence = []

    # Try to place each job in latest available slot
    for job_id, deadline, profit in jobs:
        for t in range(deadline, 0, -1):
            if slots[t] == -1:
                slots[t] = job_id
                job_sequence.append(job_id)
                total_profit += profit
                break

    return job_sequence, total_profit
#  (Job ID, Deadline, Profit)
def reyad(jobs):
    sequence=[]; profit= 0
    mD = max(job[1] for job in jobs)
    slot= [-1]*(mD+1)
    for id,d,p in jobs:
        for i in range(d,0,-1):
            if slot[i] == -1 : slot[i]=1; profit+=p ; sequence.append(id) ; break
    return sequence, profit

jobs = [
    ('A', 2, 100),
    ('B', 1, 19),
    ('C', 2, 27),
    ('D', 1, 25),
    ('E', 3, 15)
]

sequence, profit = job_sequencing(jobs)
print("Job sequence:", sequence)
print("Total profit:", profit)
sequence2, profit2 = reyad(jobs)
print("Job sequence:", sequence2)
print("Total profit:", profit2)