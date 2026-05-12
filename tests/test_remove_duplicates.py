import pandas as pd
from scripts.remove_duplicates import remove_duplicates

def test_remove_duplicates_creates_clean_file(tmp_path):
    data = pd.DataFrame({
        "id": [1, 1, 2, 3],
        "value": ["A", "A", "B", "C"]
    })
    input_file = tmp_path / "dataset.csv"
    output_file = tmp_path / "dataset_clean.csv"
    data.to_csv(input_file, index=False)

    remove_duplicates(str(input_file), str(output_file))
    cleaned = pd.read_csv(output_file)

    assert cleaned.shape[0] == 3
    assert set(cleaned["id"]) == {1, 2, 3}
