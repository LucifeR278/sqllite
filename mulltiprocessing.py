import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i * i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")

## Create 2 processes
if __name__ == "__main__":
    # Create the Process objects
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    # Start the timer
    start_time = time.time()

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()

    # Calculate and print the total time taken
    total_time = time.time() - start_time
    print(f"Finished in {total_time:.2f} seconds")
