# CSV Processor

A Python command-line tool for processing CSV files.  
Supports filtering, aggregation (avg, min, max), and sorting.

## ✅ Features

- Filter rows with `--where`
- Aggregate numeric columns with `--aggregate`
- Sort rows with `--order-by`
- Pretty table output using `tabulate`
- No external dependencies (except tabulate)

---

## 📦 Installation

1. Clone the repo:
```bash
git clone https://github.com/your-username/csv-processor.git
cd csv-processor
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

---

## 🛠 Usage
### Prepare a CSV file like products.csv:
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
poco x5 pro,xiaomi,299,4.4

### 📄 Show all data
```bash
python main.py --file products.csv
```

### 🔎 Filter rows
```bash
python main.py --file products.csv --where "rating>4.5"
```

### 📊 Aggregate numeric values
```bash
python main.py --file products.csv --aggregate "price=avg"
python main.py --file products.csv --aggregate "rating=max"
```

### ↕️ Sort rows
```bash
python main.py --file products.csv --order-by "price=desc"
python main.py --file products.csv --order-by "name=asc"
```

### 🧠 Combine everything
```bash
python main.py --file products.csv \
  --where "brand=xiaomi" \
  --order-by "price=asc" \
  --aggregate "price=max"
```

---

## 🧪 Run Tests
```bash
pytest
```

- Make sure you have all test dependencies installed.

---

## 📂 Project Structure

csv-processor/
├── main.py             ← Entry point to run the script
├── parser.py           ← Command-line argument handling
├── processor.py        ← Logic for filtering, aggregation, sorting
├── utils.py            ← Helper functions (like parsing conditions)
├── products.csv        ← The CSV file to test with
├── tests/
│   └── test_main.py    ← Test file
└── README.md

---

## 📋 Notes

- Aggregation works only on numeric columns
- Sorting falls back to string sort if values can't be converted to float
- Input files must be valid .csv format

---

## 📜 License
MIT — feel free to use and modify.






## Project structure

csv_processor/
├── main.py             ← Entry point to run the script
├── processor.py        ← Logic for filtering, aggregation, sorting
├── parser.py           ← Command-line argument handling
├── utils.py            ← Helper functions (like parsing conditions)
├── tests/              ← Folder for test files
│   └── test_main.py    ← Test file
└── products.csv        ← The CSV file to test with
