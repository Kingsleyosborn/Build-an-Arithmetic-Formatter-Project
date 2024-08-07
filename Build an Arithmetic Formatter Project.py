def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""

    for i, problem in enumerate(problems):
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the width needed
        width = max(len(num1), len(num2)) + 2

        # Format the parts
        if i > 0:
            first_line += "    "
            second_line += "    "
            dashes_line += "    "
            answers_line += "    "

        first_line += num1.rjust(width)
        second_line += operator + num2.rjust(width - 1)
        dashes_line += "-" * width

        if display_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answers_line += answer.rjust(width)

    if display_answers:
        arranged_problems = f"{first_line}\n{second_line}\n{dashes_line}\n{answers_line}"
    else:
        arranged_problems = f"{first_line}\n{second_line}\n{dashes_line}"

    return arranged_problems

# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
