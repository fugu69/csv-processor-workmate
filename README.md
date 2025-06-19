## Project structure

csv_processor/
├── main.py          ← Entry point to run the script
├── processor.py     ← Logic for filtering, aggregation, sorting
├── parser.py        ← Command-line argument handling
├── utils.py         ← Helper functions (like parsing conditions)
├── tests/           ← Folder for test files
│   └── test_main.py ← Your test file
└── products.csv     ← The CSV file to test with
