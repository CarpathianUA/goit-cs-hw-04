import os

from faker import Faker

from constants.files import NUM_FILES, FILES_DIR

fake = Faker()


def seed_files():
    """
    Generate and seed mock text files in a specified directory.

    This function checks if the specified directory exists, creates it if it doesn't,
    and then generates a specified number of mock text files.
    The files are filled with random text generated using the fake.text() method.

    Parameters:
    - None

    Returns:
    - None
    """
    if not os.path.exists(FILES_DIR):
        os.mkdir(FILES_DIR)
    for i in range(NUM_FILES):
        file_path = f"{FILES_DIR}/mock_text_{i}.txt"
        with open(file_path, "w") as file:
            for _ in range(NUM_FILES):
                file.write(fake.text() + "\n")


if __name__ == "__main__":
    seed_files()
