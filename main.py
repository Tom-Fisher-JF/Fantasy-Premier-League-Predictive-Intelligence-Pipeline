from processing import run_dual_pipeline, get_raw_season_data, split_by_recent_gw_percent
from models import run_linear_comparison, run_tree_comparison

def main():
    seasons_list = ["2020-21","2021-22", "2022-23", "2023-24",
                    "2024-25", "2025-26", "2026-27"]
    raw_dfs = get_raw_season_data(seasons_list)

    df_linear, df_tree = run_dual_pipeline(raw_dfs=raw_dfs)
    df_tree.to_csv('Fantasy-Premier-League-data/tree_data.csv', index=False)
    df_linear.to_csv('Fantasy-Premier-League-data/linear_datafile.csv', index=False)

    linear_split = split_by_recent_gw_percent(df_linear) #->(X_train, y_train, X_val, y_val)
    linear_results = run_linear_comparison(linear_split)

    tree_split = split_by_recent_gw_percent(df_tree)
    tree_results = run_tree_comparison(tree_split)

    print(tree_results)
    print(linear_results)
    return

if __name__ == "__main__":
    main()