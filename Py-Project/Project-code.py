# FitnessClass class for class listings
class FitnessClass:
    def __init__(self, class_id, name, capacity):
        self.class_id = class_id
        self.name = name
        self.capacity = capacity
        self.booked_spots = 0
        self.attendance_list = []

    def update_class_details(self, name=None, capacity=None):
        if name:
            self.name = name
        if capacity:
            self.capacity = capacity

    def available_spots(self):
        return self.capacity - self.booked_spots

    def __repr__(self):
        return f"Class: {self.name}, Capacity: {self.capacity}, Booked: {self.booked_spots}"

# FitnessCenter class for managing bookings and attendance
class FitnessCenter:
    def __init__(self):
        self.classes = {}

    # CRUD operations for class listings
    def create_class(self, class_id, name, capacity):
        if class_id in self.classes:
            return f"Class ID {class_id} already exists."
        self.classes[class_id] = FitnessClass(class_id, name, capacity)
        return f"Class {name} created with ID {class_id}."

    def read_class(self, class_id):
        if class_id in self.classes:
            return self.classes[class_id]
        return "Class not found."

    def update_class(self, class_id, name=None, capacity=None):
        if class_id in self.classes:
            self.classes[class_id].update_class_details(name, capacity)
            return f"Class {class_id} updated."
        return "Class not found."

    def delete_class(self, class_id):
        if class_id in self.classes:
            del self.classes[class_id]
            return f"Class {class_id} deleted."
        return "Class not found."

    # Manage bookings for classes
    def manage_bookings(self, class_id):
        if class_id not in self.classes:
            return "Class not found."
        fitness_class = self.classes[class_id]
        if fitness_class.available_spots() > 0:
            fitness_class.booked_spots += 1
            return f"Booked spot in {fitness_class.name}. Remaining spots: {fitness_class.available_spots()}."
        return f"Class {fitness_class.name} is fully booked."

    # Track class attendance
    def track_class_attendance(self, class_id, attendees):
        if class_id not in self.classes:
            return "Class not found."
        fitness_class = self.classes[class_id]
        fitness_class.attendance_list = attendees
        return f"Attendance for class {fitness_class.name} recorded: {len(attendees)} attendees."

# Menu loop and interaction
fc = FitnessCenter()  # Instantiate the FitnessCenter object

while True:
    print("\n--- Fitness Center Menu ---")
    print("1. Create a class")
    print("2. View a class")    
    print("3. Update a class")
    print("4. Delete a class")
    print("5. Book a spot in a class")
    print("6. Track class attendance")
    print("7. Exit")
    
    choice = input("Choose an option (1-7): ")

    if choice == "1":
        class_id = int(input("Enter class ID: "))
        name = input("Enter class name: ")
        capacity = int(input("Enter class capacity: "))
        result = fc.create_class(class_id, name, capacity)
        print(result)
    
    elif choice == "2":
        class_id = int(input("Enter class ID to view: "))
        result = fc.read_class(class_id)
        print(result)
    
    elif choice == "3":
        class_id = int(input("Enter class ID to update: "))
        name = input("Enter new class name (leave blank to keep unchanged): ")
        capacity = input("Enter new class capacity (leave blank to keep unchanged): ")
        capacity = int(capacity) if capacity else None
        result = fc.update_class(class_id, name, capacity)
        print(result)
    
    elif choice == "4":
        class_id = int(input("Enter class ID to delete: "))
        result = fc.delete_class(class_id)
        print(result)
    
    elif choice == "5":
        class_id = int(input("Enter class ID to book a spot: "))
        result = fc.manage_bookings(class_id)
        print(result)
    
    elif choice == "6":
        class_id = int(input("Enter class ID to track attendance: "))
        attendees = input("Enter attendees (comma-separated): ").split(",")
        attendees = [attendee.strip() for attendee in attendees]
        result = fc.track_class_attendance(class_id, attendees)
        print(result)
    
    elif choice == "7":
        print("Exiting the Fitness Center app.")
        break
    
    else:
        print("Invalid option. Please try again.")
