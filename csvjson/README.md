# csvjson

A tiny, dependency-free command-line tool and library to convert tabular data
between **CSV** and **JSON**.

## Install (editable)

```bash
cd csvjson
pip install -e .
```

## Usage

```bash
csvjson data.csv --to json
csvjson data.json --to csv
```

The output format is inferred from the input extension when `--to` is omitted.
