def modify_content(content):
    return content.upper()

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            original_content = file.read()
            print(" File read successfully.")
            print (original_content)

        modified_content = modify_content(original_content)

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            new_content = new_file.read()
            print(f" Modified content written to '{new_filename}'.")
            print (new_content)

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename and try again.")
    except IOError:
        print(" Error: Unable to read or write the file due to an I/O issue.")
    except Exception as e:
        print(f" Unexpected error: {e}")

if __name__ == "__main__":
    main()
