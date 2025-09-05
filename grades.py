from typing import List

def average(grades: List[float]) -> float:
    """Return the average of the grades."""
    return sum(grades) / len(grades)

def max_grade(grades: List[float]) -> float:
    """Return the maximum grade."""
    max_val = grades[0]
    for g in grades:
        if g > max_val:
            max_val = g
    return max_val

def main() -> None:
    """Run sample calculation and print results."""
    grades = [90, 80, 70, 85, 60]
    avg = average(grades)
    maxg = max_grade(grades)
    print("Average:", avg, "Max:", maxg)

if __name__ == "__main__":
    main()
