Creating a virtual environment:
```bash
python3 -m venv <venv>
```

Activating virtual environment:
```bash
source <venv>/bin/activate
```

Creating a requirements.txt file:
```bash
touch requirements.txt
```

Install the requirements.txt file
```bash
pip install -r requirements.txt
```

Initiating Git:
```bash
git init
```
Initiating DVC:
```bash
dvc init
```
Adding Dataset to DVC:
```bash
dvc add data_given/winequality.csv
```