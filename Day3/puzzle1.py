#!/usr/bin/python

def main():
    file = open("input.txt", "r")
    coordinates = {}
    for line in file.readlines():
        claim = parse_claim(line)
        for width in range(claim["width"]):
            for height in range(claim["height"]):
                coordinate = '{}:{}'.format(width + claim["left_offset"], height + claim["top_offset"])
                coordinates[coordinate] = coordinates[coordinate]+1 if coordinate in coordinates else 1
    
    print(len([i for i in coordinates.values() if i > 1]))
        
def parse_claim(raw_value):
    parts = raw_value.split()
    return {
        "id": int(parts[0][1:]),
        "left_offset": int(parts[2].split(',')[0]),
        "top_offset": int(parts[2].split(',')[1][:-1]),
        "width": int(parts[3].split('x')[0]),
        "height": int(parts[3].split('x')[1]),
    }
        
if __name__ == '__main__':
    main()