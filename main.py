def main(x:int, y:int, z:int) -> int:
    return sum([x + y + z])


if __name__ == "__main__":
    result = main(1, 2, 3)
    print(f"Result: {result}")
