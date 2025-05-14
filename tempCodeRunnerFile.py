def process_file():
    try:
        # Get input filename from user
        input_filename = input("Enter the filename to process: ")

        # Try to open and read the file
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()

        # Modify content (capitalize everything)
        modified_content = content.upper()

        # Create output filename by adding '_modified' before extension
        output_filename = input_filename.rsplit('.', 1)
        output_filename = f"{output_filename[0]}_modified.{output_filename[1]}"

        # Write modified content to new file
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied accessing the file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    process_file()