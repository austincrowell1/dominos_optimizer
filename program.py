import datetime
import json
import logging
import os

from domino_optimizer import domino_optimizer

# globals
fn_run_datetime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
run_date = datetime.datetime.now().strftime("%Y-%m-%d")
app_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(app_dir,"config/config.json")

def main(kwargs):
    # get inputs of starting # and hand
    # input_starting_domino = input("Please provide the number on the starting double domino:  ")
    # input_dominos = input("Please provide a comma seperated list of the dominos in your hand in the following format - top #/bottom # i.e. 5/2,6/7,8/4:  ")
    input_starting_domino = "3"
    input_dominos = "3/4,4/6,3/7,6/12,12/11,11/8,5/10,6/5,8/1,8/0,0/2,2/9"
    # input_dominos = "3/4,4/6,6/5,4/7"
    
    logger.info("starting domino: " + input_starting_domino)
    logger.info("dominos in hand: " + input_dominos)

    # convert input to proper datatype - add logic to handle bad inputs
    starting_domino = int(input_starting_domino)
    list_dominos = input_dominos.split(",")

    dom_op = domino_optimizer()
    # breakpoint()
    all_trains = dom_op.get_paths(logger, starting_domino, list_dominos)
    all_scores = [x["score"] for x in all_trains]
    all_scores.sort(reverse=True)
    used_ids = []
    for idx, score in enumerate(all_scores[0:3]):
        # handle tie scores with unique identifier
        curr_train = [x for x in all_trains if x["score"] == score and x["id"] not in used_ids]
        first_curr_train = curr_train[0]
        used_ids.append(first_curr_train["id"])
        str_score = str(first_curr_train["score"])
        str_train = ",".join(first_curr_train["train"])

        output_train = f"#{str(idx+1)} train: score: {str_score}, dominos: {str_train}"
        print(output_train)



    

if __name__ == "__main__":
    log_filename = os.path.join(app_dir,f"logs/dominos_optimizer_{fn_run_datetime}.log")
    logging.basicConfig(
        filename = log_filename,
        level=logging.INFO,
        format = "%(asctime)s - %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S"
    )
    logger = logging.getLogger()

    print("---- APP START ----")
    logger.info("---- APP START ----")

    #load config
    with open(config_dir) as config_file:
        config = json.load(config_file)

    _kwargs = config

    main(_kwargs)