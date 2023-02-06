import random
import json


def cal_win_ammount(winning_drawing, my_drawing, time_won):
    win_amount = 0

    white_matches = len(my_drawing["whites"].intersection(winning_drawing["whites"]))
    power_match = my_drawing["red"] == winning_drawing["red"]

    if white_matches == 5:
        if power_match:
            win_amount = 2_000_000_000
            time_won["5+P"] += 1
        else:
            win_amount = 1_000_000
            time_won["P"] += 1
    elif white_matches == 4:
        if power_match:
            win_amount = 50_000
            time_won["4+P"] += 1
        else:
            win_amount = 100
            time_won["4"] += 1
    elif white_matches == 3:
        if power_match:
            win_amount = 100
            time_won["3+P"] += 1
        else:
            win_amount = 7
            time_won["3"] += 1
    elif white_matches == 2 and power_match:
        win_amount = 7
        time_won["2+P"] += 1
    elif white_matches == 1 and power_match:
        win_amount = 4
        time_won["1+P"] += 1
    elif power_match:
        win_amount = 4
        time_won["P"] += 1
    else:
        time_won["0"] += 1

    return win_amount


def main():
    ticket_per_drawing = 100
    number_of_drawing = 100
    total_tickets = 0
    spend = 0
    total_won = 0

    white_possibles = list(range(1, 70))
    red_possible = list(range(1, 27))

    time_won = {
        "5+P": 0,
        "5": 0,
        "4+P": 0,
        "4": 0,
        "3+P": 0,
        "3": 0,
        "2+P": 0,
        "1+P": 0,
        "P": 0,
        "0": 0,
    }

    for i in range(number_of_drawing):
        whites_drawn = set(random.sample(white_possibles, k=5))
        red_drawn = random.choice(red_possible)
        winning_drawing = {"whites": whites_drawn, "red": red_drawn}

        for i in range(ticket_per_drawing):
            spend += 2
            total_tickets += 1
            whites_drawn = set(random.sample(white_possibles, k=5))
            red_drawn = random.choice(red_possible)
            my_drawing = {"whites": whites_drawn, "red": red_drawn}
            win_amount = cal_win_ammount(winning_drawing, my_drawing, time_won)
            total_won += win_amount

    print(f"\n{number_of_drawing} drawing, {total_tickets} tickets drawned.")
    print(f"Spent: $ {spend:,}")
    print(f"Total won: $ {total_won:,}")

    print()
    print(json.dumps(time_won, indent=2))


if __name__ == "__main__":
    main()
