import os


class PathManager:
    @staticmethod
    def create_path(directory, filename):
        """
        Constructs a full path by combining the specified directory and filename.

        Args:
            directory (str): The directory path where the file is located or needs to be placed.
            filename (str): The name of the file.

        Returns:
            str: The full path combining the directory and the filename.
        """
        return os.path.join(directory, filename)

    @staticmethod
    def get_list_of_files(directory):
        """
        Retrieves a list of filenames from the specified directory.

        Args:
            directory (str): The directory from which to list all files.

        Returns:
            list: A list of filenames found in the specified directory.
        """
        return os.listdir(directory)
