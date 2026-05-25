from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "darwin_suburb_gardens.csv"
OUTPUT_DIR = ROOT / "outputs"
SUMMARY_FILE = OUTPUT_DIR / "garden_summary.json"
SORTED_FILE = OUTPUT_DIR / "suburb_garden_counts_sorted.csv"


def read_garden_data(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as csvfile:
        return list(csv.DictReader(csvfile))


def build_summary(rows: list[dict[str, str]]) -> dict[str, object]:
    suburb_counts = [
        {"suburb": row["suburb"], "gardens": int(row["gardens"])} for row in rows
    ]
    gardens = [item["gardens"] for item in suburb_counts]
    top_5 = sorted(suburb_counts, key=lambda x: x["gardens"], reverse=True)[:5]

    return {
        "total_suburbs": len(suburb_counts),
        "total_gardens": sum(gardens),
        "average_gardens_per_suburb": round(mean(gardens), 2),
        "median_gardens_per_suburb": median(gardens),
        "max_gardens": max(gardens),
        "min_gardens": min(gardens),
        "top_5_suburbs_by_gardens": top_5,
    }


def write_outputs(rows: list[dict[str, str]], summary: dict[str, object]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sorted_rows = sorted(rows, key=lambda row: int(row["gardens"]), reverse=True)
    with SORTED_FILE.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["suburb", "gardens"])
        writer.writeheader()
        writer.writerows(sorted_rows)

    with SUMMARY_FILE.open("w", encoding="utf-8") as jsonfile:
        json.dump(summary, jsonfile, indent=2)


def main() -> None:
    rows = read_garden_data(DATA_FILE)
    summary = build_summary(rows)
    write_outputs(rows, summary)

    print("Garden data analysis completed.")
    print(f"Summary saved to: {SUMMARY_FILE}")
    print(f"Sorted data saved to: {SORTED_FILE}")


if __name__ == "__main__":
    main()
