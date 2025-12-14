from datasets import load_dataset

def load_data(sample_size=200):
    """
    Load SQuAD dataset from Hugging Face
    """
    dataset = load_dataset("squad", split=f"train[:{sample_size}]")
    return dataset


if __name__ == "__main__":
    data = load_data()
    print("Dataset loaded successfully!")
    print("Number of samples:", len(data))
    print(data[0])
