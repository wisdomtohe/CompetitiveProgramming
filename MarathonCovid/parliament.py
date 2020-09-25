go = True
while(go):
    values = list(map(int, input().strip().split(" ")))
    if all([v == 0 for v in values]):
        go = False
    else:
        total_num_of_members, p_members, r_members = values
        vote_need_number = (total_num_of_members//2)+1
        person_need_number = max(vote_need_number-p_members,0)
        remaining_members = total_num_of_members-p_members-r_members
        if person_need_number>remaining_members:
            person_need_number = -1
        print(person_need_number)
            