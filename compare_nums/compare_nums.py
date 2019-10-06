import csv
import json





def main():
	r = csv.reader(open('./nums1.csv', 'r'))
	lines = [l for l in r]

	s = csv.reader(open('./nums2.csv', 'r'))
	lines2 = [l for l in s]

	result = compare(lines, lines2)


def compare(lines, lines2):
	for n in lines2:
		if n not in lines:
			print(n[0])

if __name__ == '__main__':
	main()