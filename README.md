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

![small-world network](https://github.com/Inj3ct0r/wikiscrapper_simulation/assets/95256181/bc87db80-299f-4f20-ace2-41f707b0b598)

![image](/Screenshots/degrees barplot.png)
```
##### Taller de manejo y analisis de datos 2023
