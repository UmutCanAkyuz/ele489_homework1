import numpy as np

def knn_predict(X_train, y_train, X_test, k, distance_metric='euclidean'):
    
    predictions = []
    
    for x in X_test:
        # Compute distances from x to each point in X_train
        if distance_metric == 'euclidean':
            # Euclidean distance
            dists = np.sqrt(np.sum((X_train - x)**2, axis=1))
        elif distance_metric == 'manhattan':
            # Manhattan distance 
            dists = np.sum(np.abs(X_train - x), axis=1)
        else:
            raise ValueError("Unsupported distance metric. Choose euclidean or manhattan.")

        # Indices of the k nearest neighbors
        idx_sorted = np.argsort(dists)
        k_nearest = idx_sorted[:k]
        k_labels = y_train[k_nearest]

        # Majority vote
        #Determining the predicted class via majority vote
        values, counts = np.unique(k_labels, return_counts=True)
        majority_class = values[np.argmax(counts)]
        predictions.append(majority_class)
        
    return np.array(predictions)
