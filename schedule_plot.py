import matplotlib.pyplot as plt

def create_daily_schedule():
    # Define the schedule data
    activities = [
        "Sleep", "Wake Up", "Breakfast", "Work", "Lunch", 
        "Work", "Dinner", "Relax", "Sleep"
    ]
    times = [
        "12:00 AM", "7:00 AM", "8:00 AM", "9:00 AM", "12:00 PM",
        "1:00 PM", "6:00 PM", "8:00 PM", "10:00 PM"
    ]
    # Convert times to 24-hour format for plotting
    hours = [0, 7, 8, 9, 12, 13, 18, 20, 22]
    
    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot the timeline as a line chart
    ax.plot(hours, [1]*len(hours), marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
    
    # Add labels for each activity
    for i, (activity, time) in enumerate(zip(activities, times)):
        ax.text(hours[i], 1.02, activity, ha='center', va='bottom', fontsize=10)
        ax.text(hours[i], 0.98, time, ha='center', va='top', fontsize=8, color='gray')
    
    # Customize the plot
    ax.set_title("My Daily Schedule Timeline", fontsize=14, pad=20)
    ax.set_xlabel("Time of Day (24-hour format)", fontsize=12)
    ax.set_ylabel("Activities", fontsize=12)
    
    # Set x-axis ticks and labels
    ax.set_xticks(range(0, 25, 1))
    ax.set_xticklabels([f"{h}:00" for h in range(0, 25)], rotation=45)
    
    # Remove y-axis as it's not needed
    ax.set_yticks([])
    
    # Set limits
    ax.set_xlim(0, 24)
    ax.set_ylim(0.9, 1.1)
    
    # Add grid
    ax.grid(True, axis='x', linestyle='--', alpha=0.7)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save and show the plot
    plt.savefig('daily_schedule.png')
    plt.show()

if __name__ == "__main__":
    create_daily_schedule()