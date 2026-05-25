# Darwin Garden Data Analysis

This repository analyzes the number of gardens in Darwin (AU) suburbs and prepares data for reporting in Power BI.

## Data

- Input file: `data/darwin_suburb_gardens.csv`
- Columns:
  - `suburb`: suburb name
  - `gardens`: number of gardens in that suburb

## Run analysis

From the repository root:

```bash
python3 scripts/analyze_gardens.py
```

This generates:

- `outputs/garden_summary.json` (key statistics)
- `outputs/suburb_garden_counts_sorted.csv` (suburbs sorted by garden count)

## Statistics produced

- Total suburbs
- Total gardens
- Average gardens per suburb
- Median gardens per suburb
- Minimum and maximum gardens
- Top 5 suburbs by garden count

## Power BI dashboard setup

1. Open Power BI Desktop.
2. Import `data/darwin_suburb_gardens.csv` (or `outputs/suburb_garden_counts_sorted.csv`).
3. Create cards for:
   - Total Suburbs
   - Total Gardens
   - Average Gardens per Suburb
4. Create visuals:
   - Bar chart: `suburb` vs `gardens`
   - Top N filter (Top 5 suburbs by `gardens`)
   - Table with all suburbs and garden counts
5. Sort charts by `gardens` descending.
