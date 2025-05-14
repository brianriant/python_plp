def process_file():

    """
    Read a file, modify its content, and write to a new file with '_modified' suffix.

    The function:
    - Prompts user for input filename
    - Reads content from input file
    - Converts content to uppercase
    - Creates new filename with '_modified' suffix
    - Writes modified content to new file

    Error handling:
    - FileNotFoundError: If input file doesn't exist
    - PermissionError: If file access is denied
    - General exceptions: For other unexpected errors

    Returns:
        None

    Example:
        If input file is 'test.txt', creates 'test_modified.txt' with uppercase content
    """
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

    finally:
        input_file.close()
        output_file.close()

if __name__ == "__main__":
    process_file()
