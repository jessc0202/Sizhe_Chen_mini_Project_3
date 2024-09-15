"""
Test goes here

"""
import pandas as pd
from main import load_dataset, general_describe, generate_vis, generate_dist, visualize_boxplot
import matplotlib.pyplot as plt

dataset = "/Users/chensi/Desktop/MIDS/Fall 2024/IDS 706/HW2/StudentPerformanceFactors.csv"
df = load_dataset(dataset)
def test_load_dataset():
    df_test = load_dataset(dataset)  # Ensure this function uses the correct path
    assert isinstance(df_test, pd.DataFrame), "The loaded dataset should be a DataFrame."

# Test the general_describe function for 'Hours_Studied'
def test_general_describe():
    desc = general_describe(df, 'Hours_Studied')
    assert round(desc['mean'], 6) == 19.975329, "Mean of 'Hours_Studied' should be 19.975329."
    assert desc['50%'] == 20.0, "Median (50%) of 'Hours_Studied' should be 20."
    assert desc['max'] == 44.0, "Max of 'Hours_Studied' should be 44."
    assert desc['min'] == 1.0, "Min of 'Hours_Studied' should be 1."
    assert round(desc['std'], 6) == 5.990594, "Standard deviation of 'Hours_Studied' should be 5.990594."
    assert desc['25%'] == 16.0, "25th percentile of 'Hours_Studied' should be 16."
    assert desc['75%'] == 24.0, "75th percentile of 'Hours_Studied' should be 24."

# Test the generate_vis function for 'Hours_Studied' vs 'Exam_Score'
def test_generate_vis():
    try:
        generate_vis(df, 'Hours_Studied', 'Exam_Score')
    except Exception as e:
        assert False, f"generate_vis raised an exception: {e}"

# Test the generate_dist function for 'Hours_Studied'
def test_generate_dist():
    try:
        generate_dist(df, 'Hours_Studied')
    except Exception as e:
        assert False, f"generate_dist raised an exception: {e}"

# Test the visualize_boxplot function for 'Hours_Studied'
def test_visualize_boxplot():
    try:
        visualize_boxplot(df, 'Hours_Studied')
    except Exception as e:
        assert False, f"visualize_boxplot raised an exception: {e}"

# Run the tests
if __name__ == "__main__":
    test_load_dataset()
    test_general_describe()
    test_generate_vis()
    test_generate_dist()
    test_visualize_boxplot()
    print("All tests passed.")
