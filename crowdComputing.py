from statistics import mean

# Initialize an empty list to store the estimates
estimates = []

# Variable to control the loop
c = 1

# Loop to collect data from the user
while c != 0:
    # Prompt the user to enter data and add it to the estimates list
    estimates.append(int(input("Enter Data: ")))

    # Prompt the user to continue or end the data entry
    print("Continue: 1")
    print("End: 0")
    c = int(input("Enter choice: "))

# Sort the estimates in ascending order
estimates.sort()

# Calculate the number of elements to remove from both ends
trim_value = int(0.1 * len(estimates))

# Remove the trim_value number of elements from the beginning and end of the sorted estimates
estimates = estimates[trim_value:]
estimates = estimates[:len(estimates) - trim_value]

# Calculate and print the mean of the trimmed estimates
print("Mean:", mean(estimates))
