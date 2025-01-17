#!/usr/bin/env python

# Supervisor
SUPERVISOR_OK = 10
JUDGE_TIMEOUT = 14
JUDGE_EOF = 15
JUDGE_WRONG_MESSAGE = 11
JUDGE_SCORES_TIMEOUT = 16
JUDGE_SCORES_EOF = 17
JUDGE_WRONG_SCORES = 12
NOT_EXISTING_KILL = 18
NOT_EXISTING_MESSAGE = 13
JUDGE_WRITE = 104

# Bots
BOT_OK = 0
BOT_TLE = 1 # Time limit exceeded
BOT_MLE = 2 # Memory limit exceeded
BOT_KILLED = 3 # Bot killed by judge

# Match statuses
MATCH_NOT_PLAYED = 1
MATCH_WALKOVER = 2
#MATCH_PLAYED = 2
