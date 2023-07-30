import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Recursively find all files with the given extension under the specified directory.
    """

    if suffix is None or path is None:
        return None

    files = []
    try:
        search_files(suffix, path, files)
    except FileNotFoundError as e:
        print(f"Error: {e}")

    return files

def search_files(suffix, path, files):
    #print(path)
    if os.path.isfile(path) and path.endswith(suffix):
        files.append(path)
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) and filename.endswith(suffix):
                files.append(file_path)
            elif os.path.isdir(file_path):
                search_files(suffix, file_path, files)




## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values
test_case_1 = find_files(".c", "testdir")
test_case_2 = find_files(".c", None)
test_case_3 = find_files(".c", "nonexistent_testdir/subdir2/subsubdir1")
test_case_4 = find_files("", "testdir")
test_case_5 = find_files(".c", "testdir/subdir3/subsubdir1/subdir2/subdir1/b.h")
test_case_6 = find_files(".h", "testdir/subdir3/subsubdir1/b.h")

print(f"Test 1: {test_case_1}") 
print(f"Test 2: {test_case_2}")
print(f"Test 3: {test_case_3}")
print(f"Test 4: {test_case_4}")
print(f"Test 5: {test_case_5}")
print(f"Test 6: {test_case_6}")


