import copy, time
from functions import *


# read input file
input_file_name = input("Masukkan nama file input: (file berada di dalam folder test)\n")
with open("test/" + input_file_name, "r") as file_input:
    
    # read buffer size
    buffer_size = int(file_input.readline())
    
    # read matrix dimension
    matrix_dimension = file_input.readline().split()
    matrix_height = int(matrix_dimension[0])
    matrix_width = int(matrix_dimension[1])
    
    # read matrix content
    matrix = [file_input.readline().split() for i in range(matrix_height)]
    
    # read number of sequences
    number_of_sequences = int(file_input.readline())

    # read sequences and its rewards
    sequences = [[] for i in range(number_of_sequences)]
    rewards = [0 for i in range(number_of_sequences)]
    for i in range(number_of_sequences):
        sequences[i] = file_input.readline().split()
        rewards[i] = int(file_input.readline())


# find the solution

# min_sequences_length = min(map(len, sequences))
# max_rewards = sum(rewards)

# player choose starting position
while True:
    start_position = int(input(f"Pilih posisi kolom token di barisan paling atas: (1 - {matrix_width})\n")) - 1
    if 0 <= start_position <= matrix_width - 1:
        break

    print("Input tidak valid, coba lagi !\n")

start_time = time.time()

# solution variables
total_reward = 0
buffer_solution = []
coordinates = []

# temporary variables
temp_reward = 0
temp_buffer = []
temp_coordinates = []

# process
MIN_BUFFER_SIZE = 2
temp_buffer.append(matrix[0][start_position])
temp_coordinates.append([0, start_position])
i = 2
j = 0
while MIN_BUFFER_SIZE <= i <= buffer_size:
    if is_even(i):
        go_longer = False
        while j < matrix_height and not go_longer:
            last_x_coordinate = temp_coordinates[len(temp_coordinates) - 1][1]
            if not [j, last_x_coordinate] in temp_coordinates:
                temp_buffer.append(matrix[j][last_x_coordinate])
                temp_coordinates.append([j, last_x_coordinate])
                temp_reward = calculate_reward(temp_buffer, sequences, rewards)
                if temp_reward > total_reward:
                    total_reward = temp_reward
                    buffer_solution = copy.deepcopy(temp_buffer)
                    coordinates = copy.deepcopy(temp_coordinates)
                
                if i < buffer_size:
                    i += 1
                    j = 0
                    go_longer = True
                else:
                    temp_buffer.pop()
                    temp_coordinates.pop()
                    j += 1
            else:
                j += 1
        
        if not go_longer:
            i -= 1
            j = temp_coordinates[len(temp_coordinates) - 1][1] + 1
            temp_buffer.pop()
            temp_coordinates.pop()
    else:
        go_longer = False
        while j < matrix_width and not go_longer:
            last_y_coordinate = temp_coordinates[len(temp_coordinates) - 1][0]
            if not [last_y_coordinate, j] in temp_coordinates:
                temp_buffer.append(matrix[last_y_coordinate][j])
                temp_coordinates.append([last_y_coordinate, j])
                temp_reward = calculate_reward(temp_buffer, sequences, rewards)
                if temp_reward > total_reward:
                    total_reward = temp_reward
                    buffer_solution = copy.deepcopy(temp_buffer)
                    coordinates = copy.deepcopy(temp_coordinates)
                
                if i < buffer_size:
                    i += 1
                    j = 0
                    go_longer = True
                else:
                    temp_buffer.pop()
                    temp_coordinates.pop()
                    j += 1
            else:
                j += 1
        
        if not go_longer:
            i -= 1
            j = temp_coordinates[len(temp_coordinates) - 1][0] + 1
            temp_buffer.pop()
            temp_coordinates.pop()

# coordinates formatting
coordinates = [[b + 1, a + 1] for [a, b] in coordinates]

end_time = time.time()

# display result to terminal
print(total_reward)
print(*buffer_solution, sep=" ")
for i in coordinates:
    print(f"{i[0]}, {i[1]}")

print(f"\n{(end_time - start_time) * 1000} ms\n")

# ask user to save the result
save_solution = input("Apakah ingin menyimpan solusi? (y/n)\n")
if save_solution == "y":
    output_file_name = input("Masukkan nama file output: (file berada di dalam folder test)\n")
    with open("test/" + output_file_name, "w") as file_output:

        # write total reward
        file_output.write(str(total_reward) + "\n")

        # write buffer solution
        for i in range(len(buffer_solution)):
            file_output.write(buffer_solution[i])
            if i < len(buffer_solution) - 1:
                file_output.write(" ")
            else:
                file_output.write("\n")
        
        # write coordinates
        for i in coordinates:
            file_output.write(f"{i[0]}, {i[1]}\n")
        
        # write time execution
        file_output.write(f"\n{(end_time - start_time) * 1000} ms\n")
