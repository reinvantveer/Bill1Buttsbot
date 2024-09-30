import tomllib

def main():
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)

    print(data)

if __name__ == '__main__':
    main()
