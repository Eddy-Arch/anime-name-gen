#!/usr/bin/python3
import matplotlib.pyplot as plt
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--anime', action='store_true', help='anime model')
parser.add_argument('-n', '--names', action='store_true', help='names model')

args = parser.parse_args()
if args.anime:
    with open("data/anime/loss.txt", "r") as file:
        numbers = [float(line.strip()) for line in file]

    with open("data/anime/step.txt", "r") as file:
        step = [float(line.strip()) for line in file]
    # Create the plot
    plt.plot(step, numbers)
    plt.xlabel( "Number of steps", fontsize=14)
    plt.ylabel("Loss value", fontsize=14)

    # Display the plot
    plt.savefig('data/anime/plot.png', format='png')
    plt.show()
else:
    with open("data/names/loss.txt", "r") as file:
        numbers = [float(line.strip()) for line in file]

    with open("data/names/step.txt", "r") as file:
        step = [float(line.strip()) for line in file]
    # Create the plot
    plt.plot(step, numbers)
    plt.xlabel( "Number of steps", fontsize=14)
    plt.ylabel("Loss value", fontsize=14)

    # Display the plot
    plt.savefig('data/names/plot.png', format='png')
    plt.show()




# Read the numbers from the file
