voters_classifier = {}

def check_voter(voter):
    if voters_classifier.get(voter):
        print(f"{voter} cant't vote")
    else:
        voters_classifier[voter] = True
        print(f"Let {voter} vote!")


def main():
    voters = ["Maikel", "Juan", "Maria", "Pedro", "Joel", "Maikel", "Jhon"]
    for voter in voters:
        check_voter(voter)


if __name__ == "__main__":
    main()
