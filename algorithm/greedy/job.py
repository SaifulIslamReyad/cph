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

# **Algorithm** JobSequencing(jobs)

# // Schedules jobs to maximize profit while meeting deadlines
# // Returns:
# //   - job_sequence: List of scheduled job IDs
# //   - total_profit: Total profit of scheduled jobs

# {
#     // Sort jobs by profit in descending order
#     Sort jobs by job[2] (profit) in non-increasing order;

#     // Find maximum deadline to initialize slots
#     max_deadline := max(job[1] for job in jobs);
#     slots := array of size (max_deadline + 1) initialized to -1;  // slots[0] unused
#     total_profit := 0;
#     job_sequence := empty list;

#     // Place each job in the latest available slot ≤ its deadline
#     for each (job_id, deadline, profit) in jobs do:
#         for t from deadline down to 1 do:
#             if slots[t] = -1 then:
#                 slots[t] := job_id;
#                 Append job_id to job_sequence;
#                 total_profit := total_profit + profit;
#                 break;  // Move to next job

#     return (job_sequence, total_profit);
# }