import os

def generate_tree(dir_path, prefix=""):
    contents = os.listdir(dir_path)
    # Exclude the .git directory from the contents
    contents = [item for item in contents if item != ".git"]
    
    pointers = ['├── '] * (len(contents) - 1) + ['└── ']
    for pointer, path in zip(pointers, contents):
        full_path = os.path.join(dir_path, path)
        if os.path.isdir(full_path):
            print(f"{prefix}{pointer}{path}")
            generate_tree(full_path, prefix + "│   ")
        else:
            print(f"{prefix}{pointer}{path}")

def main():
    print("```\n.")
    generate_tree(".")
    print("```")

if __name__ == "__main__":
    main()
