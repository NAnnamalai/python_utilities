import yaml
# parse yaml
with open('config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

for k, v in data.items():
    print("========================================")
    print(k)
    print("       -----------------                ")
    for wording, number in sorted(v.items(), key=lambda item: item[1]):
        print(f"{wording}: {number}")
    print("========================================")


# we end up not writing these three dictionaries in python as
'''
numbers = {
  "even-numbers": {
    "two": 2,
    "four": 4,
    "six": 6,
    "eight": 8,
    "ten": 10
  },
  "odd-numbers": {
     "one": 1,
     "three": 3,
     "five": 5,
     "seven": 7,
     "nine": 9
  },
  "all-numbers": {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10
  }
}
'''