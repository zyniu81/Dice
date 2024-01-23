import random
import sys


def dice():
    """
    Simulate dice rolling based on user input in the format xDy+z.

    Returns:
    int: Result of the dice roll.

    Raises:
    ValueError: If the input dice code is invalid.

    Example:
    >>> print(dice())
    """
    try:
        code_dice = list(input("""x - how many dice (optional)
D - required
y - type of dice (required)
+/- z - how many add or subtract to result roll dice (optional)
Enter dice code in format xDy+z: """))

#       Numbers before D
        d = code_dice.index("D")
        d_list = code_dice[:d]
        d_2 = "".join(d_list)
        d_3 = int(d_2) if d_2.isdigit() else 1

#       index sign + or -
        y = code_dice.index("+") if "+" in code_dice else code_dice.index("-") if "-" in code_dice else None

#       Type of dice
        dice_1 = "".join(code_dice[d+1:y])

#       Index sign + or - for type of dice
        if "+" in code_dice or "-" in code_dice:
            result = dice_1
        else:
            result = "".join(code_dice[d+1:])

#       Result dice
        dice_list = []
        for _ in range(d_3):
            dice_1 = "".join(code_dice[d + 1:y])

            if "+" in code_dice or "-" in code_dice:
                result = dice_1
            else:
                result = "".join(code_dice[d + 1:])
            result_2 = random.randint(1, int(result))
            dice_list.append(result_2)

#       Numbers after sign + or -
        list_after_sign = "".join(code_dice[y+1:]) if y is not None else ""

#      Adding or subtract
        if "+" in code_dice:
            result_dice = sum(dice_list) + int(list_after_sign)
        elif "-" in code_dice:
            result_dice = sum(dice_list) - int(list_after_sign)
        else:
            result_dice = sum(dice_list)

        return result_dice
    except ValueError:
        print("Invalid dice code!")
        sys.exit(1)


print(dice())
