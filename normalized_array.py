import numpy as np

def normalized_array(data):
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
