import numpy as np

def page_rank(transition_matrix, damping_factor=0.85, max_iter=100, tol=1e-6):
    """
    Computing the PageRank of nodes given a transition matrix.

    Parameters:
    - transition_matrix: A square numpy array where element (i, j) represents the probability of moving 
                         from page j to page i.
    - damping_factor: The probability a user continues clicking links; default is usually set to 0.85.
    - max_iter: Maximum number of iterations to run the algorithm.
    - tol: Tolerance for convergence checking.

    Returns (values returned):
    - rank: A numpy array containing the PageRank score for each node.
    """
    n = transition_matrix.shape[0]
    
    # Initializing the rank vector with an equal probability for each page.
    rank = np.ones(n) / n
    
    # Pre-computing the teleportation vector used for random jumping.
    teleport = np.ones(n) / n

    for iteration in range(max_iter):
        # Computing the new rank vector using the PageRank formula:
        new_rank = (1 - damping_factor) * teleport + damping_factor * transition_matrix.dot(rank)

        # Checking convergence using the L1 norm between iterations
        if np.linalg.norm(new_rank - rank, 1) < tol:
            print(f"Converged after {iteration + 1} iterations.")
            return new_rank

        rank = new_rank

    print("Maximum iterations reached without convergence.")
    return rank

def construct_transition_matrix(link_matrix):
    """
    Creating a transition matrix from a given link matrix.

    The link_matrix is a square numpy array where element (i, j) is 1 if there is a link from page j to page i,
    and 0 otherwise.

    Parameters:
    - link_matrix: A square numpy array with binary values (1/0).

    Returns:
    - transition_matrix: A column-stochastic matrix suitable for the PageRank algorithm.
    """
    n = link_matrix.shape[0]
    transition_matrix = np.zeros((n, n))
    
    # Iterating over every column (source page)
    for j in range(n):
        out_links = np.sum(link_matrix[:, j])
        if out_links == 0:
            # If a page has no out-links, assume a uniform distribution over all pages.
            transition_matrix[:, j] = 1 / n
        else:
            transition_matrix[:, j] = link_matrix[:, j] / out_links
    
    return transition_matrix

if __name__ == "__main__":
    # data simulation of 5 theoretical web pages:
    # - Page 1 links to Page 2 and Page 3.
    # - Page 2 links to Page 3.
    # - Page 3 links to Page 1.
    # - Page 4 links to Page 1, Page 3, and Page 5.
    # - Page 5 links to Page 1 and Page 2.
    #
    # The matrix is structured so that each column j represents the links from page j.
    # Each row i represents if page i is linked from page j.
    
    link_matrix = np.array([
        # P1  P2  P3  P4  P5   <-- Source Page (links from)
        [  0,  0,  1,  1,  1],  # Page 1 receives links from P3, P4, P5
        [  1,  0,  0,  0,  1],  # Page 2 receives links from P1, P5
        [  1,  1,  0,  1,  0],  # Page 3 receives links from P1, P2, P4
        [  0,  0,  0,  0,  0],  # Page 4 receives no incoming links
        [  0,  0,  0,  1,  0]   # Page 5 receives a link from P4
    ], dtype=float)

    # Creating the transition matrix using the example link matrix.
    transition_matrix = construct_transition_matrix(link_matrix)

    # Computing the PageRank scores for the pages.
    ranks = page_rank(transition_matrix)
    
    # Output of the computed PageRank scores.
    print("PageRank Scores:")
    for i, score in enumerate(ranks):
        print(f"Page {i + 1}: {score:.4f}")
