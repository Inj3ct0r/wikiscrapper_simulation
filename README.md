# wikiscrapper_simulation
Based on the `wiki-articles-crawler` made by _SadMadLad_ https://github.com/SadMadLad/wiki-articles-crawler 

A python script that does the following: Mimics a webscraper that visits a Wikipedia link, retrieves all links in the body-content and visits one at random until a fixed amount of links have been visited.
The script uses a known list of numbers rather than random links parsed from bs4, then plots the resulting article paths as small-world networks and shows a bar plot showcasing the grades of every node.

## Requirements
Python and the following libraries
- numpy
- pandas
- matplotlib.pyplot
- random
- networkx

## Usage
The `wikiscrapper_simulation.py` takes three parameters: Epochs (how many nodes each path will have), paths (how many iterations the script will run from a fixed initial element) and num_list (our universe of possible values chosen at random by the code).

## Output
Example using epochs=4, paths=4, num_list=100
```
List 1 [0, 95, 61, 43, 54]
List 2 [0, 70, 28, 29, 32]
List 3 [0, 5, 62, 14, 40]
List 4 [0, 40, 89, 94, 26]

![image](https://github.com/Inj3ct0r/wikiscrapper_simulation/assets/95256181/ea90c58e-2112-4347-863d-443245b80ba1)
![image](https://github.com/Inj3ct0r/wikiscrapper_simulation/assets/95256181/ed832042-4edd-4441-ba6e-05afe4c4074b)
```
##### Taller de manejo y analisis de datos 2023
