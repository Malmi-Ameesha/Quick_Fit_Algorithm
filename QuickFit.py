class QuickFit:
    def __init__(self):
        # Initialize memory blocks grouped by their sizes
        self.memory = {
            50: {"block1": 50, "block2": 50},
            100: {"block3": 100, "block4": 100},
            200: {"block5": 200}
        }

    def allocate(self, processSize):
        # Check if the input process size exists in the memory blocks
        if processSize in self.memory:
            for key, value in self.memory[processSize].items():
                if value >= processSize and value != 0:
                    self.memory[processSize][key] = 0  # Mark the block as allocated
                    return f"{processSize} Size can Allocate "  # Print size and result
        else:
            sorted_key = sorted(self.memory.keys())  # Sort the memory block sizes
            for key in sorted_key:
                for keyele, value in self.memory[key].items():
                    if value != 0 and processSize <= value:
                        self.memory[key][keyele] = value - processSize  # Allocate the block
                        return f"{processSize} Add"  # Print size and result
            return f"{processSize} No Space in the memory"  # No suitable block found

    def viewMemory(self):
        for size, blocks in self.memory.items():
            for block, value in blocks.items():
                print(f"Memory size: {size}, Block: {block}, Value: {value}")


# Initialize the QuickFit class
x = QuickFit()

# Run the allocation loop
isRun = True
while isRun:
    try:
        sizeOfAllocate = int(input("Enter the size you want to allocate: "))
        response = x.allocate(sizeOfAllocate)  # Try to allocate memory
        print(response)  # Print size and allocation result
        x.viewMemory()  # Show memory status
    except ValueError:
        print("Invalid input! Please enter a valid number.")
