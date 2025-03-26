import argparse


def get_hash_from_filepath(filepath, ignore_name):
    with open(filepath, "rb") as file:
        content = file.read()
        hash_value = hash(content)
        return hash_value


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--f1", type=str, required=True, help="file 1")
    parser.add_argument("--f2", type=str, required=True, help="file 2")
    parser.add_argument(
        "--ignore-name", action="store_true", help="whether to ignore file names"
    )
    args = parser.parse_args()
    f1_hash = get_hash_from_filepath(args.f1, args.ignore_name)
    f2_hash = get_hash_from_filepath(args.f1, args.ignore_name)
    print(f"f1 hash: {f1_hash}")
    print(f"f2 hash: {f2_hash}")
    if f1_hash == f2_hash:
        print("Files are the same")
    else:
        print("Files are different")
