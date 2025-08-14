from __future__ import annotations
import argparse
from pathlib import Path

from .io import load_csv
from .stats import mean, median, mode, variance, stddev, correlation_matrix
from .plots import histogram, boxplot, scatter

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="stats_helper: quick stats & plots for CSV files.")
    p.add_argument("csv", help="Path to CSV file.")
    p.add_argument("--summary", action="store_true", help="Print summary stats for numeric columns.")
    p.add_argument("--hist", metavar="COLUMN", help="Generate histogram for COLUMN.")
    p.add_argument("--bins", type=int, default=10, help="Bins for histogram (default: 10).")
    p.add_argument("--box", metavar="COLUMN", help="Generate boxplot for COLUMN.")
    p.add_argument("--scatter", nargs=2, metavar=("X", "Y"), help="Generate scatter plot between X and Y.")
    p.add_argument("--outdir", default="outputs", help="Directory to save plots (default: outputs).")
    return p

def main(argv=None):
    args = build_parser().parse_args(argv)
    df = load_csv(args.csv)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if args.summary:
        numeric = df.select_dtypes(include="number")
        print("=== Summary (describe) ===")
        print(numeric.describe())
        print("\n=== Additional metrics ===")
        for col in numeric.columns:
            print(f"\n[{col}]")
            print("mean:", mean(numeric[col]))
            print("median:", median(numeric[col]))
            print("mode:", mode(numeric[col]))
            print("variance (ddof=1):", variance(numeric[col]))
            print("stddev (ddof=1):", stddev(numeric[col]))
        print("\n=== Correlation Matrix ===")
        print(correlation_matrix(df))

    if args.hist:
        path = outdir / f"hist_{args.hist}.png"
        histogram(df, args.hist, bins=args.bins, out=str(path))
        print(f"Saved histogram to {path}")

    if args.box:
        path = outdir / f"box_{args.box}.png"
        boxplot(df, args.box, out=str(path))
        print(f"Saved boxplot to {path}")

    if args.scatter:
        x, y = args.scatter
        path = outdir / f"scatter_{x}_vs_{y}.png"
        scatter(df, x, y, out=str(path))
        print(f"Saved scatter plot to {path}")

if __name__ == "__main__":
    main()
