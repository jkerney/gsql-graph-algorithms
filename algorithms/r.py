from genericpath import isdir
import os

Documentation = {
    'betweenness_centrality': 'betweenness-centrality',
    'closeness': 'closeness-centrality',
    'connected_components': 'connected-components',
    'cosine': 'cosine-similarity-of-neighborhoods-batch',
    'cycle_detection': 'cycle-detection',
    'estimated_diameter': 'estimated-diameter',
    'greedy_graph_coloring': 'greedy-graph-coloring',
    'jaccard': 'jaccard-similarity-of-neighborhoods-batch',
    'k_core': 'k-core-decomposition',
    'k_means': 'https://raw.githubusercontent.com/tigergraph/gsql-graph-algorithms/master/algorithms/schema-free/kmeans.gsql',
    'k_nearest_neighbors': 'k-nearest-neighbors-cosine-neighbor-similarity-all-vertices-batch',
    'label_propagation': 'label-propagation',
    'local_clustering_coefficient': 'local-clustering-coefficient',
    'louvain_distributed': 'louvain-method-with-parallelism-and-refinement',
    'louvain': 'louvain-method-with-parallelism-and-refinement',
    'maximal_independent_set': 'maximal-independent-set',
    'minimum_spanning_forest': 'minimum-spanning-forest-msf',
    'minimum_spanning_tree': 'minimum-spanning-tree-mst',
    'pagerank': 'pagerank',
    'strongly_connected_components': 'strongly-connected-components-1',
    'shortest_path': 'single-source-shortest-path-weighted',
    'triangle_counting': 'triangle-counting' 
    }




r = 'algorithms'
s = set()
def recursvie_dir(path):
    for item in os.listdir(path):
        new_path = os.path.join(path, item)
        if os.path.isdir(new_path):
            if not has_subdirectories(new_path):
                s.add(new_path)
            recursvie_dir(new_path)

def has_subdirectories(path):
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            return True
    return False

recursvie_dir('algorithms')
for dir in s:
    ignore_dir = ['algorithms/GraphML/Embeddings/Node2Vec', 'algorithms/GraphML/Embeddings/FastRP']
    if dir not in ignore_dir :
        with open(os.path.join(dir, 'README.md'), 'w') as handler:
            title = dir.split('/')[-1]
            anchor = Documentation[title]
            link = f'https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#{anchor}'
            template = f'## {title}\n### Documentation : {link}\n'
            template += f'### Install {title} via Tigergraph CLI\n'
            template += f'```bash\n$ tg box algos install {title}\n```\n'
            template += f'### Install {title} via GSQL terminal\n'
            template += f'```bash\n$ BEGIN \n\n# Paste query code after BEGIN command\n\n$ <{title}_gsql_code>\n$ END \n$ INSTALL QUERY {title}\n```'

            handler.write(template)


