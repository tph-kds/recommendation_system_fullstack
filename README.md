<h1 align="center">RECOMMENDATION SYSTEM FULLSTACK PROJECT</h1>

<img src="https://raw.githubusercontent.com/tph-kds/image_storages/main/images/svgs/recommendation_system/logo_bg.png" width="800">

## I. Introduce

### 1. The goals of project
Studying and developing for the real-life project with recommendation system topic use integrated continous pipeline. Moreover, its application will deploy into the social media such as website and help some people approach closely about boardgame.   


### 2. Data Sources
Datasets are taken from link > https://www.kaggle.com/datasets/jvanelteren/boardgamegeek-reviews/
But `Boardgame Reviewer` datasets are originally extracted by `BoardgameGeek` website. - one of the popular games' information website around the world.


> **BoardgameGeek:**
>
Link website: https://boardgamegeek.com/

### 3. Steps of project
Boardgame recommendation systems is to assist researchers, developers and enthusiasts in prototyping, experimenting with and bringing to production a range of classic and state-of-the-art recommendation systems about thinking game model.



This repository contains examples and best practices for building recommendation systems, provided as Jupyter notebooks, between some folders and used methods. The examples detail our learnings on five key tasks:

- [Prepare Data](docs/01_prepare_data): Preparing and loading data for each recommendation algorithm.
- [Model](docs/00_quick_start): Building models using various classical and recommendation algorithms such as Collaborative Filtering Based ([CFB](https://medium.com/@evelyn.eve.9512/collaborative-filtering-in-recommender-system-an-overview-38dfa8462b61)) and Content Based ([CB](https://developers.google.com/machine-learning/recommendation/content-based/basics)) Hybrid RS ([HRS](https://www.kaggle.com/code/iambideniz/hybrid-recommender-system)) and Merge Average Based RS ([MAB](https://www.kaggle.com/code/iambideniz/hybrid-recommender-system)).
- [Evaluate](docs/03_evaluate): Evaluating algorithms with offline metrics.
- [Model Select and Optimize](docs/04_model_select_and_optimize): Fine tuning and optimizing hyperparameters for recommendation models.
- [Deployment](docs/05_Deployment): Deployment models in a production environment on Website by using ([Flask Framework](https://flask.palletsprojects.com/en/3.0.x/)).

Several utilities are provided in [src](src) to support common tasks such as complete seperate stages and algorithmns and combine them to receive a accuracy and confident result throughout [src/Hydrid RS](src/Hybrid_RS/) . See the detailly processing stream and workflow of all project, you can run at [main.py](src/main.py).

For a more detailed overview of the repository, please see the documents on the [github page](https://github.com/tph-kds/recommendation_system_fullstack).

For some of the practical deployment where recommendation systems have been applied, see [deployment](deployment).  


### 4. Data Lineage ([Project's Workflow](workflow.png))

<img src="https://raw.githubusercontent.com/tph-kds/image_storages/main/images/svgs/recommendation_system/logo_bg.png" width="800">


## II. Getting Started

We recommend [conda](https://docs.conda.io/projects/conda/en/latest/glossary.html?highlight=environment#conda-environment) for environment management, and [VS Code](https://code.visualstudio.com/) for development. To install the recommendation system about boardgames topic package and run an example notebook on Linux/WSL:

```bash
# 1. Install gcc if it is not installed already. On Ubuntu, this could done by using the command
# sudo apt install gcc

# 2. Create and activate a new conda environment
conda create -n <environment_name> python=3.9
conda activate <environment_name>

# 3. Install the core recommenders package. It can run all the CPU notebooks.
pip install rs_boardgame

# 4. create a Jupyter kernel
python -m ipykernel install --user --name <environment_name> --display-name <kernel_name>

# 5. Clone this repo within VSCode or using command line:
git clone https://github.com/tph-kds/recommendation_system_fullstack

# 6. Within VSCode:
#   a. Open a notebook, e.g., examples/00_quick_start/sar_movielens.ipynb;  
#   b. Select Jupyter kernel <kernel_name>;
#   c. Run the notebook.
```

For more information about setup on other platforms (e.g., Windows and macOS) and different configurations, see the [Setup Guide](SETUP.md).


## III. Algorithms

The table below lists the recommendation algorithms currently available in the repository. Notebooks are linked under the Example column as Quick start, showcasing an easy to run example of the algorithm, or as Deep dive, explaining in detail the math and implementation of the algorithm.

| Algorithm | Type | Description | Example |
|-----------|------|-------------|---------|
| Similarity Based Recommendation Systems (SBRS) | Collaborative Filtering | It relies on the similarity value between items to make recommendations. The system calculates how similar items are to each other based on user interactions, such as ratings, views, or purchases. When a user interacts with an item, the system recommends other items that are similar based on these calculated similarities. This approach is particularly useful for generating recommendations when there is a large number of users and the focus is on the relationships between items rather than users." This description focuses on the key aspects of similarity-based item-item recommendation systems, without conflating it with other techniques like matrix factorization. It works in the CPU/GPU environment.| [Quick start](examples/00_quick_start/als_movielens.ipynb) / [Deep dive](examples/02_model_collaborative_filtering/als_deep_dive.ipynb) |
| Similarity Based Recommendation Systems (SBRS) | Content Based Filtering | Content-based filtering is another popular recommendation technique that, like item-item collaborative filtering, relies on similarity. However, instead of using the similarity between items based on user interactions, content-based filtering uses the attributes or features of the items themselves. It works in the CPU/GPU environment. | [Quick start](examples/00_quick_start/sequential_recsys_amazondataset.ipynb) |
| Weight-rating<sup>*</sup> | Hydrid Based | Weight-rating methods are used to aim to enhance the accuracy of the recommendations by assigning different weights to items or features based on their importance or relevance. It works in the CPU/GPU environment. | [Quick start](examples/00_quick_start/sequential_recsys_amazondataset.ipynb) |
| Mergetive Result Average<sup>*</sup> | Merge Arverage Based |  Mergetive Result Average algorithm that aims to capture and merge all of method results throughout averaging between the weights represents the mutual importance of the results - 3 methods which are used above. These weights can be adjusted during fine tuning processing. It works in the CPU/GPU environment. | [Quick start](examples/00_quick_start/sequential_recsys_amazondataset.ipynb) |



### Algorithm Comparison

We provide a [benchmark notebook](examples/06_benchmarks/movielens.ipynb) to illustrate how different algorithms could be evaluated and compared. In this notebook, the project's dataset is split into training/test sets at a 75/25 ratio using a stratified split. A recommendation model is trained using each of the collaborative filtering algorithms below. We utilize empirical parameter values reported in literature [here](http://mymedialite.net/examples/datasets.html). For ranking metrics we use `k=10` (top 10 recommended items). In this table we show the results on 20,588 boardgame name, running the algorithms for 10 epochs.

| Algo | MAP | Precision@k | Recall@k |
| --- | --- | --- |  --- |
| [CFB](examples/00_quick_start/als_movielens.ipynb) | 0.003428 |	0.012902 | 0.010606 |
| [CB](examples/02_model_collaborative_filtering/cornac_bivae_deep_dive.ipynb) | 0.146126	| 0.475077 |	0.219145 |
| [HRS](examples/02_model_collaborative_filtering/cornac_bpr_deep_dive.ipynb) | N/A	| N/A | N/A |
| [MAB](examples/02_model_collaborative_filtering/cornac_bpr_deep_dive.ipynb) | N/A	|  0.069507 |	0.000491 |


## IV. References

- **FREE COURSE**: M. González-Fierro, "Recommendation Systems: A Practical Introduction", LinkedIn Learning, 2024. [Available on this link](https://www.linkedin.com/learning/recommendation-systems-a-practical-introduction).
- D. Li, J. Lian, L. Zhang, K. Ren, D. Lu, T. Wu, X. Xie, "Recommender Systems: Frontiers and Practices", Springer, Beijing, 2024. [Available on this link](https://www.amazon.com/Recommender-Systems-Frontiers-Practices-Dongsheng/dp/9819989639/).

- KAGGLE Jesse Van Elteren. Boardgamegeek reviews.
https://www.kaggle.com/datasets/jvanelteren/boardgamegeek-reviews/
, 2022. [Online; accessed January 8, 2024].

- GEEK. Boardgamegeek. https://boardgamegeek.com/. [Online; accessed January 8, 2024].

- GITHUB. Boardgame recommendation system. https://github.com/tph-kds/recommendation_system_fullstack.git/
. [Online; accessed January 8, 2024].

- NVIDIA. Recommendation system.
https://www.nvidia.com/en-us/glossary/data-science/recommendation-system/
. [Online; accessed January 8, 2024].