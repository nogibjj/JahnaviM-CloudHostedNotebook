from mylib.lib import read_df, summarize_df, hist_time_occ

def test_read_df():
    df = read_df("Crime_Data_from_2020_to_Present.csv.zip")
    assert df.shape == (974477, 29)
    return True

def test_summarize_df():
    df = read_df("Crime_Data_from_2020_to_Present.csv.zip")
    summary = summarize_df(df)
    assert summary.shape == (8, 16)
    return True

def test_hist_time_occ():
    df = read_df("Crime_Data_from_2020_to_Present.csv.zip")
    output_message = hist_time_occ(df)
    assert output_message == "Histogram Loaded"
    return True

if __name__ == "__main__":
    test_read_df()
    test_summarize_df()
    test_hist_time_occ()
    print("All tests passed")