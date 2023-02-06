import random
import json


def cal_win_amount(my_numbers, winning_numbers, time_won):
    win_amount = 0

    white_matches = len(my_numbers["whites"].intersection(winning_numbers["whites"]))
    power_matches = my_numbers["red"] == winning_numbers["red"]

    if white_matches == 5:
        if power_matches:
            win_amount = 2_000_000_000
            time_won["5+P"] += 1
        else:
            win_amount = 1_000_000
            time_won["5"] += 1
    elif white_matches == 4:
        if power_matches:
            win_amount = 50_000
            time_won["4+P"] += 1
        else:
            win_amount = 100
            time_won["4"] += 1
    elif white_matches == 3:
        if power_matches:
            win_amount = 100
            time_won["3+P"] += 1
        else:
            win_amount = 7
            time_won["3"] += 1
    elif white_matches == 2 and power_matches:
        win_amount = 7
        time_won["2+P"] += 1
    elif white_matches == 1 and power_matches:
        win_amount = 4
        time_won["1+P"] += 1
    elif power_matches:
        win_amount = 4
        time_won["P"] += 1
    else:
        time_won["0"] += 1

    return win_amount


def main():
    tickets_per_drawing = 100
    number_of_drawing = 100

    white_possibilities = list(range(1, 70))
    red_possibilities = list(range(1, 27))

    # print(white_possibilities)
    # print(red_possibilities)

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

    spent = 0
    total_win_amount = 0
    total_tickets = 0
    years = 0

    # for i in range(number_of_drawing):
    hit_jackpot = False

    while True:
        number_of_drawing += 1
        whites_drawn = set(random.sample(white_possibilities, k=5))
        red_drawn = random.choice(red_possibilities)
        winning_numbers = {"whites": whites_drawn, "red": red_drawn}

        for i in range(tickets_per_drawing):
            spent += 2
            total_tickets += 1
            whites_drawn = set(random.sample(white_possibilities, k=5))
            red_drawn = random.choice(red_possibilities)
            my_numbers = {"whites": whites_drawn, "red": red_drawn}

            win_amount = cal_win_amount(my_numbers, winning_numbers, time_won)
            total_win_amount += win_amount

            if total_win_amount > 2_000_000:
                hit_jackpot = True
                break

        if number_of_drawing % 156 == 0:
            years += 1
            print(f"\n{years} years passed", end="")

        if hit_jackpot:
            break

    print(f", {number_of_drawing} drawing, {total_tickets} tickets drawned.")
    print(f"Spent: $ {spent:,}")
    print(f"Earned: $ {total_win_amount:,}")

    print()
    print(json.dumps(time_won, indent=2))


if __name__ == "__main__":
    main()
