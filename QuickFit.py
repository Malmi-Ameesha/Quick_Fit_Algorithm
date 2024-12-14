class QuickFit:
    def __init__(self):
        # Initialize memory blocks grouped by their sizes
        # Each key represents the block size, and the value is a dictionary of blocks with their sizes
        self.memory = {
            50: {"block1": 50, "block2": 50},
            100: {"block3": 100, "block4": 100},
            200: {"block5": 200}
        }

    def allocate(self, processSize):
        """
        Allocates memory for a process of the given size using the Quick Fit strategy.
        1. Attempts to find an exact block size match for the process.
        2. If no exact match is found, looks for larger blocks and allocates memory partially.
        3. Returns a message indicating success or failure of memory allocation.
        """
        # Check if a perfect block exists for the process size
        if processSize in self.memory:
            for block, size in self.memory[processSize].items():
                if size >= processSize and size != 0:   # Ensure the block is unused
                    self.memory[processSize][block] = 0  # Mark block as used
                    return f"Process of size {processSize} allocated to {block}"

        ## If no perfect match, search for larger blocks that can accommodate the process
        sorted_keys = sorted(self.memory.keys())    # Sort keys to check blocks in ascending order of size
        for size in sorted_keys:
            if size >= processSize: # Look for blocks larger than or equal to the process size
                for block, block_size in self.memory[size].items():
                    if block_size >= processSize:    # Check if the block can accommodate the process
                        self.memory[size][block] -= processSize  # Partially allocate block
                        return f"Process of size {processSize} allocated to {block} (remaining: {self.memory[size][block]})"

        # If no suitable block is found, return failure message
        return "No space available for the process."

    def viewMemory(self):
        """
        Prints the current state of memory blocks, showing their sizes and availability.
        """

        print("Memory Status:")
        for size, blocks in self.memory.items():
            print(f"Size {size}: {blocks}")

# Example Usage
if __name__ == "__main__":
    quick_fit = QuickFit()
    while True:
        try:
            # Prompt the user to enter the process size
            process_size = int(input("Enter process size: "))
            if process_size == -1:  # Exit condition
                print("Exiting...")
                break

            # Allocate memory for the process and display the result
            result = quick_fit.allocate(process_size)
            print(result)
            quick_fit.viewMemory()
        except ValueError:
             # Handle invalid input gracefully
            print("Invalid input. Please enter an integer.")
