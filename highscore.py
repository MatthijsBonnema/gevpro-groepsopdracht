#!/usr/bin/python3


def highscore(name, gold_amount, arrowsleft, number_of_steps, won):

    if won:
        score = 5000 - (number_of_steps * 100) + (arrowsleft * 250) + (gold_amount * 1000)
    else:
        score = 0 - (number_of_steps * 100) + (arrowsleft * 250) + (gold_amount * 1000)

    print("Score: ", score)
    scorestring = str(score) +" "+ str(name) + "\n"

    outfile_name = "highscores.txt"
    outfile = open(outfile_name, "a")

    outfile.write(scorestring)



    outfile.close()
if __name__ == "__main__":
    print("Yolo")
