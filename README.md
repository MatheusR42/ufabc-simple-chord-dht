# distributed-systems-2024


## How to install dependencies


## Python

To setup your virtual env firstly run:

```
virtualenv .venv
source .venv/bin/activate
```

## Generate protocol files and install dependencies

Run:
```
./setup.sh
```

This file will:
- Create python protocol files using `protos/meu-qoelho-mq.proto` and put them in the `node/src/protocols` folder
- Install python dependencies from `node/requirements.txt`

## node

To run node:

```
python3 ./node/src/node.py
```