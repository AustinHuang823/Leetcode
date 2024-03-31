from copy import copy
from random import random as rand
# Object
obj_hp = 6750000
obj_sp = 6000
obj_def = 420
obj_re = 600

# number of characters
num_char = 2

# Charactor List
char_list = ['da', 'da']
skill_idx = [1, 1]

# Charactor stats
sts = [3374, 2051]
mps = [333, 259]
sks = [2196, 3420]
sps = [1356, 1167]

hps = []

defenses = []
resists = []

dmg_incs = [1.007, 1.051]
# both magic and physical dmg applies

# Charactor UI
weapon_powers = [649, 641]
accuracys = [0.418, 0.4]
criticals = [0.30, 0]
def_ignores = [570, 500]

# equipments_effect
# write key as "trigger" for trigeer event, addon for addon event
# trigger ['trigger' -> str, possibilities -> float]
# addon ['addon' -> str, 'stats name' -> str, possibilites -> float, value multiple with -> float]
special_effs = [[['trigger', 0.4], ['addon', 0.15, 1.0, sts, 2.6], ['trigger', 0.1]],
               []]
eq_dot_chances = [0, 0.55]

# Skill library
# 2D dictionary, to access the element ['character class']['spell index']
# the element formed as: [dmg lines(currnect3), spell_special_buff, if_dot, skill_accuracy, skill_cri, skill_pause]
# classes:
# da: dragon hunter
skill_lib = {'da':{1:[2.6, sts, 1, weapon_powers, 0, 0, 3, True, 0.45, 0.06, 1.3]}}

skill_dot_lib = {'da':{1:[0.25, sks, 1, 1, 0.75, 8]}}

# initializing characters stats
overall_accs = []
overall_cris = []
t_first_hits = []
t_each_hits = []
dot_chances = []
for i in range(len(char_list)):
    overall_acc_ = skill_lib[char_list[i]][skill_idx[i]][-3] + (sks[i] / obj_sp * 0.3) + accuracys[i]
    if overall_acc_ > 1:
        overall_acc_ = 1
    overall_accs.append(overall_acc_)

    overall_cri_ = sks[i] * 0.05 * 0.01 + skill_lib[char_list[i]][skill_idx[i]][-2] + criticals[i]
    if overall_cri_ > 1:
        overall_cri_ = 1
    overall_cris.append(overall_cri_)

    st_over_sp_ = sts[i] / (sps[i] + 1)
    first_hit_ = st_over_sp_ + 1.5
    t_first_hits.append(first_hit_)
    t_each_hit_ = st_over_sp_ + 1.5 + skill_lib[char_list[i]][skill_idx[i]][-1]
    t_each_hits.append(t_each_hit_)

    if_dot = skill_lib[char_list[i]][skill_idx[i]][-4]
    dot_chance_ = eq_dot_chances[i] + skill_dot_lib[char_list[i]][skill_idx[i]][-2] - obj_re / 1000
    if dot_chance_ > 1:
        dot_chance_ = 1
    dot_chances.append(dot_chance_)

# print(overall_accs)
# print(overall_cris)
# print(t_first_hits)
# print(t_each_hits)
# print(dot_chances)


# calculation:
match_len = 300
iter = 1000
direct_damages = []
dot_damages = []
total_damages = []
win, loss = 0, 0

for it in range(iter):
    direct_dmg = 0
    dot_timeline = [] # format as [[dot_occur_time, dmg_per_sec, time_last],[...]]
    buffs = {'st': 0, 'mp': 0, 'sk': 0, 'sp': 0}


    t_next_moves = copy(t_first_hits)
    t = float('inf')
    for i, t_next_move in enumerate(t_next_moves):
        if t_next_move <= t:
            act_char_idx = i
            t = t_next_move

    while t < match_len:
    # if t < match_len:
        for i, t_next_move in enumerate(t_next_moves):
            if t_next_move <= t:
                act_char_idx = i
        
        if_hit = False
        if rand() < overall_accs[act_char_idx]:
            if_hit = True
        
        # buff lines

        # dmg lines
        if if_hit:
            skill_stats = skill_lib[char_list[act_char_idx]][skill_idx[act_char_idx]]
            this_dmg = 0
            for i in range(0, (len(skill_stats)-5)//2, 2):
                if skill_stats[i]:
                    this_dmg += skill_stats[i] * skill_stats[i+1][act_char_idx]
                    # print(this_dmg)
            this_dmg *= dmg_incs[act_char_idx]
            # print(this_dmg) # use this line to check with app numbers
            if rand() < overall_cris[act_char_idx]:
                this_dmg *= 1.5
            # print(this_dmg)

            spell_special_buff = skill_stats[-5]
            this_dmg *= spell_special_buff
            # print(this_dmg)

        t_next_moves[act_char_idx] = t + t_each_hits[act_char_idx]

        # effect lines
        special_eff = special_effs[act_char_idx]
        for eff in special_eff:
            if eff[0] == 'trigger':
                if rand() < eff[1]:
                    t_next_moves[act_char_idx] = t + 0.5
                    # print('char:', act_char_idx, ' triggered!!')
                    break
            if eff[0] == 'addon':
                if rand() < eff[1]:
                    this_dmg += (eff[2] * eff[3][act_char_idx] * eff[4] * spell_special_buff)
                    # print('char:', act_char_idx, ' addon!')
                    break


        # dot lines
        if if_hit and if_dot:
            dot_chance = dot_chances[act_char_idx]
            if rand() < dot_chance:
                m1, stats1, m2, stat2, _, t_last = skill_dot_lib[char_list[act_char_idx]][skill_idx[act_char_idx]]
                dmg_per_sec = m1*stats1[act_char_idx] + m2 * stat2
                dot_timeline.append(([t, int(dmg_per_sec), t_last]))
                # print(dot_timeline)
        # print(f"{t:.1f}",' char:', act_char_idx,' dmg:',int(this_dmg))
        direct_dmg += int(this_dmg)

        # configuration for next move
        t = float('inf')
        for i, t_next_move in enumerate(t_next_moves):
            if t_next_move <= t:
                act_char_idx = i
                t = t_next_move
    
    # direct damges
    direct_damages.append(direct_dmg)

    # dot simulation
    t = 0
    dot_dmg = 0
    dot_timeline.append(([match_len]))
    for i in range(len(dot_timeline)-1):
        t, dmg_per_sec, time_last = dot_timeline[i]
        next_t = dot_timeline[i+1][0]
        stop_t = min(next_t, t + time_last)
        t += 1
        while t <= stop_t:
            dot_dmg += int(dmg_per_sec)
            t += 1
    dot_damages.append(dot_dmg)

    total_dmg = direct_dmg + dot_dmg
    total_damages.append(total_dmg)

    if total_dmg >= obj_hp:
        win += 1
    else:
        loss += 1


# print(total_damages)

print('Average damage: ', sum(total_damages)/ iter)
print('Wins: ', win, ' Losses: ', loss)
print('Win percentage: ', f"{(win/iter * 100):.2f}%")


# didn't calculate resist