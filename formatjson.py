'''
* This script aims to format a json elements to be more pretty
* It replaces long leading spaces to tabs
* It formats json objects into prettier version, by aligning all key value start/end positions
* For example, 
Given ->
{
    "name": "something",
    "somethinglong": "somethingelse"
}

Produces ->
{
	"name"          : "something",
	"somethinglong" : "somethingelse"
}
'''

INPUT_FILE =  "E:/Temp/json.json"

def read_file():
	with open(INPUT_FILE, 'r') as input_file:
		return [leading_spaces_to_tabs(line) for line in input_file.readlines()]


def check_run(line, index, runs):
	if is_of_interest(line):
		last_run = runs[-1]
		last_run.append((line, index))
	else:
		runs.append([])


def is_of_interest(line):
	return ':' in line


def format_run(run, lines):
	colon_indices = [r.index(':') for r,_ in run]
	max_colon_indices = max(colon_indices) + 1
	
	for (line,idx),colon_index in zip(run, colon_indices):
		space_count = max_colon_indices - colon_index
		spaces = ' ' * space_count
		line = line[:colon_index] + spaces + line[colon_index:]
		
		lines[idx] = line


def leading_spaces_to_tabs(line):
	lstr = line.lstrip()
	diff = len(line) - len(lstr)
	diff = int(diff/4)
	return "{0}{1}".format('\t' * diff, lstr)


def do_work():
	lines = read_file()
	runs = []
	for index, line in enumerate(lines):
		check_run(line, index, runs)
	
	for run in [r for r in runs if len(r) > 1]:
		format_run(run, lines)
	
	with open('E:/Temp/out.json', 'w') as outjson:
		for line in lines:
			outjson.write(line)


if __name__ == "__main__":
	do_work()