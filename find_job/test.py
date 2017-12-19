import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--keyword', required=True)
args = parser.parse_args()

print (args.keyword)
