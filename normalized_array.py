import numpy as np

def normalized_array(data):
    """
    מנרמלת מערך נתונים לטווח של [0, 1] לפי שיטת Min-Max Scaling.

    הנוסחה לביצוע:
    x_norm = (x - min) / (max - min)

    פרמטרים:
    data (list or np.array): מערך של מספרים.

    מחזירה:
    np.array: מערך מנורמל. אם כל הערכים במערך זהים, יש להחזיר מערך של אפסים.
    """

    data = np.array(data, dtype=float)

    min_val = np.min(data)
    max_val = np.max(data)

    if max_val == min_val:
        return np.zeros_like(data, dtype=float)

    return (data - min_val) / (max_val - min_val)


if __name__ == "__main__":
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
