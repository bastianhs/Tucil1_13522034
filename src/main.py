import copy, time, random, os
from functions import *


# player choose input from file or randomized
while True:
    input_choice = input("Apakah input dari file atau acak? (file/acak)\n")
    print()
    if input_choice in ["file", "acak"]:
        break
    
    print("Input tidak valid, coba lagi.\n")

if input_choice == "file":
    # read input file
    while True:
        input_file_name = input("Masukkan nama file input: (file berada di dalam folder test)\n")
        print()
        if os.path.isfile("test/" + input_file_name):
            break

        print("File tidak ditemukan.\n")
        
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
        num_of_sequences = int(file_input.readline())

        # read sequences and its rewards
        sequences = [[] for i in range(num_of_sequences)]
        rewards = [0 for i in range(num_of_sequences)]
        for i in range(num_of_sequences):
            sequences[i] = file_input.readline().split()
            rewards[i] = int(file_input.readline())
else:
    while True:
        # enter the data needed for random generator
        print("""Masukkan data berikut:
              1. Banyak token unik
              2. Token unik (dipisahkan dengan spasi)
              3. Ukuran buffer
              4. Ukuran baris dan kolom matriks (dipisahkan dengan spasi)
              5. Banyak sekuens
              6. Ukuran maksimal sekuens""")
        num_of_token = int(input())
        tokens = list(input().split(sep=" "))
        buffer_size = int(input())
        matrix_dimension = input().split(sep=" ")
        matrix_height = int(matrix_dimension[0])
        matrix_width = int(matrix_dimension[1])
        num_of_sequences = int(input())
        max_size_of_sequences = int(input())

        print()

        # check input validity
        input_valid = True
        if num_of_token <= 0:
            input_valid = False
            print("Banyak token harus lebih dari 0.")
        
        if len(tokens) != num_of_token:
            input_valid = False
            print("Banyak token tidak sesuai dengan banyaknya token yang dimasukkan.")
        
        if not all(map(is_token_valid, tokens)):
            input_valid = False
            print("Masukan token tidak valid, masing-masing harus 2 karakter alfanumerik.")
        
        if not is_elements_unique(tokens):
            input_valid = False
            print("Masukan token tidak unik.")

        if buffer_size < 2:
            input_valid = False
            print("Ukuran buffer minimal adalah 2.")
        
        if matrix_height < 1 or matrix_width < 1:
            input_valid = False
            print("Ukuran baris dan kolom matriks minimal adalah 1.")
        
        if num_of_sequences < 1:
            input_valid = False
            print("Banyak sekuens minimal adalah 1.")
        
        if max_size_of_sequences < 2:
            input_valid = False
            print("Ukuran maksimal sekuens paling kecil adalah 2.")
        
        if input_valid:
            break

        print()
    
    # random matrix, sequence, and reward generator
    print("Generating matrix ...")
    matrix = [random.choices(tokens, k=matrix_width) for i in range(matrix_height)]
    print("Generating sequences and rewards ...")
    sequences = [[] for i in range(num_of_sequences)]
    rewards = [0 for i in range(num_of_sequences)]
    for i in range(num_of_sequences):
        sequence_size = random.randrange(2, max_size_of_sequences + 1)
        sequence = random.choices(tokens, k=sequence_size)
        if not sequence in sequences:
            sequences[i] = sequence
        rewards[i] = random.randrange(-50, 51, 10)
    
    print()
    
    # display matrix, sequences, and rewards
    print("Matriks yang dihasilkan:")
    for i in range(matrix_height):
        for j in range(matrix_width):
            print(matrix[i][j], end="")
            if j < matrix_width - 1:
                print(end=" ")
            else:
                print()
    
    print()
    
    print("Sequence dan reward yang dihasilkan:")
    for i in range(num_of_sequences):
        for j in range(len(sequences[i])):
            print(sequences[i][j], end="")
            if j < len(sequences[i]) - 1:
                print(end=" ")
            else:
                print()
        
        print(rewards[i])
    
    print()

# find the solution

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
for start_position in range(0, matrix_width):
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
print("Hasil pencarian:")

print(total_reward)
print(*buffer_solution, sep=" ")
for i in coordinates:
    print(f"{i[0]}, {i[1]}")

print()

duration = end_time - start_time
print(f"{duration * 1000} ms\n")

# ask user to save the result
while True:
    save_solution = input("Apakah ingin menyimpan solusi? (y/n)\n")
    print()
    if save_solution in ["y", "n"]:
        break

    print("Input tidak valid.\n")

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
        file_output.write(f"\n{duration * 1000} ms\n")
