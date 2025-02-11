def calculate_love_score(name1, name2):
    match = (name1 + name2).upper()
    score1= "TRUE"
    score2 = "LOVE"
    true_score = 0
    love_score = 0


    for letter in score1:
        count_true = match.count(letter)
        if count_true == 0 or count_true == 2:
            print(f"{letter} occurs {count_true} times.")
        else:
            print(f"{letter} occurs {count_true} time.")
        true_score += count_true
    for letter in score2:
        count_love = match.count(letter)
        if count_love == 0 or count_love == 2:
            print(f"{letter} occurs {count_love} times.")
        else:
            print(f"{letter} occurs {count_love} time.")
        love_score += count_love

    true_love_score = int(str(true_score)+ str(love_score))
    print()
    print(f"Love Score = {true_love_score}")

    # t_t = 0
    # t_r = 0
    # t_u = 0
    # t_e = 0
    # l_l = 0
    # l_o = 0
    # l_v = 0
    # l_e = 0
    # for letter in match:
    #     if letter == "T":
    #         t_t += 1
    #         #print("t value is:",t_t)
    #     if letter == "R":
    #         t_r += 1
    #         #print("r value is:",t_r)
    #     if letter == "U":
    #         t_u += 1
    #         #print("u value is:", t_u)
    #     if letter == "E":
    #         t_e += 1
    #         #print("e value is:", t_e)
    # for letter in match:
    #     if letter == "L":
    #         l_l += 1
    #         #print("t value is:",t_t)
    #     if letter == "O":
    #         l_o += 1
    #         #print("r value is:",t_r)
    #     if letter == "V":
    #         l_v += 1
    #         #print("u value is:", t_u)
    #     if letter == "E":
    #         l_e += 1
    #         #print("e value is:", t_e)


    #TODO: Make it so that the word time prints times if the count is greater than or equal to 2
    # if t_t >= 2 or t_t == 0:
    #     print(f"T occurs {t_t} times")
    # else:
    #     print(f"T occurs {t_t} time")
    # if t_r >= 2 or t_r == 0:
    #     print(f"R occurs {t_r} times")
    # else:
    #     print(f"R occurs {t_r} time")
    # if t_u >= 2 or t_u == 0:
    #     print(f"U occurs {t_u} times")
    # else:
    #     print(f"U occurs {t_u} time")
    # if t_e >= 2 or t_e == 0:
    #     print(f"E occurs {t_e} times")
    # else:
    #     print(f"E occurs {t_e} time")
    #
    # count_true = t_t+t_r+t_u+t_e
    # print(f"Total = {count_true}")
    # if l_l >= 2 or l_l == 0:
    #     print(f"L occurs {l_l} times")
    # else:
    #     print(f"L occurs {l_l} time")
    # if l_o >= 2 or l_o == 0:
    #     print(f"O occurs {l_o} times")
    # else:
    #     print(f"O occurs {l_o} time")
    # if l_v >= 2 or l_v == 0:
    #     print(f"V occurs {l_v} times")
    # else:
    #     print(f"V occurs {l_v} time")
    # if l_e >= 2 or l_e == 0:
    #     print(f"E occurs {l_e} times")
    # else:
    #     print(f"E occurs {l_e} time")
    # count_love = l_l+l_o+l_v+l_e

    # print(f"Total = {count_love}")


calculate_love_score("Angela Yu", "Jack Bauer")
