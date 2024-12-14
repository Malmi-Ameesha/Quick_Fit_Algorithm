class QuickFit:
    def __init__(self):
        # Memory blocks grouped by sizes
        self.memory = {
            50: {"block1": 50, "block2": 50},
            100: {"block3": 100, "block4": 100},
            200: {"block5": 200}
        }

    def allocate(self, processSize):
        """
        Allocates memory for a process of the given size using Quick Fit strategy.
        """
        # Check if a perfect block exists
        if processSize in self.memory:
            for block, size in self.memory[processSize].items():
                if size >= processSize and size != 0:
                    self.memory[processSize][block] = 0  # Mark block as used
                    return f"Process of size {processSize} allocated to {block}"

        # Check for larger blocks
        sorted_keys = sorted(self.memory.keys())
        for size in sorted_keys:
            if size >= processSize:  # Larger block available
                for block, block_size in self.memory[size].items():
                    if block_size >= processSize:
                        self.memory[size][block] -= processSize  # Allocate partially
                        return f"Process of size {processSize} allocated to {block} (remaining: {self.memory[size][block]})"

        return "No space available for the process."

    def viewMemory(self):
        """
        Prints the current state of memory blocks.
        """
        print("Memory Status:")
        for size, blocks in self.memory.items():
            print(f"Size {size}: {blocks}")

# Example Usage
if __name__ == "__main__":
    quick_fit = QuickFit()
    while True:
        try:
            process_size = int(input("Enter process size: "))
            if process_size == -1:
                print("Exiting...")
                break
            result = quick_fit.allocate(process_size)
            print(result)
            quick_fit.viewMemory()
        except ValueError:
            print("Invalid input. Please enter an integer.")
