#!/usr/bin/env python3

import json, sys, os

ground_truth_dir_path = sys.argv[1]
run_file_name = sys.argv[2]
output_file_name = sys.argv[3]

turn_ids = {}
with open(os.path.join(ground_truth_dir_path, "scai-eval24-turn-ids.txt")) as turn_ids_file:
    turn_ids = set([turn_id.strip() for turn_id in turn_ids_file])

conversation_ids = {}
with open(os.path.join(ground_truth_dir_path, "scai-eval24-conversation-ids.txt")) as conversation_ids_file:
    conversation_ids = set([conversation_id.strip() for conversation_id in conversation_ids_file])

conversation_label_counts = {}
turn_label_counts = {}
with open(run_file_name) as run_file:
    labels = json.load(run_file)
    num_conversations = 0
    num_turns = 0
    num_unknown = 0
    for key in labels:
        if key in turn_ids:
            num_turns += 1
            for label in labels[key]:
                if label not in turn_label_counts:
                    turn_label_counts[label] = 1
                else:
                    turn_label_counts[label] += 1
        elif key in conversation_ids:
            num_conversations += 1
            for label in labels[key]:
                if label not in conversation_label_counts:
                    conversation_label_counts[label] = 1
                else:
                    conversation_label_counts[label] += 1
        else:
            sys.stderr.write("Unknown ID: " + key + "\n")
            num_unknown += 1

sys.stderr.write("\n")
sys.stderr.write("Unknown IDs: " + str(num_unknown) + "\n")
sys.stderr.write("Conversations labeled: " + str(num_conversations) + " of " + str(len(conversation_ids)) + "\n")
sys.stderr.write("Conversation label counts: " + str(conversation_label_counts) + "\n")
sys.stderr.write("Turns labeled: " + str(num_turns) + " of " + str(len(turn_ids)) + "\n")
sys.stderr.write("Turn label counts: " + str(turn_label_counts) + "\n")

with open(output_file_name, "w") as output_file:
    output_file.write("measure {\n key: \"Conversations\"\n value: \"" + str(num_conversations) + "\"\n}\n")
    output_file.write("measure {\n key: \"Turns\"\n value: \"" + str(num_turns) + "\"\n}\n")

