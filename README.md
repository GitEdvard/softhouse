# stock-winners

Show today's stock winner. 

## Pre-requirements (Windows)
- Python
- Miniconda
- Create conda environment with python 3.9 or above
  - ```conda create --name stock python=3.9```
  - For some reason, it doesn't work unless ''python=...'' is specified
- Activate conda environment
  - ```conda activate stock```

## Installation
- ```python -m pip install -U git+https://github.com/gitedvard/stock-winners.git#egg=stock-winners```

## Usage
- Start service (from conda shell), ```stock-winners --port 2000```
- Receive the winners (from cmd), ```curl localhost:2000/api/winners```
- Profit
