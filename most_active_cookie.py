#Schuyler Sloman
import sys
import csv

def main():
    command = parse_command()
    file_name, date = command["csv_file"], command["date"]
    reader = csv.reader(open(file_name, 'r'), delimiter=',')
    csv_data = list(reader)
    idx = binary_search(csv_data, date)
    if idx == -1:
        return "N/A"
    frequencies_on_date = find_frequencies(csv_data,date, idx)
    most_frequent = parse_frequencies(frequencies_on_date)
    return "\n".join(most_frequent)

def parse_command():
    i = 1
    csv_file = date = ""
    while i < len(sys.argv):
        if ((i + 1) >= len(sys.argv)):
            raise Exception("nothing after flag (and possibly incorrrect flag)")
        elif str(sys.argv[i]) == "-f":
            csv_file = sys.argv[i + 1]
        elif str(sys.argv[i]) == "-d":
            date = str(sys.argv[i + 1])
        else:
            raise Exception("unknown flag")
        i += 2
    if (csv_file.split(".")[1] != "csv"):
        raise Exception("file name not a csv")
    if (len(date) != 10):
        raise Exception("date must be in yyyy-mm-dd format")
    return {"date":date, "csv_file":csv_file}

def parse_frequencies(freqs):
    ans = []
    best_count = -1
    for k,v in freqs.items():
        if v == best_count:
            ans.append(k)
        elif v > best_count:
            best_count = v
            ans = [k]
    return ans

def find_frequencies(data, date, idx):
    frequencies = {}
    i = idx
    j = idx + 1
    while i >= 1:
        check_date = data[i][1][:10]
        cookie = data[i][0]
        if check_date == date:
            if cookie not in frequencies:
                frequencies[cookie] = 0
            frequencies[cookie] += 1
        i -= 1
    while j < len(data):
        check_date = data[j][1][:10]
        cookie = data[j][0]
        if check_date == date:
            if cookie not in frequencies:
                frequencies[cookie] = 0
            frequencies[cookie] += 1
        j += 1
    return frequencies

def binary_search(data_list, date):
    lo = 1
    hi = len(data_list) - 1
    while lo <= hi:
        mid = (lo + hi)//2
        check_date = data_list[mid][1][:10]
        if check_date == date:
            return mid
        if date_x_before_y(check_date, date):
            hi = mid-1
        else:
            lo = mid+1
    return -1

def date_x_before_y(x, y):
    split_x = x.split("-")
    split_y = y.split("-")
    yy_x,mm_x,dd_x = int(split_x[0]), int(split_x[1]), int(split_x[2])
    yy_y,mm_y,dd_y = int(split_y[0]), int(split_y[1]), int(split_y[2])
    if yy_x < yy_y:
        return True
    elif (yy_x == yy_y) and mm_x < mm_y:
        return True
    elif (yy_x == yy_y) and (mm_x == mm_y) and dd_x < dd_y:
        return True 
    else:
        return False


if __name__ == "__main__":
    ans = main()
    print(ans)