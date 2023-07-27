import matplotlib.pyplot as plt
import time

# binary search algorithm to find the target value in the array
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# visualisation function to display the binary search process
def visualise_binary_search(arr, target):
    fig, ax = plt.subplots()
    fig.canvas.manager.full_screen_toggle()
    ax.set_title("Binary Search Visualisation")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")

    ax.bar(range(len(arr)), arr, color = "skyblue")
    # pause to display the initial array
    plt.pause(1)  

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        ax.bar(mid, arr[mid], color = "orange")
        # pause to visualise the current element being considered
        plt.pause(0.1)  

        if arr[mid] == target:
            ax.bar(mid, arr[mid], color = "green")
            # pause to highlight the target element
            plt.pause(2.0)  
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
        ax.clear()
        ax.set_title("Binary Search Visualisation")
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")

        ax.bar(range(len(arr)), arr, color = "skyblue")
        # pause to display the updated array after the current iteration
        plt.pause(0.1)  
    
    return -1

if __name__ == "__main__":
    data = list(range(1, 101))
    target_value = 58

    index = visualise_binary_search(data, target_value)

    if index != -1:
        print(f"Target value {target_value} found at index {index}")
    else:
        print("Target value not found in the array.")
        
# keep the graph displayed until the user closes it        
plt.show()