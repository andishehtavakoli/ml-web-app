from src.data_preprocessing import mnist_data_load, mnist_data_prepare


data = mnist_data_load()
X, y = mnist_data_prepare(data)


