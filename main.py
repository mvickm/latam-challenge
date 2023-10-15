from datetime import datetime
from src.solutions import *
import click
import json
import time
import logging

# Configure the logging
logging.basicConfig(level=logging.INFO)  # Set the desired logging level

# Generical function to log results
def log_results_generic(results, num_results=10):
    logging.info("Results:")
    for i, result in enumerate(results[:num_results], 1):
        logging.info(f"Result {i}: {result}")

# Function to execute and log execution status
def execute_and_log(function, message_time, message_memory, file_path, log_function):
    logging.info(f"Executing {message_time}...")
    start_time = time.time()
    result = function(file_path)
    execution_time = time.time() - start_time
    logging.info(f"{message_time} executed in {execution_time} seconds.")

    logging.info(f"Executing {message_memory} with memory profiling...")
    start_time = time.time()
    result = function(file_path)
    execution_time = time.time() - start_time
    logging.info(f"{message_memory} executed in {execution_time} seconds.")

    logging.info("Wait for memory profiling")
    time.sleep(2)
    # Call to log results
    log_function(result)

# Main function
@click.command()
@click.option("--file_path", help="Path of JSON file")
def main(file_path):
    # q1 execution
    execute_and_log(q1_time, "q1_time", "q1_memory", file_path, log_results_generic)

    # q2 execution
    execute_and_log(q2_time, "q2_time", "q2_memory", file_path, log_results_generic)

    # q3 execution
    execute_and_log(q3_time, "q3_time", "q3_memory", file_path, log_results_generic)

if __name__ == "__main__":
    main()