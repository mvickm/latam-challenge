from datetime import datetime
from src.solutions import *
import click
import json
import time

# Generical function to print results
def print_results_generic(results, num_results=10):
    print("Results:")
    for i, result in enumerate(results[:num_results], 1):
        print(f"Result {i}: {result}")

# Function to execute and print execution status
def execute_and_print(function, message_time, message_memory, file_path, print_function):
    print(f"Executing {message_time}...")
    start_time = time.time()
    result = function(file_path)
    execution_time = time.time() - start_time
    print(f"{message_time} executed in {execution_time} seconds.")

    print(f"Executing {message_memory} with memory profiling...")
    start_time = time.time()
    result = function(file_path)
    execution_time = time.time() - start_time
    print(f"{message_memory} executed in {execution_time} seconds.")

    print("Wait for memory profiling")
    time.sleep(2)
    # Call to print results
    print_function(result)
    
# Main function
@click.command()
@click.option("--file_path", help="Path of JSON file")

def main(file_path):
    
    # q1 execution
    execute_and_print(q1_time, "q1_time", "q1_memory", file_path, print_results_generic)

    # q2 execution
    execute_and_print(q2_time, "q2_time", "q2_memory", file_path, print_results_generic)

    # q3 execution
    execute_and_print(q3_time, "q3_time", "q3_memory", file_path, print_results_generic)

if __name__ == "__main__":
    main()
