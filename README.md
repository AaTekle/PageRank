# PageRank Implementation

The PageRank algorithm was developed by Google to rank web pages in their search results, helping search engines rank web pages based on the structure of links between them. 

PageRank primarily ranks pages based on their popularity. Other variables like similarity are not valued as much as popularity when thinking about rankings within this algorithm.

## Applicability of PageRank

- **Usage within Search Engines:**  
  *   Used to measure the relevance of web pages. Helping users find credible ranked information quickly.

## PageRank Vocabulary List:

Simple dictionary for the concepts being talked about within the code:

- **PageRank:**  
  * A numerical score assigned to a web page based on the structure and quality of links pointing to it. It reflects the page's relative importance.

- **Rank Vector:**  
  * A vector/array that holds the PageRank scores for all pages in the network. Each entry corresponds to a page's current importance score.

- **Transition Matrix:**  
  * The matrix is column-stochastic, meaning that the sum of the entries in each column is 1. This is done by normalizing the entries for each page by its total number of out-links.

  * The transition matrix is a column-stochastic matrix that represents the probabilities of moving from one page to another. It is constructed from the link structure of the web: Each column represents a source page (a page that contains links). Each row represents a destination page (a page that is linked to).
  
  * If a page has no out-links, it is treated as linking to all pages uniformly.


- **Link Matrix:**  
  * A binary matrix (matrix that only contains 0's and 1's) representing the presence or absence of links between pages. Each entry is `1` if there's a link from one page to another and `0` otherwise.

- **Teleportation (Random Jump):**  
  * A process that allows a user to jump to any page regardless of the link structure. It prevents pages with no in-links from having zero rank, ensuring every page gets a minimal score.

- **Damping Factor:**  
  * A value (commonly 0.85) representing the probability that a user will follow a link rather than teleport. It balances the influence of the network structure and random jumps.

  *  The value 0.85 is standardized because researchers have stated that it closely matches real user behavior, users tend to follow links about 85% of the time and choose a random page about 15% of the time. This balance allows the algorithm to simulate rankings that reflect the overall link structure of the web. 

  * **Sources for the 85% statistic:**
    * The Anatomy of a Large-Scale Hypertextual Web Search Engine" (1998) by Sergey Brin and Lawrence Page: https://research.google/pubs/the-anatomy-of-a-large-scale-hypertextual-web-search-engine/

 
- **Link Contribution:**  
  * The portion of the PageRank score that a page receives from other pages linking to it. It is calculated based on the PageRank of the linking pages and the number of their outgoing links.

- **$L1$ Norm:**  
  * A measure of difference between two vectors. It is computed as the sum of the absolute differences of the vector elements. When applied onto the PageRank algorithm, it’s used to check the difference between successive rank vectors to determine convergence.

- **Convergence:**  
  * The point in the iterative process when the rank vector stops changing significantly (i.e., the L1 norm of the change falls below a specified threshold). At this point, the algorithm terminates.

## Math behind PageRank

* The PageRank score of a page is computed using the following formula:

```math
PR(i) = \frac{1 - d}{N} + d \sum_{j \in B_i} \frac{PR(j)}{L(j)}
```

Where:

- $PR(i)$ is the PageRank of page $i$.
- $d$ is the damping factor (usually set to 0.85). This represents the probability that a user will continue clicking on links.
- $N$ is the total number of pages.
- $B_i$ is the set of pages that link to page $i$.
- $L(j)$ is the number of out-links on page $j$.
- $i$ is the index that represents a particular page in the network
- $j$ is used as an index variable representing each page that links to page $i$.

The formula has two parts:
1. **Teleportation (Random Jump):** $(1-d)/N$ ensures every page gets a minimum rank even if no other pages link to it.
2. **Link Contribution:** $d \sum_{j \in B_i} (PR(j)/L(j))$ accumulates the rank from pages that link to page $i$.


### Other Math: L1 Norm and Convergence

The PageRank algorithm uses an iterative process where the rank vector is updated repeatedly until it stabilizes. The stabilization is determined using the **L1 norm**.

Consider two successive PageRank vectors:
- $r^{(k)}$ for iteration $k$ ($k$ represents the current stage)
- $r^{(k+1)}$ for iteration $k+1$ ($k+1$ represents the next stage following the current one.)

The L1 norm of the difference between these two vectors is defined as:

```math
r^{(k+1)} - r^{(k)} \|_1 = \sum_{i=1}^{N} \left| r_i^{(k+1)} - r_i^{(k)} \right|
```


Where $N$ is the total number of pages.

- The L1 norm sums up the absolute differences in the PageRank values for every page between two iterations.
- When the L1 norm falls below a specified tolerance, it indicates that the PageRank values have converged. At this point, further iterations will not significantly change the rankings, and the algorithm can terminate.

This convergence check helps the algorithm stops in a reasonable time while maintaining accuracy.

## Data Used in the Code

The code within my python script simulates a small network of 5 web pages with the following link structure:
- **Page 1** links to **Page 2** and **Page 3**.
- **Page 2** links to **Page 3**.
- **Page 3** links to **Page 1**.
- **Page 4** links to **Page 1**, **Page 3**, and **Page 5**.
- **Page 5** links to **Page 1** and **Page 2**.

The link matrix in the code is setup to where each column corresponds to the outgoing links from a page, and each row corresponds to incoming links for a page.

## PageRank Scores Explained
A score closer to 1 indicates that a page is more important within the network, while a score closer to 0 suggests a lower level of importance relative to the other pages.

Here are the PageRank scores for each page in the network:

- **Page 1:** 0.3651  
- **Page 2:** 0.2015  
- **Page 3:** 0.3649  
- **Page 4:** 0.0300  
- **Page 5:** 0.0385

## Score Interpretations

- **Relative Importance within page scores:**  
  * PageRank scores show how important each page is relative to the others. A higher score means the page is more influential, while a lower score means it's less significant compared to pages with higher scores.

- **Score Distribution in the Code:**  
  - **Page 1 and Page 3:** Both scores around 0.365, making them the most influential pages in the network.
  - **Page 2:** With a score of 0.2015, this page had a moderate level of influence.
  - **Page 4 and Page 5:** These pages scored 0.0300 and 0.0385, showing they are much less significant in comparison to the other pages.





