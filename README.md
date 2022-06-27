
# Aliaser
Aliaser is an extension of the alias command to curry out aliasing of directories within
folders automatically. All you have to do is create a directory and create files/folders with unique names. To alias them you don't have to manually add them. Aliaser comes to the rescue and you are now left to just type the names in the terminal and vuala.
N.b: Default shell is zsh : change to Your preferred shell
## Authors

- [@yadazora](https://github.com/yadazora)
-
-
## Contributing
Contributions are always welcome!
## Installation

```bash
  git clone https://github.com/michelangeloTM/Aliaser
  cd Aliaser
  sudo ./install
```
## Usage/Examples
Automatically aliases folders in chosen directory path
```python
aliaser -p /path/todir
...............______________________________........................
note:after running this type zsh on your terminal to restart session
```
Automatically aliases all folders in the Chosendir folders
```python
cd Chosendir
aliaser -a auto
```

```python
aliaser -r reset
```
RUNNING FROM THE REPO

Automatically aliases folders in chosen directory path
```python
python3 or ./aliaser -p /path/todir
note:after running this type zsh on your terminal to restart session
```
Automatically aliases all folders in the Chosendir folders
```python
cd Chosendir
python3 /path/to/aliaser -a auto
```
```python
python3 /path/to/aliaser -r reset
```
N.B Aliasing a direcory that contains [aliaser] will also alias [aliaser] & hence edit
the .zshrc file to match accordingly
........................._________________________.................................
N.B Designed for zsh shell/ to run on bash change accordingly
...................................  
