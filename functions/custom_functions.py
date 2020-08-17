from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score, silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

def k_means_fitted(n_clusters, X):
    '''Fit the K-Means Cluster Algorithm to a series (X)'''
    
    k_means = KMeans(n_clusters=n_clusters)
    k_means.fit(X)
    y_hat = k_means.predict(X)
    
    return k_means

def calc_calinski_harabasz_score(k_means, X):
    '''Calculate Calinski Harabasz score from k_means object'''
    
    # Store labels from our model
    labels = k_means.labels_
    
    # Calculate Calinski Harabasz Score
    score = calinski_harabasz_score(X, labels)
    
    return score

def calc_silhouette_score(k_means, X):
    '''Calculate silhouette coefficient from k_means object'''
    
    # Store labels from our model
    labels = k_means.labels_

    # Calculate Silhouette Score
    score = silhouette_score(X, labels)
    
    return score

def plot_clusters(k_means, X, y, score, x_label='X_label', y_label='Y_label', save_fig=False):
    '''Visualize the Cluster Groups formed'''
    
    y_hat = k_means.predict(X)
    k = k_means.n_clusters
    
    # Visualize the results of k-means clustering algorithm
    
    # Set size of chart
    plt.figure(figsize=(6, 5), dpi=80)

    # Plot Data
    ax = sns.scatterplot(X[:, 0], X[:, 1], markers = y_hat, hue=y, size = 30, legend=False, palette='Set1');
    # Plot Cluster Centers
    cl_centers = k_means.cluster_centers_
    ax =sns.scatterplot(cl_centers[:, 0], cl_centers[:, 1], s=100, color=".2");

    # Title and Axis
    sns.set(style='darkgrid', font='sans-serif');
    score = round(score, 2)
    ax.set_title('Visualization of Clusters Formed\n(K:{}    Score:{})'.format(k, score));
    ax.set(xlabel=x_label, ylabel=y_label);
    
    # Save Figure
    
    if save_fig:
        plt.savefig('cluster_plot_k_of_{}'.format(k))

def calc_score_for_each_k(k_range, X, metric='variance'):
    '''Calculate the score acrosa a range of k values.  metric may be variance of silhouette'''
    
    # List to gather the scores
    scores = []
    best_score = 0
    best_k = None
    
    # Calculate score for Variance / Calinski Harabasz
    if metric=='variance':   
        for k in k_range:
            k_means = k_means_fitted(k, X)
            score = calc_calinski_harabasz_score(k_means, X)
            scores.append(score)
            if score > best_score:
                best_score = score
                best_k = k
        print('Best Variance Score: {} (K={})'.format(round(best_score,2), best_k))
    
    # Calculate score for Silhouette
    elif metric=='silhouette':
        for k in k_range:
            k_means = k_means_fitted(k, X)
            score = calc_silhouette_score(k_means, X)
            scores.append(score)
            if score > best_score:
                best_score = score
                best_k = k
        print('Best Silhouette Score: {} (K={})'.format(round(best_score,2), best_k))
        
    return scores, best_score, best_k

def plot_k_scores(k_range, scores, best_score, best_k, metric='Variance', save_fig=False):
    '''Visualize the scores at different K values'''
    
    # Set size of chart
    plt.figure(figsize=(6, 5), dpi=80)

    # Plot Data
    ax = sns.lineplot(x=k_range, y=scores, marker='o', dashes=False)
    # Plot Market for Best Score
    ax = sns.scatterplot([best_k], [best_score], marker='o', s=100, color='r');
    # Text for Best Score
    text = '(K:{}   {}:{})'.format(best_k, metric, round(best_score, 2))
    ax.text(0.98*best_k, best_score, text, horizontalalignment='right', size='small', weight='bold')
    
    # Title and Axis
    sns.set(style='darkgrid', font='sans-serif');
    best_score = round(best_score, 2)
    ax.set_title('Elbow for K-Means Clustering\n');
    ax.set(xlabel='Number of Clusters', ylabel='Score ({})'.format(metric));
    
    # Save Figure    
    if save_fig:
        plt.savefig('cluster_plot_k_of_{}'.format(k))