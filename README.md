# basis
An interpreter for the Programming Basics book (https://github.com/prgbas/book)

## Install

```
git clone https://github.com/Jelleas/basis
cd basis
pip install .
```

## Run

```
python basis examples/greedy.code
python basis examples/fib_it.code --verbose
```

## Test

```
pytest
```

## Build
Install ANTLR4. Then replace ANTLR path in `build.sh` with the path to your ANTLR installation.

```
bash build.sh
```

The newly generated lexer / parser are found in `basis/lang`
