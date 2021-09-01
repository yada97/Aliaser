
# Aliaser

Alias all folder names within a directory. Have many directories in your projects folder?, Don't worry they are all aliased using their directory names and all you have to do is cd directory.




## Authors

- [@michelangeloTM](https://github.com/michelangeloTM)
-
-


  
## Contributing

Contributions are always welcome!



  
## Installation

Install my-project with npm

```bash
  https://github.com/michelangeloTM/Aliaser
  cd Aliaser
  ./install
```

    
## Usage/Examples
Automatically aliases folders in chosen directory path
```python
aliaser -p /path/todir
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

N.B Designed for zsh shell/ to run on bash change accordingly
  
