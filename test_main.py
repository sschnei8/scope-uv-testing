from main import main

def test_main():
    assert main(1, 2, 3) == 6

if __name__ == "__main__":
    test_main()
    print("Everything passed")