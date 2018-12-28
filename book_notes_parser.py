
import csv
import sys

def main():
    # Parse kindle csv file to text file to be easier to comment on.
    for arg in sys.argv[1:]:
        with open(arg, "r") as input_file:
            read_csv = csv.reader(input_file)
            read_list = list(read_csv)
        title = read_list[1][0]
        author = read_list[2][0]
        print(title)
        print(author)
        with open(title + ".md", "w") as output_file:
            output_file.write(title+ "\n" + author + "\n\n")
            topics = ['Note', 'Highlight']
            for topic in topics:
                output_file.write(topic + "s\n\n")            
                for row in read_list:
                    if topic in row[0]:
                        output_file.write(row[3] + "\n\n")

if __name__ == "__main__":
    main()
