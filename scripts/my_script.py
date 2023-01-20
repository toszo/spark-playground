from pyspark import SparkContext

# Initialize Spark
sc = SparkContext("local", "Line Counter")

# Read the text file
text_file = sc.textFile("/data/mytext.txt")

# Count the number of lines
line_count = text_file.count()

# Print the result
print("Number of lines:", line_count)

# Stop Spark
sc.stop()