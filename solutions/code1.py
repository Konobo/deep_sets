items_test_len_range = np.arange(5, 50 + 1)
items_test_len = np.random.choice(items_test_len_range, dataset_len, replace=True)
mnist_items_test = []
for i in range(dataset_len):
    mnist_items_test.append(np.random.choice(mnist_items_range, size=items_test_len[i], replace=True))
