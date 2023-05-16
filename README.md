![Graph](https://github.com/Eddy-Arch/anime-name-gen/blob/master/data/anime/plot.png)
# Anime Name Generator
This project aims to use AI to generate novel anime chracter names.
The project is a fork of [makemore](https://github.com/karpathy/makemore).
## Improvements
- A new dataset to train a model on "anime.txt" (A dataset of 72 thousand anime character names ripped from a CSV and converted into plain text using VIM and a clever macro)
- Matplot Graphing via "plot.py"
## Usage
There are 4 shell scripts within the projects to act as aliases
for running the long python commands necessary for the stuff here to work.
### Training

```bash
./train-anime.sh
```
This will start training the anime model, saving the output to models/anime/model.pt.

likewise,
```bash
./train-names.sh
```
will do the same thing but will save the output to models/names/model.pt
### Using
The same concept applies for retrieving data from the model.

```bash
./sample-anime.sh
```
For retrieving data from the anime model, and
```bash
./sample-names.sh
```
for the names model.
### Plotting
The plotting is handled via Matplotlib, and works by calling the ```plot.py``` 
file.
Usage goes as follows:
```bash
./plot.py -a 
```
```bash
./plot.py --anime
```
And the same goes for names.
Usage goes as follows:
```bash
./plot.py -n 
```
```bash
./plot.py --names
```
both of which will plot the anime models loss function, and will
store a PNG of the plot at data/names/.
store a PNG of the plot at data/names/.

The plotting itself works via logging the training data of each model
into two files, ```loss.txt``` and ```steps.txt```
loss being the loss function value, and step being the step at
which the loss function was at at the step.

btw, the data in data/ must be deleted when retraining the models,
so that accurate training data is written.
