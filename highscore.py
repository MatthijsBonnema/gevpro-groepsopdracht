#!/usr/bin/python3


def highscore(name, gold_amount, arrowsleft, number_of_steps, won)

    if won == True:
        score = 5000 - (number_of_steps * 100) + (arrowsleft * 250) + (gold_amount * 1000)
    else:
        score = 0 - (number_of_steps * 100) + (arrowsleft * 250) + (gold_amount * 1000)

    outfile_name = "highscores.txt"
    outfile = open(outfile_name, "w")



    outfile.close()
if __name__ == "__main__":
