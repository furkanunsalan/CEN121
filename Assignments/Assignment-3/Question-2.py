def main():
    index = 0
    true_answers = 0
    false_answers = 0
    grade = ""
    student_answers = []
    correct_answers = [
        "A", "C", "A", "A", "D",
        "B", "C", "A", "C", "B",
        "A", "D", "C", "A", "D",
        "C", "B", "B", "D", "A"
    ]

    answer_file = open("student_answers.txt", "r")

    for line in answer_file:
        question_answer = line.rstrip("\n")
        student_answers.append(question_answer)
    answer_file.close()

    for item in correct_answers:
        if correct_answers[index] == student_answers[index]:
            true_answers += 1
            index += 1
        else:
            false_answers += 1
            index += 1

    if true_answers >= 15:
        grade = "passed"
    else:
        grade = "failed"

    print(f"The student {grade}. Student has {true_answers} true and {false_answers} wrong questions.")


if __name__ == '__main__':
    main()
