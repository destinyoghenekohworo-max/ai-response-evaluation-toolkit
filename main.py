
def get_score(criterion):
    while True:
        try:
            score = int(input(f"Rate {criterion} (1-5): "))

            if 1 <= score <= 5:
                return score
            else:
                print("Enter a score between 1 and 5.")

        except ValueError:
            print("Invalid input. Enter a whole number.")


def evaluate_response():
    print("\nAI RESPONSE EVALUATION TOOLKIT")
    print("--------------------------------")

    accuracy = get_score("Accuracy")
    relevance = get_score("Relevance")
    clarity = get_score("Clarity")
    completeness = get_score("Completeness")

    total = accuracy + relevance + clarity + completeness
    average = total / 4
    percentage = (total / 20) * 100

    print("\nEVALUATION RESULTS")
    print("------------------")
    print(f"Accuracy: {accuracy}/5")
    print(f"Relevance: {relevance}/5")
    print(f"Clarity: {clarity}/5")
    print(f"Completeness: {completeness}/5")

    print(f"\nAverage Score: {average:.2f}/5")
    print(f"Overall Quality: {percentage:.1f}%")

    if percentage >= 80:
        print("Rating: Excellent")
    elif percentage >= 60:
        print("Rating: Good")
    elif percentage >= 40:
        print("Rating: Fair")
    else:
        print("Rating: Poor")


if __name__ == "__main__":
    evaluate_response()
