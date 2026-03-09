import datetime
import json
import logging
import os
import uuid

class domino_optimizer:
    def __init__(self):
        self.all_trains = []
        self.it_count = 0
    
    def get_paths(self, logger, curr_num, list_dominos, curr_train=None, curr_score=0):
        if curr_train is None:
            curr_train = []
        
        # track number of iterations
        self.it_count += 1
        logger.info("currently on iteration #" + str(self.it_count))
        # log iteration data
        logger.info("    curr_num = " + str(curr_num))
        logger.info("    list_dominos = " + ",".join(list_dominos))
        logger.info("    curr_train = " + ",".join(curr_train))
        logger.info("    curr_score = " + str(curr_score))

        # default to no match
        match_found = False
        
        #breakpoint()
        for domino in list_dominos:
            dom_nums = [int(x) for x in domino.split("/")]
            # breakpoint()
            if curr_num in dom_nums:
                match_found = True
                # get the number that DOESN'T match the current number being compared to - will be the starting_domino in the next iteration
                next_num = dom_nums[0] if dom_nums[1] == curr_num else dom_nums[1]
                # remove the current domino from the list
                remaining_dominos = [x for x in list_dominos if x != domino]

                # add match to train
                curr_train.append(domino)
                
                #recusion
                self.get_paths(
                    logger,
                    next_num, 
                    remaining_dominos, 
                    curr_train, 
                    curr_score + dom_nums[0] + dom_nums[1]
                )
                # remove the current match to backtrack               
                curr_train.pop()
                # breakpoint()

        if not match_found:
            logger.info("End of train")
            logger.info("final train: " + ",".join(curr_train))
            # breakpoint()
            self.all_trains.append(
                {
                    "id":uuid.uuid1(),
                    "score":curr_score,
                    "train":curr_train.copy(),
                    "leftovers":list_dominos.copy()
                }
            )

        return self.all_trains