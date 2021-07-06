import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")
math_list = df["mathscore"].to_list()
reading_list = df["readingscore"].to_list()

math_mean = statistics.mean(math_list)
reading_mean = statistics.mean(reading_list)

math_median = statistics.median(math_list)
reading_median = statistics.median(reading_list)

math_mode = statistics.mode(math_list)
reading_mode = statistics.mode(reading_list)

#Printing mean, median and mode to validate
print("Mean, Median and Mode of math is {}, {} and {} respectively".format(math_mean, math_median, math_mode))
print("Mean, Median and Mode of reading is {}, {} and {} respectively".format(reading_mean, reading_median, reading_mode))


math_std_deviation = statistics.stdev(math_list)
reading_std_deviation = statistics.stdev(reading_list)
#1, 2 and 3 Standard Deviations 
math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)
#1, 2 and 3 Standard Deviations 
reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)
#Percentage of data within 1, 2 and 3 Standard Deviations 
math_list_of_data_within_1_std_deviation = [result for result in math_list if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in math_list if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in math_list if result > math_third_std_deviation_start and result < math_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations 
reading_list_of_data_within_1_std_deviation = [result for result in reading_list if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_list_of_data_within_2_std_deviation = [result for result in reading_list if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_list_of_data_within_3_std_deviation = [result for result in reading_list if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]
#Printing data (Standard Deviation)

print("{}% of data for math lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_list)))
print("{}% of data for math lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(math_list)))
print("{}% of data for math lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(math_list)))
print("{}% of data for reading lies within 1 standard deviation".format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 2 standard deviations".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading_list)))
print("{}% of data for reading lies within 3 standard deviations".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading_list)))
